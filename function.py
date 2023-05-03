import os 

def limpar_tela():
    return os.system("cls")

def dica_e_nome():
    limpar_tela()
    print("Jogo da Forca")
    palavra = (input("Escolha sua Palavra:")).lower().strip()
    dica1 = (input("Digite a Primeira Dica:")).lower().strip()
    dica2 = (input("Digite a Segunda Dica:")).lower().strip()
    dica3 = (input("Digite a Terceira Dica:")).lower().strip()
    return (palavra,dica1,dica2,dica3)


def player_name():
    player1 = input("Digite seu nome:").lower().strip()
    player2 = input("Digite o nome do seu adversario:").lower().strip()
    return(player1,player2)

def escolher_palavra(palavra):
    palavra_oculta = "*" * len(palavra)
    print(f"A palavra chave tem {len(palavra)} letras: {palavra_oculta}")
    print("Escolha uma opção:")
    print("1 - Jogar")
    print("2 - Solicitar dica")
    

        







               





    

    




