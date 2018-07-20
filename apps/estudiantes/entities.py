from apps.common.constants import ESTUDIANTE_TIPO_CHOICES
from apps.common.utils import choices_to_dict


class Estudiante(object):

    def __init__(self, nombre, apellido_paterno, apellido_materno, tipo, id=None):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.tipo = tipo
        self.id = id

    def get_tipo_display(self):
        return choices_to_dict(ESTUDIANTE_TIPO_CHOICES)[self.tipo]
