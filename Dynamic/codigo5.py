import json
import os

class ScoreManager:
    def __init__(self, filepath='pontuacoes.json'):
        self.filepath = filepath
        self.pontuacoes = {}
        self.load_scores()

    def adicionar_pontuacao(self, nome, pontuacao):
        if nome in self.pontuacoes:
            self.pontuacoes[nome] += pontuacao
        else:
            self.pontuacoes[nome] = pontuacao
        self.save_scores()

    def obter_ranking(self):
        # Implementação do Merge Sort para ordenar as pontuações
        items = list(self.pontuacoes.items())
        sorted_items = self.merge_sort(items)
        return sorted_items

    def merge_sort(self, items):
        if len(items) <= 1:
            return items

        meio = len(items) // 2
        esquerda = self.merge_sort(items[:meio])
        direita = self.merge_sort(items[meio:])

        return self.merge(esquerda, direita)

    def merge(self, esquerda, direita):
        resultado = []
        i = j = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i][1] > direita[j][1]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1

        # Adiciona os restantes
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado

    def save_scores(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.pontuacoes, f, indent=4)

    def load_scores(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                self.pontuacoes = json.load(f)
        else:
            self.pontuacoes = {}

    def remover_jogador(self, nome):
        if nome in self.pontuacoes:
            del self.pontuacoes[nome]
            self.save_scores()
            print(f"Jogador '{nome}' removido com sucesso.")
        else:
            print(f"Jogador '{nome}' não encontrado.")

    def atualizar_pontuacao(self, nome, nova_pontuacao):
        if nome in self.pontuacoes:
            self.pontuacoes[nome] = nova_pontuacao
            self.save_scores()
            print(f"Pontuação de '{nome}' atualizada para {nova_pontuacao}.")
        else:
            print(f"Jogador '{nome}' não encontrado.")

def menu_principal(manager):
    while True:
        print("\n=== Sistema de Pontuação com Recursão ===")
        print("1. Registrar Pontuação")
        print("2. Exibir Ranking")
        print("3. Remover Jogador")
        print("4. Atualizar Pontuação")
        print("5. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            registrar_pontuacao(manager)
            menu_principal(manager)  # Chamada recursiva após a operação
            break

        elif escolha == "2":
            exibir_ranking(manager)
            menu_principal(manager)  # Chamada recursiva após a operação
            break

        elif escolha == "3":
            remover_jogador(manager)
            menu_principal(manager)  # Chamada recursiva após a operação
            break

        elif escolha == "4":
            atualizar_pontuacao(manager)
            menu_principal(manager)  # Chamada recursiva após a operação
            break

        elif escolha == "5":
            print("Finalizando o programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")
            menu_principal(manager)  # Chamada recursiva para opção inválida
            break

def registrar_pontuacao(manager):
    nome = input("Digite o nome do jogador: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return
    try:
        pontuacao = int(input(f"Digite a pontuação de {nome}: "))
        manager.adicionar_pontuacao(nome, pontuacao)
        print(f"Pontuação de {nome} registrada com sucesso!")
    except ValueError:
        print("Pontuação inválida. Por favor, insira um número inteiro.")

def exibir_ranking(manager):
    ranking = manager.obter_ranking()
    print("\n=== Ranking ===")
    for pos, (nome, pontuacao) in enumerate(ranking, start=1):
        print(f"{pos}. {nome} - {pontuacao} pontos")

def remover_jogador(manager):
    nome = input("Digite o nome do jogador a remover: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return
    manager.remover_jogador(nome)

def atualizar_pontuacao(manager):
    nome = input("Digite o nome do jogador para atualizar: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return
    try:
        nova_pontuacao = int(input(f"Digite a nova pontuação de {nome}: "))
        manager.atualizar_pontuacao(nome, nova_pontuacao)
    except ValueError:
        print("Pontuação inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    score_manager = ScoreManager()
    menu_principal(score_manager)
