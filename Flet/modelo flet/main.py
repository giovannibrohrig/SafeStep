import flet as ft


# Função principal do nosso aplicativo
def main(page: ft.Page):

    # Define o título da janela
    page.title = "SafeStep"

    # Centraliza o conteúdo verticalmente
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Centraliza o conteúdo horizontalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    # Campo para digitar o usuário
    usuario = ft.TextField(
        label="Insira o Email ou Telefone",
        width=300
    )


    # Campo para digitar a senha
    senha = ft.TextField(
        label="Insira a Senha",
        password=True,
        width=300
    )


    # Texto que vamos usar para mostrar mensagens
    mensagem = ft.Text()


    # Função executada quando o usuário clicar em "Entrar"
    def fazer_login(e):

        # Verifica se usuário e senha estão corretos
        if usuario.value == "admin" and senha.value == "1234":

            # Altera o texto da mensagem
            mensagem.value = "Login realizado com sucesso!"

        else:

            # Caso estejam errados
            mensagem.value = "Usuário ou senha incorretos."

        # Atualiza a página
        page.update()


    # Cria o botão de login
    botao = ft.Button(
        "Entrar",
        on_click=fazer_login,
        width=300
    )


    # Organiza os elementos verticalmente
    tela_login = ft.Column(
        [
            # Título
            ft.Text(
                "Login",
                size=30,
                weight=ft.FontWeight.BOLD
            ),

            # Campo de usuário
            usuario,

            # Campo de senha
            senha,

            # Botão
            botao,

            # Mensagem
            mensagem
        ],

        # Centraliza os elementos
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        # Espaçamento entre eles
        spacing=15
    )


    # Coloca a tela de login na página
    page.add(tela_login)


# Inicia o aplicativo
ft.run(main)
