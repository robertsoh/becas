from django.core.paginator import Paginator

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

    def get_all_estudiantes(self, page_size, page):
        queryset = ORMEstudiante.objects.order_by('apellido_paterno', 'apellido_materno', 'nombre')
        paginator = Paginator(queryset, page_size)
        try:
            queryset = paginator.page(page)
        except Exception:
            queryset = paginator.page(paginator.num_pages)
        estudiantes = []
        for estudiante in queryset:
            estudiantes.append(self._decode_db_estudiante(estudiante))
        pagination_data = {
            'count': paginator.count,
            'page_range': list(paginator.page_range),
            'num_pages': paginator.num_pages,
            'per_page': paginator.per_page,
            'page': page
        }
        return estudiantes, pagination_data