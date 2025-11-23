#Banco - Programa baseado em uma caixa digital que tem as seguintes opções
#pedir Usuario, Mostrar saldo, - Sacar, Depositar em dinheiro para a conta e fechar


                            #CADASTRO DO INICIO DO PROGRAMA
def Cadastro_Novo():        # classe de cadastro futuro
    print("""
Certo, seja bem vindo
Iremos fazer um Cadastro simples!""")

    nome = input("Nome: ").strip().lower()
    idade = input("Idade: ").strip().lower()
    sexo = input("""                            
Como prefere ser chamado? 
Senhor - Senhora?
: """).strip().lower()
    senha = input("Crie uma senha: ")
    saldo = float(input("Seu Saldo Atual?: "))

    print("Ótimo, Cadastro feito")
    print(f"""
Aqui está seus dados
Nome: {nome}
Idade: {idade}
Sexo: {sexo}
Senha: {senha}
Saldo: {saldo}""")

    return nome, saldo, sexo


def banco(nome, saldo, sexo):   # classe funções do banco
    while True:
        pergunta_banco = input("""
Bem vindo - Oque deseja fazer?
Ver Saldo ----------- saldo
Sacar Saldo --------- sacar
Sair Do Programa ---- sair
    """).strip().lower()

        if pergunta_banco == "saldo":
            print(f"Seu saldo é de R${saldo} {sexo} {nome}")

        elif pergunta_banco == "sacar":
            pergunta_saque = float(input("Quanto deseja sacar?: "))

            if pergunta_saque > saldo:
                print("Saldo insuficiente!")
            else:
                saldo -= pergunta_saque
                print(f"Saldo de R${pergunta_saque} sacado com sucesso! Seu saldo atual é de R${saldo}")

        elif pergunta_banco == "sair":
            print("Programa encerrado!")
            break

        else:
            print("Digite uma das alternativas acima!")

    return saldo  #  devolve o saldo atualizado


nome, saldo, sexo = Cadastro_Novo()
saldo = banco(nome=nome, saldo=saldo, sexo=sexo)  # pega o saldo atualizado

print(f"\nSaldo final após sair do banco: R${saldo}") # saldo atualizado após sair do banco
