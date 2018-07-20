from apps.common.decorators import serialize_exceptions
from apps.common.paginators import CustomPagination
from apps.estudiantes.api_v1.serializers import EstudianteSerialize, EstudiantesSerialize


class EstudianteListCreateView:
    def __init__(self,
             create_estudiante_interactor=None,
             get_all_estudiantes_interactor=None):
        self.create_estudiante_interactor = create_estudiante_interactor
        self.get_all_estudiantes_interactor = get_all_estudiantes_interactor

    @serialize_exceptions
    def post(self, data):
        customer = self.create_estudiante_interactor.set_params(
            nombre=data.get('nombre'),
            apellido_paterno=data.get('apellido_paterno'),
            apellido_materno=data.get('apellido_materno'),
            tipo=data.get('tipo'),
        ).execute()
        body = EstudianteSerialize.serialize(customer)
        status = 201
        return body, status

    @serialize_exceptions
    def get(self, page_size=None, page=None):
        """
        :param page_size: El tamaño de la paginación
        :param page: Número de página que desea consultar
        :return: asdasd
        """
        custom_pagination = CustomPagination(page_size=page_size, page=page)
        cleaned_data = custom_pagination.cleaned_data()
        estudiantes, pagination_data = self.get_all_estudiantes_interactor.set_params(
            page_size=cleaned_data.get('page_size'),
            page=cleaned_data.get('page')
        ).execute()
        body = custom_pagination.set_params(queryset=EstudiantesSerialize.serialize(estudiantes),
                                            count=pagination_data.get('count'),
                                            page_range=pagination_data.get('page_range')
                                            ).paginate_queryset()
        status = 200
        return body, status