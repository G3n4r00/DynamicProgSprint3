pontuacoes = []

def adicionar_pontuacao(nome, pontuacao):
    pontuacoes.append((nome, pontuacao))

def exibir_ranking():
    for i in range(len(pontuacoes) - 1):
        for j in range(i + 1, len(pontuacoes)):
            if pontuacoes[i][1] < pontuacoes[j][1]:
                pontuacoes[i], pontuacoes[j] = pontuacoes[j], pontuacoes[i]
    

    print("\nRanking:")
    for posicao, (nome, pontuacao) in enumerate(pontuacoes, start=1):
        print(f"{posicao}. {nome} - {pontuacao} pontos")


while True:
    nome = input("Digite o nome do jogador (ou 'sair' para finalizar): ").strip()
    if nome.lower() == 'sair':
        break
    try:
        pontuacao = int(input(f"Digite a pontuação de {nome}: "))
        adicionar_pontuacao(nome, pontuacao)
    except ValueError:
        print("Insira uma pontuacao valida!")

exibir_ranking()