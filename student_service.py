from models.student import Student

from repositories.student_repository import StudentRepository


class StudentService:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def find_all(self):
        return self.repository.find_all()

    def create_one(self, id, nombre, asignatura, calificacion):
        student = Student(int(id), nombre, asignatura, float(calificacion))
        self.repository.create_one(student)
