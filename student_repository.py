from models.student import Student


class StudentRepository:
    def __init__(self):
        self._students = [
            Student(1, "Juan Pérez", "Matemáticas", 95.0),
            Student(2, "Ana López", "Programación", 82.0),
            Student(3, "Luis Díaz", "Base de Datos", 65.0),
        ]

    def find_all(self):
        return self._students

    def create_one(self, student: Student):
        self._students.append(student)
