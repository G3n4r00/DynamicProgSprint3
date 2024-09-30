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
        self.salvar_scores()  # Corrigido para chamar o método correto

    def obter_ranking(self):
        return sorted(self.pontuacoes.items(), key=lambda item: item[1], reverse=True)

    def salvar_scores(self):
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.pontuacoes, f, indent=4)
        except IOError as e:
            print(f"Erro ao salvar as pontuações: {e}")

    def load_scores(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    self.pontuacoes = json.load(f)
            except json.JSONDecodeError:
                print("Erro ao carregar as pontuações. O arquivo JSON está corrompido.")
                self.pontuacoes = {}
            except IOError as e:
                print(f"Erro ao ler o arquivo de pontuações: {e}")
                self.pontuacoes = {}
        else:
            self.pontuacoes = {}

    def remover_jogador(self, nome):
        if nome in self.pontuacoes:
            del self.pontuacoes[nome]
            self.salvar_scores()
            print(f"Jogador '{nome}' removido com sucesso.")
        else:
            print(f"Jogador '{nome}' não encontrado.")

    def atualizar_pontuacao(self, nome, nova_pontuacao):
        if nome in self.pontuacoes:
            self.pontuacoes[nome] = nova_pontuacao
            self.salvar_scores()
            print(f"Pontuação de '{nome}' atualizada para {nova_pontuacao}.")
        else:
            print(f"Jogador '{nome}' não encontrado.")

def menu():
    manager = ScoreManager()
    while True:
        print("\n=== Sistema de Pontuação ===")
        print("1. Registrar Pontuação")
        print("2. Exibir Ranking")
        print("3. Remover Jogador")
        print("4. Atualizar Pontuação")
        print("5. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            nome = input("Digite o nome do jogador: ").strip()
            if not nome:
                print("Nome não pode ser vazio.")
                continue
            try:
                pontuacao = int(input(f"Digite a pontuação de {nome}: "))
                manager.adicionar_pontuacao(nome, pontuacao)
                print(f"Pontuação de {nome} registrada com sucesso!")
            except ValueError:
                print("Pontuação inválida. Por favor, insira um número inteiro.")

        elif escolha == "2":
            ranking = manager.obter_ranking()
            print("\n=== Ranking ===")
            if not ranking:
                print("Nenhuma pontuação registrada ainda.")
            else:
                for pos, (nome, pontuacao) in enumerate(ranking, start=1):
                    print(f"{pos}. {nome} - {pontuacao} pontos")

        elif escolha == "3":
            nome = input("Digite o nome do jogador a remover: ").strip()
            if not nome:
                print("Nome não pode ser vazio.")
                continue
            manager.remover_jogador(nome)

        elif escolha == "4":
            nome = input("Digite o nome do jogador para atualizar: ").strip()
            if not nome:
                print("Nome não pode ser vazio.")
                continue
            try:
                nova_pontuacao = int(input(f"Digite a nova pontuação de {nome}: "))
                manager.atualizar_pontuacao(nome, nova_pontuacao)
            except ValueError:
                print("Pontuação inválida. Por favor, insira um número inteiro.")

        elif escolha == "5":
            print("Finalizando o programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

if __name__ == "__main__":
    menu()
