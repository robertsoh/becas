from apps.estudiantes.entities import Estudiante


class CreateEstudianteInteractor:

    def __init__(self, estudiante_repository):
        self.estudiante_repository = estudiante_repository

    def set_params(self, nombre, apellido_paterno, apellido_materno, tipo):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.tipo = tipo
        return self

    def execute(self):
        estudiante = Estudiante(nombre=self.nombre,
                                apellido_paterno=self.apellido_paterno,
                                apellido_materno=self.apellido_materno,
                                tipo=self.tipo)
        return self.estudiante_repository.create(estudiante)


class GetAllEstudiantesInteractor:

    def __init__(self, estudiante_repository):
        self.estudiante_repository = estudiante_repository

    def set_params(self, page_size, page):
        self.page_size = page_size
        self.page = page
        return self

    def execute(self):
        return self.estudiante_repository.get_all_estudiantes(page_size=self.page_size, page=self.page)