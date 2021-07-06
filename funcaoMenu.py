# função que enumera uma lista e printa como opções [no.] - Opção.
# verifica se a resposta é numéria e se está entre as opções da lista
# Retorna a opção da lista

def menu(listaOpcoes):
    opcoes = enumerate(listaOpcoes, 1)
    for i, v in opcoes:
        print(f"[{i}] - {v}")
    resposta = ""
    while resposta.isnumeric() == False:
        resposta = input("Escolha o número da opção\n-> ")
        while resposta.isnumeric() == True and int(resposta) not in list(range(1,len(listaOpcoes)+1)):
            resposta = input("Escolha o número da opção dentre as do menu!\n-> ")
    return listaOpcoes[int(resposta) - 1]

print(f"Você vai beber {menu(['leite', 'café', 'chá', 'água'])}")
