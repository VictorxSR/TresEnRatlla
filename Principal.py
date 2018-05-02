import random 
import os 
import time
import random
 
 
tauler=[" "," "," ",
         " "," "," ",
         " "," "," " ]
 

def jugar():
    
    guanyador = 0

    while True:

        #os.system("clear")


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


        jugadaMaquina()
        mostrarTauler()
        guanyador = comprovarTauler()
       
        print("Guanyador" + str(guanyador))

        if guanyador == 2:
            os.system("clear")
            mostrarTauler()
            print("La màquina GUANYA")
            break

        

def jugadaMaquina():

    while True:
        posicio = random.randrange(8)

        if tauler[0] == 'X':
            print("0")
            if tauler[1] == 'X' and tauler[2] == " ":
                print("0.1")
                tauler[2] = 'O'
                break
            if tauler[3] == 'X' and tauler[6] == " ":
                print("0.3")
                tauler[6] = 'O'
                break
            if tauler[4] == 'X' and tauler[8] == " ":
                print("0.4")
                tauler[8] = 'O'
                break

            if tauler[2] == 'X' and tauler[1] == " ":
                tauler[1] = 'O'
            

        if tauler[4] == 'X':
            print("4")
            if tauler[3] == 'X'and tauler[5] == " ":
                print("4.3")
                tauler[5] = 'O'
                break
            if tauler[1] == 'X' and tauler[7] == " ":
                print("4.1")
                tauler[7] = 'O'
                break
            if tauler[2] == 'X' and tauler[6] == " ":
                print("4.2")
                tauler[6] = 'O'
                break

        if tauler[3] == 'X':
             if tauler[5] == 'X' and tauler[4] == " ":
                 tauler[4] = 'O'
                 break

        if tauler[8] == 'X':
            print("8")
            if tauler[7] == 'X' and tauler[6] == " ":
                print("8.7")
                tauler[6] = 'O'
                break
            if tauler[5] == 'X' and tauler[2] == " ":
                print("8.5")
                tauler[2] = 'O'
                break
            if tauler[6] =='X' and tauler[7] == " ":
                tauler[7] = 'O'
                break
            
     
        if tauler[posicio] != 'X' and tauler[posicio] != 'O':
            print("elif")
            tauler[posicio] = 'O'
            break
    
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

    print("Casilles " + str(tauler.count(" ")))

    

    #Jugador
    if tauler[0] == 'X':
        if tauler[1] == 'X' and tauler[2] == 'X':
            return 1
        if tauler[3] == 'X' and tauler[6] == 'X':
            return 1
        if tauler[4] == 'X' and tauler[8] == 'X':
            return 1

    elif tauler[4] == 'X':
        if tauler[3] == 'X' and tauler[5] == 'X':
            return 1
        if tauler[1] == 'X' and tauler[7] == 'X':
            return 1
        if tauler[2] == 'X' and tauler[6] == 'X':
            return 1
    
    elif tauler[8] == 'X':
        if tauler[7] == 'X' and tauler[6] == 'X':
            return 1
        if tauler[5] == 'X' and tauler[2] == 'X':
            return 1

    else:
        return 0
    #Maquina
    if tauler[0] == 'O':
        if tauler[1] == 'O' and tauler[2] == 'O':
            return 2
        if tauler[3] == 'O' and tauler[6] == 'O':
            return 2
        if tauler[4] == 'O' and tauler[8] == 'O':
            return 2

    elif tauler[4] == 'O':
        if tauler[3] == 'O' and tauler[5] == 'O':
            return 2
        if tauler[1] == 'O' and tauler[7] == 'O':
            return 2
        if tauler[2] == 'O' and tauler[6] == 'O':
            return 2
    
    elif tauler[8] == 'O':
        if tauler[7] == 'O' and tauler[6] == 'O':
            return 2
        if tauler[5] == 'O' and tauler[2] == 'O':
            return 2


    if tauler.count(" ") == 0:
        return 3 #Empat

    else:
        return 0

jugar()

