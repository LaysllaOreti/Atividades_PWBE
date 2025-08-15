from tiposTamagoshi import TamagoshiFeliz, TamagoshiFominha, TamagoshiZangado
from salvar import salvar_bichinho, carregar_bichinho

def menu(bicho):
    while bicho.saude > 0:
        print("\n--- Menu ---")
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Passar o tempo")
        print("4. Falar")
        print("5. Salvar")
        print("6. Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            bicho.alimentar(50)
        elif escolha == "2":
            bicho.brincar(50)
        elif escolha == "3":
            bicho.tempoPassando()
        elif escolha == "4":
            bicho.falar()
        elif escolha == "5":
            salvar_bichinho(bicho, f"{bicho.nome}.json")
        elif escolha == "6":
            break

        print(f"\nStatus de {bicho.nome}:")
        print(vars(bicho))

if __name__ == "__main__":
    print("Escolha um tipo de Tamagoshi:")
    print("1. Feliz")
    print("2. Fominha")
    print("3. Zangado")

    tipo = input("Digite o número: ")
    nome = input("Dê um nome ao seu Tamagoshi: ")

    if tipo == "1":
        bicho = TamagoshiFeliz(nome)
    elif tipo == "2":
        bicho = TamagoshiFominha(nome)
    elif tipo == "3":
        bicho = TamagoshiZangado(nome)
    else:
        print("Tipo inválido. Criando um Tamagoshi Feliz por padrão.")
        bicho = TamagoshiFeliz(nome)

    menu(bicho)
