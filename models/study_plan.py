"""Modelo de plan de estudios."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Set
from models.course import Course


@dataclass
class StudyPlan:
    """Representa un plan de estudios completo."""

    plan_id: str
    name: str
    total_credits: int
    courses: Dict[str, Course] = field(default_factory=dict)

    def add_course(self, course: Course) -> None:
        self.courses[course.code] = course

    def get_course(self, code: str) -> Course | None:
        return self.courses.get(code)

    def get_courses_by_cycle(self, cycle: int) -> List[Course]:
        return sorted(
            [c for c in self.courses.values() if c.cycle == cycle],
            key=lambda c: c.code,
        )

    def get_all_cycles(self) -> List[int]:
        cycles = sorted(set(c.cycle for c in self.courses.values()))
        return cycles

    def get_eligible_courses(self, approved: Set[str], enrolled: Set[str]) -> List[Course]:
        """Retorna cursos para los que el estudiante cumple requisitos
        y que no ha aprobado ni tiene matriculado."""
        eligible = []
        for course in self.courses.values():
            if course.code in approved or course.code in enrolled:
                continue
            if course.prerequisites_met(approved | enrolled):
                eligible.append(course)
        return eligible

    @property
    def all_course_codes(self) -> Set[str]:
        return set(self.courses.keys())
