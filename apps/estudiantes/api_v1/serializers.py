

class EstudianteSerialize:

    @staticmethod
    def serialize(estudiante):
        data = {
            'id': estudiante.id,
            'nombre': estudiante.nombre,
            'apellido_paterno': estudiante.apellido_paterno,
            'apellido_materno': estudiante.apellido_materno,
            'tipo': estudiante.get_tipo_display()
        }
        return data


class EstudiantesSerialize:

    @staticmethod
    def serialize(estudiantes):
        return [EstudianteSerialize.serialize(estudiante) for estudiante in estudiantes]