import random
class Maquina:

    def jugadaMaquina(tauler):

        while True:
        
            #Maquina pensa guanyar
            if tauler[0] == 'O':
                print("0")
                if tauler[1] == 'O' and tauler[2] == " ":
                    print("0.1")
                    tauler[2] = 'O'
                    break
                if tauler[3] == 'O' and tauler[6] == " ":
                    print("0.3")
                    tauler[6] = 'O'
                    break
                if tauler[4] == 'O' and tauler[8] == " ":
                    print("0.4")
                    tauler[8] = 'O'
                    break
                if tauler[6] == 'O' and tauler[3] == " ":
                    tauler[3] = 'O'
                    break

                if tauler[2] == 'O' and tauler[1] == " ":
                    tauler[1] = 'O'
                    break

            if tauler[1] == 'O':
                if tauler[7] == 'O' and tauler[4] == " ":
                    tauler[4] = 'O'
                    break

            if tauler[2] == 'O':
                if tauler[5] == 'O' and tauler[8] == " ":
                    tauler[8] = 'O'
                    break

            if tauler[4] == 'O':
                print("4")
                if tauler[3] == 'O'and tauler[5] == " ":
                    print("4.3")
                    tauler[5] = 'O'
                    break
                if tauler[1] == 'O' and tauler[7] == " ":
                    print("4.1")
                    tauler[7] = 'O'
                    break
                if tauler[2] == 'O' and tauler[6] == " ":
                    print("4.2")
                    tauler[6] = 'O'
                    break
                if tauler[8] == 'O' and tauler[0] == " ":
                    tauler[0] = 'O'
                    break
                if tauler[6] == 'O' and tauler[2] == " ":
                    tauler[2] = 'O'
                    break
                if tauler[7] == "O" and tauler[1] == " ":
                    tauler[1] == "O"
                    break
                if tauler[5] == 'O' and tauler[3] == " ":
                    tauler[3] = 'O'
                    break
    
            if tauler[3] == 'O':
                if tauler[5] == 'O' and tauler[4] == " ":
                    tauler[4] = 'O'
                    break

            if tauler[6] == 'O':
                if tauler[2] == 'O' and tauler[4] == " ":
                    tauler[4] = 'O'
                    break

            if tauler[8] == 'O':
                print("8")
                if tauler[7] == 'O' and tauler[6] == " ":
                    print("8.7")
                    tauler[6] = 'O'
                    break
                if tauler[5] == 'O' and tauler[2] == " ":
                    print("8.5")
                    tauler[2] = 'O'
                    break
                if tauler[6] =='O' and tauler[7] == " ":
                    tauler[7] = 'O'
                    break
                if tauler[0] == 'O' and tauler[4] == " ":
                    tauler[4] = 'O'
                    break 
                if tauler[2] == 'O' and tauler[5] == " ":
                    tauler[5] = 'O'
                    break


            #Maquina pensa no perdre
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
                if tauler[6] == 'X' and tauler[3] == " ":
                    tauler[3] = 'O'
                    break

                if tauler[2] == 'X' and tauler[1] == " ":
                    tauler[1] = 'O'
                    break

            if tauler[1] == 'X':
                if tauler[7] == 'X' and tauler[4] == " ":
                    tauler[4] = 'O'
                    break

            if tauler[2] == 'X':
                if tauler[5] == 'X' and tauler[8] == " ":
                    tauler[8] = 'O'
                    break

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
                if tauler[8] == 'X' and tauler[0] == " ":
                    tauler[0] = 'O'
                    break
                if tauler[6] == 'X' and tauler[2] == " ":
                    tauler[2] = 'O'
                    break
                if tauler[7] == "X" and tauler[1] == " ":
                    tauler[1] == "O"
                    break
                if tauler[5] == 'X' and tauler[3] == " ":
                    tauler[3] = 'O'
                    break
    
            if tauler[3] == 'X':
                if tauler[5] == 'X' and tauler[4] == " ":
                    tauler[4] = 'O'
                    break

            if tauler[6] == 'X':
                if tauler[2] == 'X' and tauler[4] == " ":
                    tauler[4] = 'O'
                    break

            if tauler[8] == 'O':
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
                if tauler[0] == 'X' and tauler[4] == " ":
                    tauler[4] = 'O'
                    break 
                if tauler[2] == 'X' and tauler[5] == " ":
                    tauler[5] = 'O'
                    break
              
            else:
                posicio = random.randrange(8) 
                if tauler[posicio] != 'X' and tauler[posicio] != 'O': 
                    tauler[posicio] = 'O'
                break    
            

            
        
        return tauler