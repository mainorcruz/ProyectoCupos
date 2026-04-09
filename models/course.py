"""Modelo de curso dentro de un plan de estudios."""

from dataclasses import dataclass, field
from typing import List, Set


@dataclass
class Course:
    """Representa un curso del plan de estudios."""

    code: str
    name: str
    credits: int
    cycle: int
    prerequisites: List[str] = field(default_factory=list)
    corequisites: List[str] = field(default_factory=list)
    # Cada elemento en equivalents mapea código original -> código equivalente
    # Si un requisito tiene equivalente, el estudiante puede cumplir con cualquiera
    prerequisite_equivalents: dict = field(default_factory=dict)

    def prerequisites_met(self, approved_courses: Set[str]) -> bool:
        """Verifica si un estudiante cumple los requisitos del curso.

        Args:
            approved_courses: Conjunto de siglas de cursos aprobados.

        Returns:
            True si todos los requisitos están cumplidos.
        """
        for prereq in self.prerequisites:
            equiv = self.prerequisite_equivalents.get(prereq)
            if prereq in approved_courses:
                continue
            if equiv and equiv in approved_courses:
                continue
            return False
        return True

    @property
    def display_name(self) -> str:
        return f"{self.code} - {self.name}"
