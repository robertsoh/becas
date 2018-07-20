from django.conf.urls import url

from apps.common.views import ViewWrapper
from apps.estudiantes.view_factories import create_estudiante_list_create_view

urlpatterns = [
    url(r'^estudiantes$',
        ViewWrapper.as_view(view_creator_func=create_estudiante_list_create_view),
        name='estudiantes'),
]