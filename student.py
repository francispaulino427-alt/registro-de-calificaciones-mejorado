from dataclasses import dataclass


@dataclass
class Student:
    id: int
    nombre: str
    asignatura: str
    calificacion: float

    @property
    def estado(self) -> str:
        return "Aprobado" if self.calificacion >= 70 else "Reprobado"
