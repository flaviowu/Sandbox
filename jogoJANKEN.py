from random import choice
from time import sleep

jankenpon = ["じゃん", "けん", "ぽん!"]
aikodesho = ["あい", "こ", "で","しょ!"]
saishowaguu = ["さい", "しょ", "は", "ぐう!"]

def game_ON():
    sleep(0.5)
    print(45*"=")
    print("Escolha: ")
    print("[1] - Pedra")
    print("[2] - Papel")
    print("[3] - Tesoura")
    u_K_index = int(input("> ")) - 1
    return u_K_index

def decideWinner(a, b):
    print(45*"=")
    if a == b:
        return "CPUSER"
    elif a == "Pedra":
        if b == "Papel":
            return "CPU"
        elif b == "Tesoura":
            return "USER"
    elif a == "Tesoura":
        if b == "Pedra":
            return "CPU"
        elif b == "Papel":
            return "USER"
    elif a == "Papel":
        if b == "Tesoura":
            return "CPU"
        elif b == "Pedra":
            return "USER"
    else:
        print("Opção Inválida! Rodada anulada!")
        return "PASSAR"
      
def printLista(lista):
    print(f'\n')
    for i in lista:
        print(i)
        print()
        sleep(0.5)

init_flag = "S"
print("Vamos jogar JANKEN?")
start_flag = input("(S/N) >> ").strip().upper()
while init_flag == "S":

    if start_flag == "N":
        break
    n = int(input("Quantas rodadas deseja jogar? >> "))
    score_sys = []
    score_user = []
    rodada = 0
    intern_count = 0
    while sum(score_user) < n or sum(score_sys) < n:
        ken = ["Pedra", "Papel", "Tesoura"]
        intern_count += 1
        if intern_count == 1 and score_sys == [] and score_user == []:
            printLista(saishowaguu)
        printLista(jankenpon)
        system_ken = choice(ken)
        user_ken = ken[game_ON()-1]
       
        if decideWinner(user_ken, system_ken) == "USER":
            score_sys.append(0)
            score_user.append(1)
            print("Parabéns! Você ganhou a rodada!")
            rodada += 1
        elif decideWinner(user_ken, system_ken) == "CPU":
            score_sys.append(1)
            score_user.append(0)
            print("Que pena! Você perdeu!")
            rodada += 1
        elif decideWinner(user_ken, system_ken) == "CPUSER":
            print("Empate! Ninguém Pontua. Rodada anulada.")
            printLista(aikodesho)
            continue
        else:
            pass
        
        print(f"A CPU escolheu {system_ken}.\nVocê escolheu {user_ken}.\n")
        print(f"Placar:\n  Usuário: {sum(score_user)} X CPU: {sum(score_sys)}")
        print(f"  Rodada(s) válidas: {rodada}\n  Rolagens: {intern_count}")
        
    if sum(score_user) > sum(score_sys):
        print("Parabéns! Você venceu a partida!")
    elif sum(score_user) < sum(score_sys):
        print("Que pena! Continue tentando.")
    elif sum(score_user) == sum(score_sys):
        print("Deu empate. Continue tentando.")
    print("Deseja jogar novamente?")
    init_flag = input("(S/N)> ").strip().upper()
print(45*"=")
print(f"OK! Encerrando...\n遊んでくれてありがとうございました！\n終わり。。。")
