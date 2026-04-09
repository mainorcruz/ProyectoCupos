"""Modelo de estudiante y su expediente académico."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Set, List
from enum import Enum


PASSING_GRADE = 7.0


class CourseStatus(Enum):
    APPROVED = "Aprobado"
    ENROLLED = "Matriculado"
    FAILED = "Reprobado"
    WITHDRAWN = "Retirado"
    IN_PROGRESS = "En curso"


@dataclass
class CourseRecord:
    """Registro de un curso en el expediente de un estudiante."""

    code: str
    name: str
    credits: int
    grade: float | None
    status: CourseStatus
    modality: str
    period: str
    year: str
    group: str
    belongs_to_plan: str


@dataclass
class Student:
    """Representa un estudiante con su expediente."""

    student_id: str  # Carné
    first_name: str
    last_name_1: str
    last_name_2: str
    campus: str = ""
    records: List[CourseRecord] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return f"{self.last_name_1} {self.last_name_2} {self.first_name}"

    def add_record(self, record: CourseRecord) -> None:
        self.records.append(record)

    @property
    def approved_courses(self) -> Set[str]:
        return {r.code for r in self.records if r.status == CourseStatus.APPROVED}

    @property
    def enrolled_courses(self) -> Set[str]:
        return {r.code for r in self.records if r.status == CourseStatus.ENROLLED}

    @property
    def enrolled_records(self) -> List[CourseRecord]:
        return [r for r in self.records if r.status == CourseStatus.ENROLLED]

    @property
    def failed_courses(self) -> Set[str]:
        return {r.code for r in self.records if r.status == CourseStatus.FAILED}

    def has_approved(self, code: str) -> bool:
        return code in self.approved_courses

    def is_enrolled(self, code: str) -> bool:
        return code in self.enrolled_courses


@dataclass
class AcademicRecord:
    """Contenedor del expediente académico global."""

    students: Dict[str, Student] = field(default_factory=dict)

    def get_or_create_student(
        self, student_id: str, first_name: str, last_name_1: str,
        last_name_2: str, campus: str = ""
    ) -> Student:
        if student_id not in self.students:
            self.students[student_id] = Student(
                student_id=student_id,
                first_name=first_name,
                last_name_1=last_name_1,
                last_name_2=last_name_2,
                campus=campus,
            )
        return self.students[student_id]

    @property
    def student_count(self) -> int:
        return len(self.students)


def determine_status(grade_value: float | None, modality: str) -> CourseStatus:
    """Determina el estado de un curso según la nota y modalidad.

    Convenciones UCR:
        - Nota >= 7.0 -> Aprobado
        - 'RJ' / 'RET' en modalidad -> Retirado
        - 'PI' -> En curso / Matriculado
        - Nota < 7.0 -> Reprobado
    """
    mod_upper = (modality or "").strip().upper()

    if mod_upper in ("RJ", "RET", "RETIRADO", "RETIRO JUSTIFICADO"):
        return CourseStatus.WITHDRAWN
    if mod_upper in ("PI", "MATRICULADO", "EN CURSO"):
        return CourseStatus.ENROLLED

    if grade_value is None:
        return CourseStatus.ENROLLED

    if grade_value >= PASSING_GRADE:
        return CourseStatus.APPROVED
    return CourseStatus.FAILED
