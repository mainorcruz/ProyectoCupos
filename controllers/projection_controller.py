"""Controlador de proyección de cupos basado en requisitos y expedientes."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Set

from models.student import AcademicRecord, Student
from models.study_plan import StudyPlan
from models.course import Course


@dataclass
class CourseProjection:
    """Resultado de la proyección de cupos para un curso."""

    course: Course
    eligible_students: List[Student] = field(default_factory=list)
    already_approved: List[Student] = field(default_factory=list)
    currently_enrolled: List[Student] = field(default_factory=list)

    @property
    def projected_demand(self) -> int:
        """Demanda proyectada = estudiantes que necesitan cupo (no aprobado, no matriculado, cumplen requisitos)."""
        return len(self.eligible_students)

    @property
    def total_approved(self) -> int:
        return len(self.already_approved)

    @property
    def total_enrolled(self) -> int:
        return len(self.currently_enrolled)


class ProjectionController:
    """Genera proyecciones de cupos para cursos de un plan de estudios."""

    def __init__(self, plan: StudyPlan, record: AcademicRecord):
        self.plan = plan
        self.record = record
        self._current_period = self._detect_current_period()

    def _detect_current_period(self) -> tuple:
        """Detecta el (año, período) más reciente con cursos matriculados en el expediente."""
        best = ("", "")
        for student in self.record.students.values():
            for r in student.enrolled_records:
                candidate = (r.year or "", r.period or "")
                if candidate > best:
                    best = candidate
        return best

    def _student_is_active(self, student: Student) -> bool:
        """True si el estudiante tiene cursos matriculados en el período más reciente detectado."""
        year, period = self._current_period
        if not year:
            # Sin información de año, basta con tener algún curso matriculado
            return bool(student.enrolled_courses)
        return any(
            (r.year or "") == year and ((not period) or (r.period or "") == period)
            for r in student.enrolled_records
        )

    def project_course(self, course_code: str) -> CourseProjection | None:
        """Proyecta la demanda de cupos para un curso específico."""
        course = self.plan.get_course(course_code)
        if not course:
            return None

        projection = CourseProjection(course=course)

        for student in self.record.students.values():
            approved = student.approved_courses
            enrolled = student.enrolled_courses

            # Solo considerar estudiantes activos en el período más reciente
            if not self._student_is_active(student):
                continue

            if course_code in approved:
                projection.already_approved.append(student)
            elif course_code in enrolled:
                projection.currently_enrolled.append(student)
            elif course.prerequisites_met(approved | enrolled):
                projection.eligible_students.append(student)

        return projection

    def project_cycle(self, cycle: int) -> List[CourseProjection]:
        """Proyecta cupos para todos los cursos de un ciclo."""
        courses = self.plan.get_courses_by_cycle(cycle)
        return [self.project_course(c.code) for c in courses if self.project_course(c.code)]

    def project_selected_courses(self, course_codes: List[str]) -> List[CourseProjection]:
        """Proyecta cupos para una lista de cursos seleccionados."""
        projections = []
        for code in course_codes:
            proj = self.project_course(code)
            if proj:
                projections.append(proj)
        return projections

    def get_student_eligible_courses(self, student_id: str) -> List[Course]:
        """Obtiene los cursos para los que un estudiante es elegible."""
        student = self.record.students.get(student_id)
        if not student:
            return []
        return self.plan.get_eligible_courses(student.approved_courses, student.enrolled_courses)
