from apps.common.decorators import serialize_exceptions
from apps.estudiantes.api_v1.serializers import EstudianteSerialize


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