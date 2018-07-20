from apps.estudiantes.api_v1.views import EstudianteListCreateView
from apps.estudiantes.interactor_factories import create_create_estudiante_interactor


def create_estudiante_list_create_view(request, **kwargs):
    return EstudianteListCreateView(
        create_estudiante_interactor=create_create_estudiante_interactor(),
    )
