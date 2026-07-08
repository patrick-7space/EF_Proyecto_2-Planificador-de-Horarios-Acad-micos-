Algoritmo Horarios
	
	Definir n, i, j Como Entero
	Dimension horario[10]
	Dimension usado[10]
	
	Escribir "Cantidad de cursos (maximo 5):"
	Leer n
	
	Para i <- 1 Hasta 5 Hacer
		usado[i] <- 0
	FinPara
	
	Para i <- 1 Hasta n Hacer
		
		Para j <- 1 Hasta 5 Hacer
			
			Si usado[j] = 0 Entonces
				
				horario[i] <- j
				usado[j] <- 1
				
				j <- 5
				
			FinSi
			
		FinPara
		
	FinPara
	
	Escribir ""
	Escribir "HORARIO GENERADO"
	
	Para i <- 1 Hasta n Hacer
		Escribir "Curso ", i, " -> Horario ", horario[i]
	FinPara
	
FinAlgoritmo