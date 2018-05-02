import numpy as np 
import random as rd 
from random import shuffle 

#Funcion que retorna la lista de opciones de lo que hay en las puestas desordenada aleatoriamente 
def sort_doors():
	lista = ['goat','goat','car']
	shuffle(lista)
	return lista 

#Funcion que simula la eleccion del participante 
def choose_door():
	return np.random.choice(3,1)[0]

#Funcion que simula que el presentador le muestra una puerta donde hay un cabra 	
def reveal_door(lista, choice):
	for i in range(len(lista)):
		if((i != choice) and (lista[i] == 'goat')):
			lista [i] = 'GOAT_MONTY'
 			return lista

#Funcion que revela las puertas segun la decision del usuario de cambiar o no su primera eleccion 

def finish_game(lista,choice,change):
	if(change == False):
		return lista[choice]
	if(change == True):
		for i in range(len(lista)):
			if((lista[i] != 'GOAT_MONTY') and (i != choice)):
				return lista[i]

#lista donde se guardan los resultados con choice igual a true
listtrue=[]

#lista donde se guardan los resultados con choice igual a false
listfalse=[]

#Ciclo que hace 100 veces el juego con true 
for i in range(100):
	listy = sort_doors()
	n = choose_door()
	rta = reveal_door(listy, n)
	rta2 = finish_game(rta, n, True)
	listtrue.append(rta2)
	

#Ciclo que hace 100 veces el juego con false
for i in range(100):
	listy2 = sort_doors()
	n2 = choose_door()
	rta2 = reveal_door(listy2,n2)
	rta4 = finish_game(rta2,n2,False)
	listfalse.append(rta4)

cganotrue = 0	
cganofalse = 0

#Ciclo que cuenta cuantaa veces gano con true
for i in range(100):
	if (listtrue[i] == 'car'):
		cganotrue = cganotrue+1

#Ciclo que cuenta cuantaa veces gano con false
for i in range(100):
	if (listfalse[i] == 'car'):
		cganofalse = cganofalse+1
		
print "la probabilidad de ganar con cambio de puerta es:",cganotrue,"la probabilidad de ganar sin cambio de puerta es:", cganofalse
