import flet as ft
from models import Session, Usuario


def main(page: ft.Page):
    page.title = "Bem-vindo ao SafeStep!"
    page.window_width = 900
    page.window_height = 600
    page.padding = 0
    page.assets_dir = "assets"

    session = Session()

    usuario = ft.TextField(
        label="Usuário",
        prefix_icon=ft.Icons.PERSON,
        width=300,
    )

    senha = ft.TextField(
        label="Senha",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=300,
    )

    mensagem = ft.Text(color=ft.Colors.RED)

    def tela_principal(nome_usuario):
        page.clean()

        # A imagem pode ser substituída por outra URL ou por
        # uma imagem local em assets/fundo.jpg.
        fundo = ft.Image(
            src="fundo.png",
            fit="cover",
            expand=True,
        )

        conteudo = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        f"Bem-vindo, {nome_usuario}!",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Login realizado com sucesso.",
                        size=18,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Button(
                        "Sair",
                        icon=ft.Icons.LOGOUT,
                        on_click=voltar_login,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            bgcolor=ft.Colors.with_opacity(0.70, ft.Colors.BLACK),
            padding=40,
            border_radius=15,
        )

        page.add(
            ft.Stack(
                [
                    fundo,
                    ft.Container(
                        content=conteudo,
                        alignment=ft.Alignment.CENTER,
                        expand=True,
                    ),
                ],
                expand=True,
            )
        )
        page.update()

    def voltar_login(e):
        page.clean()
        criar_tela_login()
        page.update()

    def fazer_login(e):
        nome = usuario.value.strip()
        password = senha.value

        if not nome or not password:
            mensagem.value = "Informe usuário e senha."
            page.update()
            return

        usuario_db = (
            session.query(Usuario)
            .filter_by(usuario=nome, senha=password)
            .first()
        )

        if usuario_db:
            mensagem.value = ""
            tela_principal(usuario_db.usuario)
        else:
            mensagem.value = "Usuário ou senha inválidos."
            senha.value = ""
            page.update()

    def cadastrar_usuario(e):
        nome = usuario.value.strip()
        password = senha.value

        if not nome or not password:
            mensagem.value = "Informe usuário e senha para cadastrar."
            mensagem.color = ft.Colors.RED
            page.update()
            return

        existente = session.query(Usuario).filter_by(usuario=nome).first()

        if existente:
            mensagem.value = "Esse usuário já existe."
            mensagem.color = ft.Colors.RED
            page.update()
            return

        novo_usuario = Usuario(usuario=nome, senha=password)
        session.add(novo_usuario)
        session.commit()

        mensagem.value = "Usuário cadastrado com sucesso. Faça o login."
        mensagem.color = ft.Colors.GREEN
        senha.value = ""
        page.update()

    def criar_tela_login():
        page.clean()

        titulo = ft.Text(
            "SafeStep",
            size=70,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_GREY_900,
        )

        subtitulo = ft.Text("Bem-vindo ao SafeStep!")

        painel = ft.Container(
            content=ft.Column(
                [
                    titulo,
                    subtitulo,
                    usuario,
                    senha,
                    mensagem,
                    ft.Row(
                        [
                            ft.Button(
                                "Entrar",
                                icon=ft.Icons.LOGIN,
                                on_click=fazer_login,
                            ),
                            ft.OutlinedButton(
                                "Cadastrar",
                                icon=ft.Icons.PERSON_ADD,
                                on_click=cadastrar_usuario,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            ),
            width=420,
            padding=35,
            border_radius=15,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(
                blur_radius=20,
                spread_radius=2,
                color=ft.Colors.BLACK_26,
            ),
        )

        page.add(
            ft.Container(
                content=painel,
                alignment=ft.Alignment.CENTER,
                expand=True,
                bgcolor=ft.Colors.BLUE_GREY_50,
            )
        )

    criar_tela_login()


'''if __name__ == "__main__":
    ft.app(target=main)'''

if __name__ == "__main__":

    #Cadastrando um user padrão quando inicia, só para poder logar.
    #Comente depois

    '''session = Session()
    usuario = Usuario(
        usuario="admin",
        senha="1234"
    )

    session.add(usuario)
    session.commit()
    session.close()'''
    

    ft.run(main)
