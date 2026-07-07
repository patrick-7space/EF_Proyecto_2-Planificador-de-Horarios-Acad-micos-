# ==========================================================
# PROYECTO FINAL - PLANIFICADOR DE HORARIOS ACADÉMICOS
# Estrategias: Backtracking, Poda y Heurística Voraz
# ==========================================================

from dataclasses import dataclass

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

# ==========================================================
# PARTE 5 - UTILIDADES
# ==========================================================

def crear_datos_prueba():
    horarios = ["Lunes 8-10","Lunes 10-12","Martes 8-10","Martes 10-12"]

    docentes = [
        Docente("Juan",["Lunes 8-10","Martes 8-10"]),
        Docente("María",["Lunes 10-12","Martes 10-12"]),
        Docente("Pedro",horarios)
    ]

    cursos = [
        Curso("Matemática","Juan"),
        Curso("Programación","Pedro"),
        Curso("Base de Datos","María"),
        Curso("Física","Juan")
    ]

    aulas = [Aula("A101"), Aula("A102")]

    return cursos,aulas,horarios,docentes

def mostrar_horario(solucion):
    print("\nHORARIO GENERADO")
    print("-"*60)
    for a in solucion:
        print(f"{a.curso:18} {a.docente:10} {a.aula:6} {a.horario}")

def explicar():
    print("\nCOMPLEJIDAD")
    print("Sin poda: O((A*H)^C)")
    print("La poda elimina combinaciones inválidas antes de seguir buscando.")

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

# ==========================================================
# PARTE 1 - MAIN
# ==========================================================

def main():

    cursos,aulas,horarios,docentes=crear_datos_prueba()

    cursos=ordenar_cursos(cursos,docentes)

    solucion=[]

    if backtracking(0,cursos,aulas,horarios,docentes,solucion):
        mostrar_horario(solucion)
    else:
        print("No se encontró una solución válida.")

    explicar()

if __name__=="__main__":
    main()
