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
