# ==========================================================
# PARTE 4 - VALIDACIONES
# ==========================================================

def es_valido(curso,aula,horario,solucion,docentes):
    docente = next(d for d in docentes if d.nombre==curso.docente)

    if horario not in docente.disponibilidad:
        return False

    for a in solucion:
        if a.docente==curso.docente and a.horario==horario:
            return False
        if a.aula==aula.nombre and a.horario==horario:
            return False
        if a.curso==curso.nombre:
            return False
    return True
