# ============================================================
# Módulo: backtracking.py
# Algoritmo de generación de horarios mediante Backtracking
# con poda (restricciones verificadas en cada paso).
#
# Se apoya en las clases definidas en modelos.py:
#   Docente, Curso, Aula, Horario, Asignacion
# ============================================================

from modelos import Asignacion


def _docente_ocupado(docente, horario, asignaciones):
    """R2: True si el docente ya tiene una clase en ese horario."""
    for asignacion in asignaciones:
        if asignacion.docente is docente and \
           asignacion.horario.dia == horario.dia and \
           asignacion.horario.hora == horario.hora:
            return True
    return False


def _aula_ocupada(aula, horario, asignaciones):
    """R3: True si el aula ya está ocupada en ese horario."""
    for asignacion in asignaciones:
        if asignacion.aula is aula and \
           asignacion.horario.dia == horario.dia and \
           asignacion.horario.hora == horario.hora:
            return True
    return False


def _capacidad_suficiente(aula, curso):
    """
    R4 (opcional): si el curso trae el atributo 'num_estudiantes',
    se exige que el aula tenga capacidad suficiente.
    Si el curso no define ese atributo, la restricción no aplica.
    """
    num_estudiantes = getattr(curso, "num_estudiantes", None)
    if num_estudiantes is None:
        return True
    return aula.capacidad >= num_estudiantes


def _horario_disponible_para_docente(docente, horario):
    """
    R1: el horario debe estar dentro de docente.disponibilidad.
    Se admite que 'disponibilidad' sea una lista de tuplas (dia, hora)
    o una lista de objetos Horario.
    """
    for disp in docente.disponibilidad:
        if hasattr(disp, "dia") and hasattr(disp, "hora"):
            if disp.dia == horario.dia and disp.hora == horario.hora:
                return True
        else:
            # Se asume tupla (dia, hora)
            if disp == (horario.dia, horario.hora):
                return True
    return False


def _backtrack(cursos, indice, aulas, horarios, asignaciones):
    # Caso base: ya se asignaron todos los cursos
    if indice == len(cursos):
        return True

    curso = cursos[indice]
    docente = curso.docente

    for horario in horarios:

        # --- Poda 1: disponibilidad del docente ---
        if not _horario_disponible_para_docente(docente, horario):
            continue

        # --- Poda 2: choque de docente ---
        if _docente_ocupado(docente, horario, asignaciones):
            continue

        for aula in aulas:

            # --- Poda 3: choque de aula ---
            if _aula_ocupada(aula, horario, asignaciones):
                continue

            # --- Poda 4: capacidad del aula ---
            if not _capacidad_suficiente(aula, curso):
                continue

            # Se prueba la asignación (curso, docente, aula, horario)
            asignaciones.append(Asignacion(curso, docente, aula, horario))

            if _backtrack(cursos, indice + 1, aulas, horarios, asignaciones):
                return True

            # No funcionó más adelante -> se deshace (backtrack real)
            asignaciones.pop()

    # Ningún (horario, aula) sirvió para este curso
    return False


def generar_horario(cursos, aulas, horarios):
    """
    Punto de entrada del algoritmo.

    Parámetros:
        cursos:   lista de objetos Curso (cada uno ya tiene su Docente)
        aulas:    lista de objetos Aula
        horarios: lista de objetos Horario candidatos

    Retorna:
        Lista de objetos Asignacion si se encontró una solución válida,
        o None si no existe ninguna combinación que satisfaga
        todas las restricciones.
    """
    asignaciones = []
    encontrado = _backtrack(cursos, 0, aulas, horarios, asignaciones)
    return asignaciones if encontrado else None


def imprimir_horario(asignaciones):
    """Muestra el horario generado en formato de tabla simple."""
    if not asignaciones:
        print("No se encontró un horario válido con las restricciones dadas.")
        return

    print(f"{'CURSO':<20}{'DOCENTE':<20}{'AULA':<10}{'DÍA':<12}{'HORA':<10}")
    print("-" * 72)
    for a in asignaciones:
        print(f"{a.curso.nombre:<20}{a.docente.nombre:<20}"
              f"{a.aula.codigo:<10}{a.horario.dia:<12}{a.horario.hora:<10}")
