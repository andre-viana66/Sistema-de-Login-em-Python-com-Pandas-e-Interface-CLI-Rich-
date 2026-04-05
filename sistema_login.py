from rich import print
from rich.panel import Panel
import pandas as pd
import os


#  Função do menu principal
def menu():  # criando menu interativo para o usuário
    print("-" * 30)
    menu_usuario = Panel(
        "[1] Acessar o sistema\n"
        "[2] Cadastrar usuário\n"
        "[3] Atualizar cadastro\n"
        "[4] Sair",
        width=30,
        title="Seja bem-vindo"
    )
    print(menu_usuario)

    #  loop para garantir entrada válida
    while True:
        try:
            escolha_usuario = int(input('Digite a opção que deseja acessar: '))

            # agora aceita de 1 a 4
            while escolha_usuario < 1 or escolha_usuario > 4:
                escolha_usuario = int(input("Digite apenas números de 1 a 4: "))

            return escolha_usuario

        except ValueError:
            print("[red]Erro: digite apenas números.[/]")


#  Função de login
def acessar_cadastro():
    print('-' * 30)

    arquivo = "lista_senhas.csv"

    #  verifica se existe base de dados
    if not os.path.exists(arquivo):
        print("[red]Nenhum usuário cadastrado[/]")
        return

    #  entrada de dados
    nome_usuario = input('Digite seu nome de usuário: ').strip()
    senha = input("Digite sua senha: ").strip()

    #  leitura do "banco"
    df = pd.read_csv(arquivo)

    #  validação de login
    resultado = df[
        (df["usuario"] == nome_usuario) &
        (df["senha"] == senha)
        ]

    #  resposta ao usuário
    if not resultado.empty:
        print("[green]Login realizado com sucesso[/]")
    else:
        print("[red]Usuário ou senha incorretos[/]")


#  Função de cadastro
def menu_cadastro():
    print('-' * 30)

    nome_usuario = input("Digite um nome de usuário: ").strip()

    print('-' * 30)
    print("A senha deve ter exatamente 8 caracteres.")

    senha = input("Digite sua senha: ").strip()

    #  validação da senha
    while len(senha) != 8:
        print('-' * 30)
        print("Digite uma senha com exatamente 8 caracteres.")
        senha = input("Digite novamente: ").strip()

    arquivo = "lista_senhas.csv"

    #  cria ou lê o banco de dados
    if os.path.exists(arquivo):
        df = pd.read_csv(arquivo)
    else:
        df = pd.DataFrame(columns=["usuario", "senha"])

    #  verifica duplicidade
    if nome_usuario in df["usuario"].values:
        print("[yellow]Esse usuário já existe[/]")
        return

    #  adiciona novo usuário
    novo_usuario = pd.DataFrame(
        [[nome_usuario, senha]],
        columns=["usuario", "senha"]
    )

    df = pd.concat([df, novo_usuario], ignore_index=True)

    #  salva no CSV
    df.to_csv(arquivo, index=False)

    print("[green]Usuário cadastrado com sucesso![/]")


#  Função de atualização de senha
def atualizacao_cadastro():
    print("-" * 30)

    arquivo = "lista_senhas.csv"

    #  verifica existência do banco
    if not os.path.exists(arquivo):
        print("[red]Nenhum usuário cadastrado[/]")
        return

    print("Confirmação de usuário")

    nome_usuario = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    df = pd.read_csv(arquivo)

    #  valida usuário
    resultado = df[
        (df["usuario"] == nome_usuario) &
        (df["senha"] == senha)
        ]

    if not resultado.empty:
        print("-" * 30)
        print("Usuário encontrado")
        print("A senha deve ter exatamente 8 caracteres.")

        nova_senha = input("Digite sua nova senha: ").strip()

        #  valida nova senha
        while len(nova_senha) != 8:
            print("-" * 30)
            print("Digite uma senha com exatamente 8 caracteres.")
            nova_senha = input("Digite novamente: ").strip()

        #  atualização no DataFrame
        df.loc[df["usuario"] == nome_usuario, "senha"] = nova_senha

        #  salva alteração
        df.to_csv(arquivo, index=False)

        print("[green]Senha atualizada com sucesso![/]")

    else:
        print("[red]Usuário não encontrado[/]")


#  Loop principal do sistema
while True:
    opcao = menu()

    if opcao == 1:
        acessar_cadastro()

    elif opcao == 2:
        menu_cadastro()

    elif opcao == 3:
        atualizacao_cadastro()

    elif opcao == 4:
        print("Saindo do programa...")
        break