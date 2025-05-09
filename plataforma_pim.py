def etapa_1():
    print("=== Etapa 1: Cadastro ===")
    nome = input("Digite seu nome: ")
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("Idade inválida. Por favor, insira um número inteiro para a idade")
    print(f"\nOlá, {nome}, seja bem-vindo ao trabalho PIM!\n")
    return nome, idade

def etapa_2():
    print("=== Etapa 2: Consentimento de Dados ===")
    while True:
        resposta = input("Você consente com o uso dos seus dados pessoais para análises estatísticas? (sim/não): ").strip().lower()
        if resposta == "sim":
            return True
        elif resposta == "não":
            print("Você não consentiu. Retornando ao início...\n")
            return False
        else:
            print("Resposta inválida. Digite 'sim' ou 'não'.\n")

def etapa_3():
    print("=== Etapa 3: Introdução à Tecnologia da Informação ===")
    print("""
Tecnologia da Informação (TI) é o conjunto de todas as atividades e soluções produzidas por recursos de computação 
para armazenar, processar, proteger e transmitir informações. 
Ela está presente em praticamente todas as áreas da sociedade moderna.
""")
    input("Pressione Enter para continuar para a próxima etapa...")

def etapa_4():
    while True:
        print("\n=== Etapa 4: Representação de Algoritmos ===")
        print("Escolha uma forma de representação:")
        print("1. Pseudocódigo")
        print("2. Fluxograma")
        escolha = input("Digite 1 ou 2: ")

        if escolha == "1":
            print("""
Pseudocódigo é uma forma textual de representar algoritmos utilizando uma linguagem próxima da natural. 
Ele é utilizado para planejar a lógica de um programa antes da codificação.
""")
        elif escolha == "2":
            print("""
Fluxograma é uma representação gráfica de um algoritmo. 
Ele utiliza símbolos visuais para mostrar o fluxo de execução das etapas de um processo.
""")
        else:
            print("Opção inválida. Tente novamente.\n")
            continue

        proximo = input("Digite 'continuar' para seguir ou 'voltar' para escolher novamente: ").strip().lower()
        if proximo == "continuar":
            break

def etapa_5():
    print("\n=== Etapa 5: Encerramento ===")
    while True:
        sair = input("Deseja sair do sistema? (sim/não): ").strip().lower()
        if sair == "sim":
            print("Retornando ao início...\n")
            return True
        elif sair == "não":
            print("Retornando à etapa 4...\n")
            return False
        else:
            print("Opção inválida. Digite 'sim' ou 'não'.")

# Loop Principal do Sistema
while True:
    nome, idade = etapa_1()

    if not etapa_2():
        continue  # Volta para a etapa 1

    etapa_3()

    while True:
        etapa_4()
        if etapa_5():
            break  # Sai para o início

    # Mensagem final após o usuário escolher sair
    print("Obrigado por participar da nossa plataforma educacional. Até a próxima!")
    break  # Encerra o programa