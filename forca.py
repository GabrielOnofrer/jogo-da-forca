from function import limpar_tela
import time
while True:

    desafiante = input("Digite o nome do desafiante: ")
    competidor = input("Digite o nome do competidor: ")
    
    palavra_chave = input("Digite a palavra chave: ")
    dica1 = input("Digite a dica 1: ")
    dica2 = input("Digite a dica 2: ")
    dica3 = input("Digite a dica 3: ")
    dicas = [dica1, dica2, dica3]

    limpar_tela()
    
    
    palavra_oculta = "*" * len(palavra_chave)
    print(f"A palavra chave tem {len(palavra_chave)} letras: {palavra_oculta}")
    print("Escolha uma opção:")
    print("1 - Jogar")
    print("2 - Solicitar dica")
    
    
    num_erros = 0
    dicas_restantes = 3
    while True:
        opcao = input("Digite sua opção: ")
        
        if opcao == "1":
            letra = input("Digite uma letra: ")
            if letra in palavra_chave:
                print("Acertou!")
                for i in range(len(palavra_chave)):
                    if palavra_chave[i] == letra:
                        palavra_oculta = palavra_oculta[:i] + letra + palavra_oculta[i+1:]
                print(palavra_oculta)
                
                if "*" not in palavra_oculta:
                    print("Parabéns, você ganhou!")
                    break
            else:
                num_erros += 1
                print(f"Erro: {num_erros}")
                if num_erros >= 6:
                    print("Você perdeu!")
                    print(f"A palavra era {palavra_chave}!")
                    break
                    
        elif opcao == "2":
            if dicas_restantes == 0:
                print("Você já usou todas as dicas!")
            else:
                dicas_restantes -= 1
                print(f"Dica {3-dicas_restantes}: {dicas[2-dicas_restantes]}")
                letra = input("Digite uma letra: ")
                if letra in palavra_chave:
                    print("Acertou!")
                    for i in range(len(palavra_chave)):
                        if palavra_chave[i] == letra:
                            palavra_oculta = palavra_oculta[:i] + letra + palavra_oculta[i+1:]
                    print(palavra_oculta)
                    
                    if "*" not in palavra_oculta:
                        print("Parabéns, você ganhou!")
                        break
                else:
                    num_erros += 1
                    print(f"Erro: {num_erros}")
              
        







