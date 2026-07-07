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
