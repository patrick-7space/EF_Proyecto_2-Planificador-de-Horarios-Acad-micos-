# ==========================================================
# PARTE 2 - MODELOS
# ==========================================================

@dataclass
class Docente:
    nombre: str
    disponibilidad: list

@dataclass
class Curso:
    nombre: str
    docente: str

@dataclass
class Aula:
    nombre: str

@dataclass
class Asignacion:
    curso: str
    docente: str
    aula: str
    horario: str
