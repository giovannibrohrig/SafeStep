import flet as ft


def main(page: ft.Page):
    page.title = "SafeStep"
    page.window_width = 400
    page.window_height = 750
    page.padding = 0

    usuario = ft.TextField(
        label="Usuário",
        prefix_icon=ft.Icons.PERSON,
        width=300,
        border_radius=10,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE,
    )

    senha = ft.TextField(
        label="Senha",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=300,
        border_radius=10,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE,
    )

    mensagem = ft.Text(color=ft.Colors.RED, size=13)

    # ────────────────────────────────────────────
    #  Tela principal (após login)
    # ────────────────────────────────────────────

    def tela_principal(nome_usuario):
        page.clean()

        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(
                            ft.Icons.VERIFIED_USER,
                            size=80,
                            color=ft.Colors.WHITE,
                        ),
                        ft.Container(height=15),
                        ft.Text(
                            f"Bem-vindo,",
                            size=18,
                            color=ft.Colors.BLUE_100,
                        ),
                        ft.Text(
                            nome_usuario,
                            size=30,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        ),
                        ft.Container(height=5),
                        ft.Text(
                            "Login realizado com sucesso.",
                            size=14,
                            color=ft.Colors.BLUE_200,
                        ),
                        ft.Container(height=40),
                        ft.Button(
                            "Sair",
                            icon=ft.Icons.LOGOUT,
                            on_click=voltar_login,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=2,
                ),
                gradient=ft.LinearGradient(
                    begin=ft.Alignment.TOP_CENTER,
                    end=ft.Alignment.BOTTOM_CENTER,
                    colors=[
                        ft.Colors.BLUE_900,
                        ft.Colors.BLUE_800,
                        ft.Colors.BLUE_600,
                    ],
                ),
                expand=True,
                alignment=ft.Alignment.CENTER,
            )
        )
        page.update()

    # ────────────────────────────────────────────
    #  Navegação
    # ────────────────────────────────────────────

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

        tela_principal(nome)

    def cadastrar_usuario(e):
        nome = usuario.value.strip()
        password = senha.value

        if not nome or not password:
            mensagem.value = "Informe usuário e senha para cadastrar."
            mensagem.color = ft.Colors.RED
            page.update()
            return

        mensagem.value = "Cadastrado com sucesso! Faça o login."
        mensagem.color = ft.Colors.GREEN
        senha.value = ""
        page.update()

    # ────────────────────────────────────────────
    #  Tela de login
    # ────────────────────────────────────────────

    def criar_tela_login():
        page.clean()
        usuario.value = ""
        senha.value = ""
        mensagem.value = ""

        # ── Área de branding (topo) ──
        topo = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(
                        ft.Icons.SHIELD,
                        size=50,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Container(height=10),
                    ft.Text(
                        spans=[
                            ft.TextSpan(
                                "SAFE",
                                style=ft.TextStyle(
                                    color=ft.Colors.WHITE,
                                ),
                            ),
                            ft.TextSpan(
                                "STEP",
                                style=ft.TextStyle(
                                    color=ft.Colors.LIGHT_BLUE_200,
                                ),
                            ),
                        ],
                        size=42,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Protegendo cada passo.",
                        size=14,
                        color=ft.Colors.BLUE_100,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=2,
            ),
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=[
                    ft.Colors.BLUE_900,
                    ft.Colors.BLUE_700,
                    ft.Colors.BLUE,
                ],
            ),
            padding=40,
            alignment=ft.Alignment.CENTER,
        )

        # ── Área do formulário (baixo) ──
        formulario = ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=15),
                    ft.Text(
                        "Entrar na sua conta",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900,
                    ),
                    ft.Container(height=20),
                    usuario,
                    senha,
                    mensagem,
                    ft.Container(height=10),
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
                spacing=12,
            ),
            bgcolor=ft.Colors.WHITE,
            padding=30,
            expand=True,
        )

        page.add(
            ft.Column(
                [topo, formulario],
                expand=True,
                spacing=0,
            )
        )

    criar_tela_login()


if __name__ == "__main__":
    ft.run(main)
