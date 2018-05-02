import random 
import os 
import time
import random
from Maquina import *
 
 
tauler=[" "," "," ",
         " "," "," ",
         " "," "," " ]
 

def jugar():
    
    guanyador = 0
    global tauler

    while True:

        os.system("clear")


        demanarPosicio()
        guanyador = comprovarTauler()

        if guanyador == 1:
            os.system("clear")
            mostrarTauler()
            print("El jugador GUANYA")
            break

        if guanyador == 3:
            os.system("clear")
            mostrarTauler()
            print("Empat")
            break

        tauler = Maquina.jugadaMaquina(tauler)
        mostrarTauler()
        guanyador = comprovarTauler()
       
        print("Guanyador" + str(guanyador))

        if guanyador == 2:
            os.system("clear")
            mostrarTauler()
            print("La màquina GUANYA")
            break

        #tauler = Maquina.jugadaMaquina(tauler)

    
        mostrarTauler()


def demanarPosicio():
    while True:
        
        mostrarTauler()
        posicio = int(input("=>"))

        if posicio >= 0 and posicio <= 8:
            if tauler[posicio] != 'X' and tauler[posicio] != 'O':
                tauler[posicio] = 'X'
                break
            else:
                print("\nAquesta posició està ocupada\n")
                time.sleep(1)
        else:
            print("\nHas d'introduir una posicio correcta\n")
            time.sleep(1)


def mostrarTauler():
    print( "-"*13)
    print( "|",tauler[0],"|",tauler[1],"|",tauler[2],"|")
    print( "-"*13)
    print( "|",tauler[3],"|",tauler[4],"|",tauler[5],"|")
    print( "-"*13)
    print( "|",tauler[6],"|",tauler[7],"|",tauler[8],"|")
    print( "-"*13)


def comprovarTauler():


    #Jugador
    if tauler[0] == 'X':
        if tauler[1] == 'X' and tauler[2] == 'X':
            return 1
        if tauler[3] == 'X' and tauler[6] == 'X':
            return 1
        if tauler[4] == 'X' and tauler[8] == 'X':
            return 1


    if tauler[4] == 'X':
        if tauler[3] == 'X' and tauler[5] == 'X':
            return 1
        if tauler[1] == 'X' and tauler[7] == 'X':
            return 1
        if tauler[2] == 'X' and tauler[6] == 'X':
            return 1
    
    if tauler[8] == 'X':
        if tauler[7] == 'X' and tauler[6] == 'X':
            return 1
        if tauler[5] == 'X' and tauler[2] == 'X':
            return 1


    #Maquina
    if tauler[0] == 'O':
        if tauler[1] == 'O' and tauler[2] == 'O':
            return 2
        if tauler[3] == 'O' and tauler[6] == 'O':
            return 2
        if tauler[4] == 'O' and tauler[8] == 'O':
            return 2

    if tauler[4] == 'O':
        if tauler[3] == 'O' and tauler[5] == 'O':
            return 2
        if tauler[1] == 'O' and tauler[7] == 'O':
            return 2
        if tauler[2] == 'O' and tauler[6] == 'O':
            return 2
    
    if tauler[8] == 'O':
        if tauler[7] == 'O' and tauler[6] == 'O':
            return 2
        if tauler[5] == 'O' and tauler[2] == 'O':
            return 2


    if tauler.count(" ") == 0:
        return 3 #Empat

    else:
        return 0

jugar()

