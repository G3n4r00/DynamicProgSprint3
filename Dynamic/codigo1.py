pontuacoes = {}

def adicionar_pontuacao(nome, pontuacao):
    pontuacoes[nome] = pontuacao

def obter_pontuacao(item):
    return item[1]  

def exibir_ranking():
    ranking = sorted(pontuacoes.items(), key=obter_pontuacao, reverse=True)
    print("\nRanking:")
    for posicao, (nome, pontuacao) in enumerate(ranking, start=1):
        print(f"{posicao}. {nome} - {pontuacao} pontos")

        
def capturar_pontuacoes():
    while True:
        nome = input("Digite o nome do jogador (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        try:
            pontuacao = int(input(f"Digite a pontuação de {nome}: "))
            adicionar_pontuacao(nome, pontuacao)
        except ValueError:
            print("Por favor, insira um número válido para a pontuação.")


capturar_pontuacoes()
exibir_ranking()
