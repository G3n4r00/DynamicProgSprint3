import os

azul = "\033[0;34m"
verde = "\033[0;32m"
vermelho = "\033[0;31m"
amarelo = "\033[0;33m"

lista_nomes=[]
lista_pontuacao = []

def organizador(pontos, nomes):
    
    indice_maior = 0
    indice_atual=0
    
    while indice_atual != len(pontos):
        
        indice_maior = indice_atual
        
        for i in range(indice_atual,len(pontos)):
            
            if pontos[i] > pontos[indice_maior]:
                indice_maior = i
      
        salva_ponto = pontos[indice_atual]
        salva_nome = nomes[indice_atual]
    
        pontos[indice_atual] = pontos[indice_maior]
        nomes[indice_atual] = nomes[indice_maior]

        pontos[indice_maior] = salva_ponto
        nomes[indice_maior] = salva_nome

        indice_atual+=1



while True:
    
    try:
        escolha = input(f"""{amarelo}
Bem-vindo ao sistema de placares:

Deseja Registrar uma pontuação ou Consultar o Ranking?

1 - {azul}Registrar
{amarelo}2 - {azul}Ranking
{amarelo}3 - {azul}Sair

""")

        os.system('cls')


        if escolha == "1":
            while True:
                nome = input(f"""{amarelo}(Caso queira voltar apenas deixe os espaços em branco)

{azul}Informe seu nome: """)

                if nome == "":
                  os.system('cls')
                  print(f"{vermelho}Voltando ao menu...")
                  break

                else:
                    try:
                        pontuacao = int(input(f"{azul}Informe a pontuação de '{verde}{nome}{azul}': {amarelo}"))

                        lista_nomes.append(nome)
                        lista_pontuacao.append(pontuacao)

                        os.system('cls')

                        print(f"{verde}Registro de '{nome}' feito com sucesso!!")
                        organizador(lista_pontuacao,lista_nomes)
                        break

                    except:
                        break

        if escolha == "2":
            os.system('cls')
            print(f"{amarelo}Pressione ENTER para voltar ao menu")
            print(f"|{verde}(Pos) {azul}Nome{verde}----------->{amarelo}Pontuação")
            for posicao in range(0, len(lista_nomes)):
                print(f"|{verde}{posicao+1}° {azul}{lista_nomes[posicao]}{verde} ----> {amarelo}{lista_pontuacao[posicao ]}")
            input()


        if escolha == "3":
            print(f"{vermelho}Finalizando programa...")
            break

        else:
            print(f"{azul}Escolha uma das opções demonstradas")
    except:
        os.system('cls')
        print(f"{vermelho}Escolha inválida...")