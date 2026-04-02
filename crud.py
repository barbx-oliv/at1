import json 
import os 

# Menu Principal 

def menu():
    print("\n === LISTAGEM GENSHIN ===")
    print("1. Adicionar personagem/player")
    print("2. Favoritar persongem")
    print("3. Listar personagens")
    print("4. Listar players")
    print("4. Classificar personagens por tipo e combate")
    print("5. Classificar players por AR")
    print(" ==================== ")
    print("6. Sair")

def escolher_grupo():
    print("\nO que você quer adicionar?: ")
    print("1. Personagem")
    print("2. Player")

    opcao = input("Escolha: ")

    if opcao == "1":
        return "Personagem"
    
    elif opcao == "2":
        return "Player"
    
    else: 
        print("Opção inválida! Verifique sua escolha e tente novamente.")
        return None
    
def ler_dados():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def salvar_dados(dados):
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

def adicionar():
    grupo = escolher_grupo()
    if not grupo:
        return
    
    if grupo == "Personagem":
        nome = input("Nome: ")
        constelacao = int(input("Constelação(4 ou 5): "))
        tipo = input("Tipo: ")
        combate = input("Combate")

        dados = ler_dados()

        dados[grupo].append({
            "Personagem": nome,
            "Constelação": constelacao,
            "Tipo": tipo,
            "Combate": combate
        })

        salvar_dados(dados)
        print("Personagem salvado com Sucesso!!")
    
    else:
        nome = input("Nome: ")
        nickname = input("Nickname")
        ar = int(input("AR (Nível de Aventura): "))

        dados = ler_dados()

        dados[grupo].append({
             "Nome": nome,
            "nickname": nickname,
            "AR (Nível de Aventura)": ar
        })

        salvar_dados(dados)
        print("Player salvo com Sucesso!")

def listar():
    grupo = escolher_grupo()

    if not grupo:
        return
    
    dados = ler_dados()
    print(f"Lista de {grupo.upper()}:")

    for index, personagem in enumerate(dados[grupo], start=1):
        print(f"{index}. {personagem['Nome']}")
    
    



