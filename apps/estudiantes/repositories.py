from apps.estudiantes.entities import Estudiante
from apps.estudiantes.models import ORMEstudiante


class EstudianteRepository:

    def _decode_db_estudiante(self, estudiante):
        return Estudiante(id=estudiante.id,
                          nombre=estudiante.nombre,
                          apellido_paterno=estudiante.apellido_paterno,
                          apellido_materno=estudiante.apellido_materno,
                          tipo=estudiante.tipo)

    def create(self, estudiante):
        db_estudiante = ORMEstudiante.objects.create(nombre=estudiante.nombre,
                                                  apellido_paterno=estudiante.apellido_paterno,
                                                  apellido_materno=estudiante.apellido_materno,
                                                  tipo=estudiante.tipo)
        return self._decode_db_estudiante(db_estudiante)
