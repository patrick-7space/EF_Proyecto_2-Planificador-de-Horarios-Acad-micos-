class Docente:
    def __init__(self, nombre, disponibilidad):
        self.nombre = nombre
        self.disponibilidad = disponibilidad


class Curso:
    def __init__(self, nombre, docente):
        self.nombre = nombre
        self.docente = docente


class Aula:
    def __init__(self, codigo, capacidad):
        self.codigo = codigo
        self.capacidad = capacidad


class Horario:
    def __init__(self, dia, hora):
        self.dia = dia
        self.hora = hora


class Asignacion:
    def __init__(self, curso, docente, aula, horario):
        self.curso = curso
        self.docente = docente
        self.aula = aula
        self.horario = horario