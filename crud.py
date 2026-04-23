import json
import os

def ler_dados():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_dados(dados):
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

def escolher_grupo():
    print("\n1. Personagem | 2. Player")
    opcao = input("Escolha: ")
    
    if opcao == "1": 
        return "personagens"
    if opcao == "2": 
        return "player"
    return None

def adicionar():
    grupo = escolher_grupo()
    if not grupo: return
    
    dados = ler_dados()
    
    if grupo == "personagens":
        novo = {
            "nome": input("Nome: "),
            "constelacao": int(input("Constelação: ")),
            "tipo": input("Tipo (ex: pyro): "),
            "combate": input("Combate (ex: catalizador): ")
        }
    else:
        novo = {
            "nome": input("Nome: "),
            "nickname": input("Nickname: "),
            "ar": int(input("AR: "))
        }
    
    dados[grupo].append(novo)
    salvar_dados(dados)
    print("Adicionado com sucesso!")

def listar():
    grupo = escolher_grupo()
    if not grupo: return
    
    dados = ler_dados()
    print(f"\nLista de {grupo.upper()}:")
    for index, item in enumerate(dados[grupo], start=1):
        print(f"{index}. {item}")

def atualizar():
    grupo = escolher_grupo()
    if not grupo: return
    
    dados = ler_dados()
    index = int(input("Index para atualizar: ")) - 1
    
    if 0 <= index < len(dados[grupo]):
        if grupo == "personagens":
            dados[grupo][index] = {
                "nome": input("Novo Nome: "),
                "constelacao": int(input("Nova Constelação: ")),
                "tipo": input("Novo Tipo: "),
                "combate": input("Novo Combate: ")
            }
        else:
            dados[grupo][index] = {
                "nome": input("Novo Nome: "),
                "nickname": input("Novo Nickname: "),
                "ar": int(input("Novo AR: "))
            }
        salvar_dados(dados)
        print("Atualizado!")
    else:
        print("Índice inválido.")

def excluir():
    grupo = escolher_grupo()
    if not grupo: return
    
    dados = ler_dados()
    index = int(input("Index para excluir: ")) - 1
    
    if 0 <= index < len(dados[grupo]):
        dados[grupo].pop(index)
        salvar_dados(dados)
        print("Excluído!")
    else:
        print("Índice inválido.")

def main():
    while True:
        print("\n === MENU GENSHIN ===")
        print("1. Adicionar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Sair")

        opcao = input("Opção: ")
        if opcao == "1": 
            adicionar()
        elif opcao == "2": 
            listar()
        elif opcao == "3": 
            atualizar()
        elif opcao == "4": 
            excluir()
        elif opcao == "5": 
            break

main()