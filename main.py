import sys
import os

# Agrega la carpeta actual a la ruta de búsqueda de módulos de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from repositories.student_repository import StudentRepository
from services.student_service import StudentService
from ui.app_window import AppWindow


def main():
    repository = StudentRepository()
    service = StudentService(repository)
    app = AppWindow(service)
    app.mainloop()


if __name__ == "__main__":
    main()