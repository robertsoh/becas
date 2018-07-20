from apps.estudiantes.interactors import CreateEstudianteInteractor, GetAllEstudiantesInteractor
from apps.estudiantes.repository_factories import create_estudiante_repository


def create_create_estudiante_interactor():
    return CreateEstudianteInteractor(estudiante_repository=create_estudiante_repository())


def create_get_all_estudiantes_interactor():
    return GetAllEstudiantesInteractor(estudiante_repository=create_estudiante_repository())