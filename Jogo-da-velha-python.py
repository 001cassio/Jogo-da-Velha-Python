
pontos = { "1": "1", "2":"2" , "3":"3" , "4":"4" , "5":"5" , "6":"6" , "7":"7" , "8":"8" ,"9":"9" }


def verificax():
    if pontos["1"] + pontos["2"] + pontos["3"] == "XXX":
        ganhou()
    elif pontos["4"] + pontos["5"] + pontos["6"] == "XXX":
        ganhou()
    elif pontos["7"] + pontos["8"] + pontos["9"] == "XXX":
        ganhou()     
    elif pontos["1"] + pontos["5"] + pontos["9"] == "XXX":
        ganhou()
    elif pontos["7"] + pontos["5"] + pontos["3"] == "XXX":
        ganhou()
    elif pontos["1"] + pontos["4"] + pontos["7"] == "XXX":
        ganhou()
    elif pontos["2"] + pontos["5"] + pontos["8"] == "XXX":
        ganhou()
    elif pontos["3"] + pontos["6"] + pontos["9"] == "XXX":
        ganhou()
    else:
        jogador2()

def verificay():
    if pontos["1"] + pontos["2"] + pontos["3"] == "OOO":
        ganhou()
    elif pontos["4"] + pontos["5"] + pontos["6"] == "OOO":
        ganhou()
    elif pontos["7"] + pontos["8"] + pontos["9"] == "OOO":
        ganhou()
    elif pontos["1"] + pontos["5"] + pontos["9"] == "OOO":
        ganhou()
    elif pontos["7"] + pontos["5"] + pontos["3"] == "OOO":
        ganhou()
    elif pontos["1"] + pontos["4"] + pontos["7"] == "OOO":
        ganhou()
    elif pontos["2"] + pontos["5"] + pontos["8"] == "OOO":
        ganhou()
    elif pontos["3"] + pontos["6"] + pontos["9"] == "OOO":
        ganhou()
    else:
        jogar()

def jogar ():
    jogador1()

def jogador1():
    x = int(input("digite qual numero deseja prencher com X  "))
    if x =="":
        print("Invalido, escolha novamente")
        jogador1
    elif x < 10: 
        x1 = str( x )
        if pontos[x1] != "X" and pontos[x1] != "O":
            pontos[x1] = "X"
            mostra()
            verificax()
        else:
            print("Este campo ja foi preenchido, escolha novamente")
            jogador1()
    else:
        print("digite valorres validos xxx")
def jogador2():
    y = int(input("digite qual numero deseja prencher com O  "))
    if y == "":
        print("Invalido, escolha novamente")
        jogador2
    elif y < 10:
        y1 = str(y)
        if pontos[y1] != "X" and pontos[y1] != "O":
            pontos[y1] = "O"
            mostra()
            verificay()
        else:
            print("Este campo ja foi preenchido, escolha novamente")
            jogador2()
    else:
         print("digite um valor valido")
         jogador2
def ganhou():
    print("VOCE GANHOU O JOGO")
    dinovo = input("digite sim para jogar novamente  ")
    if dinovo == "sim":
        novojogo()
    else:
        print("Ok, ate a proxima...")

def novojogo():
    pontosdinovo = { "1": "1", "2":"2" , "3":"3" , "4":"4" , "5":"5" , "6":"6" , "7":"7" , "8":"8" ,"9":"9" }
    pontos = pontosdinovo
    print(pontos)
    print("JOGO DA VELHA ")
    mostra()
    jogar()

def mostra():
    print(pontos["1"], "|" , pontos["2"] , "|" , pontos["3"])
    print(pontos["4"], "|" , pontos["5"] , "|" , pontos["6"])
    print(pontos["7"], "|" , pontos["8"] , "|" , pontos["9"])

print("JOGO DA VELHA")
mostra()
jogar()