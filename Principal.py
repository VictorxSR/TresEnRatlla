import random 
import os 
 
os.system("clear")
 
tauler=[" "," "," ",
         " "," "," ",
         " "," "," " ]
 
 

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
            return "jugador"
        if tauler[3] == 'X' and tauler[6] == 'X':
            return "jugador"
        if tauler[4] == 'X' and tauler[8] == 'X':
            return "jugador"

    elif tauler[4] == 'X':
        if tauler[3] == 'X' and tauler[5] == 'X':
            return "jugador"
        if tauler[1] == 'X' and tauler[7] == 'X':
            return "jugador"
        if tauler[2] == 'X' and tauler[6] == 'X':
            return "jugador"
    
    elif tauler[8] == 'X':
        if tauler[7] == 'X' and tauler[6] == 'X':
            return "jugador"
        if tauler[5] == 'X' and tauler[2] == 'X':
            return "jugador"

    #Maquina
    if tauler[0] == 'O':
        if tauler[1] == 'O' and tauler[2] == 'O':
            return "jugador"
        if tauler[3] == 'O' and tauler[6] == 'O':
            return "jugador"
        if tauler[4] == 'O' and tauler[8] == 'O':
            return "jugador"

    elif tauler[4] == 'O':
        if tauler[3] == 'O' and tauler[5] == 'O':
            return "jugador"
        if tauler[1] == 'O' and tauler[7] == 'O':
            return "jugador"
        if tauler[2] == 'O' and tauler[6] == 'O':
            return "jugador"
    
    elif tauler[8] == 'O':
        if tauler[7] == 'O' and tauler[6] == 'O':
            return "jugador"
        if tauler[5] == 'O' and tauler[2] == 'O':
            return "jugador"

mostrarTauler()

