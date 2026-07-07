# ============================================================
# PROYECTO FINAL
# Planificador de Horarios Académicos
# Curso: Análisis de Algoritmos y Estrategias de Programación
# Autor: Persona 1
# Archivo: main.py
# ============================================================

import os


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def pausa():
    input("\nPresione ENTER para continuar...")


def mostrar_menu():
    print("=" * 60)
    print("     PLANIFICADOR DE HORARIOS ACADÉMICOS")
    print("=" * 60)
    print("1. Registrar docentes")
    print("2. Registrar cursos")
    print("3. Registrar aulas")
    print("4. Registrar horarios")
    print("5. Generar horario (Backtracking)")
    print("6. Mostrar horario generado")
    print("7. Reporte de conflictos")
    print("8. Acerca del proyecto")
    print("0. Salir")
    print("=" * 60)


def registrar_docentes():
    print("\n[ MÓDULO REGISTRAR DOCENTES ]")
    print("Este módulo será desarrollado por otro integrante.")
    pausa()


def registrar_cursos():
    print("\n[ MÓDULO REGISTRAR CURSOS ]")
    print("Este módulo será desarrollado por otro integrante.")
    pausa()


def registrar_aulas():
    print("\n[ MÓDULO REGISTRAR AULAS ]")
    print("Este módulo será desarrollado por otro integrante.")
    pausa()


def registrar_horarios():
    print("\n[ MÓDULO REGISTRAR HORARIOS ]")
    print("Este módulo será desarrollado por otro integrante.")
    pausa()


def generar_horario():
    print("\n[ GENERAR HORARIO ]")
    print("Aquí se ejecutará el algoritmo Backtracking con poda.")
    pausa()


def mostrar_horario():
    print("\n[ HORARIO GENERADO ]")
    print("Aquí se mostrará el horario final.")
    pausa()


def reporte_conflictos():
    print("\n[ REPORTE DE CONFLICTOS ]")
    print("Aquí se mostrarán los conflictos detectados.")
    pausa()


def acerca_proyecto():
    print("\nPLANIFICADOR DE HORARIOS ACADÉMICOS")
    print("--------------------------------------")
    print("Proyecto Final")
    print("Curso: Análisis de Algoritmos y Estrategias de Programación")
    print("Lenguaje: Python")
    print("Estrategia utilizada:")
    print("Backtracking con poda y heurísticas voraces.")
    print("\nEl sistema busca generar horarios válidos")
    print("evitando conflictos entre cursos, docentes")
    print("aulas y horarios disponibles.")
    pausa()


def main():

    while True:

        limpiar()
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_docentes()

        elif opcion == "2":
            registrar_cursos()

        elif opcion == "3":
            registrar_aulas()

        elif opcion == "4":
            registrar_horarios()

        elif opcion == "5":
            generar_horario()

        elif opcion == "6":
            mostrar_horario()

        elif opcion == "7":
            reporte_conflictos()

        elif opcion == "8":
            acerca_proyecto()

        elif opcion == "0":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción inválida.")
            pausa()


if __name__ == "__main__":
    main()