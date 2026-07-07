# ============================================================
# Módulo: validaciones.py
# Funciones de validación para el Planificador de Horarios
# Persona 4
# ============================================================


def docente_disponible(docente, horario):
    """
    Verifica si el docente tiene disponible el horario indicado.
    La disponibilidad puede almacenarse como:
    - Lista de objetos Horario.
    - Lista de tuplas (día, hora).
    """

    for disp in docente.disponibilidad:

        if hasattr(disp, "dia") and hasattr(disp, "hora"):

            if disp.dia == horario.dia and disp.hora == horario.hora:
                return True

        else:

            if disp == (horario.dia, horario.hora):
                return True

    return False


def conflicto_docente(docente, horario, asignaciones):
    """
    Verifica si el docente ya fue asignado
    al mismo horario.
    """

    for asignacion in asignaciones:

        if (
            asignacion.docente == docente
            and asignacion.horario.dia == horario.dia
            and asignacion.horario.hora == horario.hora
        ):
            return True

    return False


def conflicto_aula(aula, horario, asignaciones):
    """
    Verifica si el aula ya está ocupada
    en el mismo horario.
    """

    for asignacion in asignaciones:

        if (
            asignacion.aula == aula
            and asignacion.horario.dia == horario.dia
            and asignacion.horario.hora == horario.hora
        ):
            return True

    return False


def capacidad_valida(aula, curso):
    """
    Comprueba si el aula tiene capacidad suficiente.
    Si el curso no posee el atributo
    'num_estudiantes', la validación se omite.
    """

    if hasattr(curso, "num_estudiantes"):

        return aula.capacidad >= curso.num_estudiantes

    return True


def validar_asignacion(curso, aula, horario, asignaciones):
    """
    Ejecuta todas las validaciones antes
    de realizar una asignación.
    """

    docente = curso.docente

    if not docente_disponible(docente, horario):
        return False, "El docente no se encuentra disponible."

    if conflicto_docente(docente, horario, asignaciones):
        return False, "Conflicto: el docente ya tiene una clase."

    if conflicto_aula(aula, horario, asignaciones):
        return False, "Conflicto: el aula ya está ocupada."

    if not capacidad_valida(aula, curso):
        return False, "El aula no posee capacidad suficiente."

    return True, "Asignación válida."


def reporte_conflictos(curso, aula, horario, asignaciones):
    """
    Devuelve una lista con todos los conflictos
    encontrados para una posible asignación.
    """

    conflictos = []

    docente = curso.docente

    if not docente_disponible(docente, horario):
        conflictos.append("Docente no disponible.")

    if conflicto_docente(docente, horario, asignaciones):
        conflictos.append("Docente ocupado en ese horario.")

    if conflicto_aula(aula, horario, asignaciones):
        conflictos.append("Aula ocupada.")

    if not capacidad_valida(aula, curso):
        conflictos.append("Capacidad del aula insuficiente.")

    if len(conflictos) == 0:
        conflictos.append("No existen conflictos.")

    return conflictos


def mostrar_conflictos(conflictos):
    """
    Muestra en pantalla los conflictos encontrados.
    """

    print("\n========== REPORTE DE CONFLICTOS ==========\n")

    for conflicto in conflictos:
        print("- " + conflicto)

    print()