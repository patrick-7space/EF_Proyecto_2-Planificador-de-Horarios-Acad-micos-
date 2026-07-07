# ==========================================================
# PARTE 3 - ALGORITMO
# ==========================================================

def ordenar_cursos(cursos,docentes):
    return sorted(
        cursos,
        key=lambda c: len(next(d for d in docentes if d.nombre==c.docente).disponibilidad)
    )

def backtracking(indice,cursos,aulas,horarios,docentes,solucion):
    if indice==len(cursos):
        return True

    curso=cursos[indice]

    for aula in aulas:
        for horario in horarios:
            if es_valido(curso,aula,horario,solucion,docentes):
                solucion.append(Asignacion(curso.nombre,curso.docente,aula.nombre,horario))

                if backtracking(indice+1,cursos,aulas,horarios,docentes,solucion):
                    return True

                solucion.pop()

    return False