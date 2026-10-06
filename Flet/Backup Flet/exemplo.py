import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # Feedback text for login action
    status_text = ft.Text(value="", color=ft.Colors.RED)

    # Input fields
    email_field = ft.TextField(
        label="E-mail",
        keyboard_type=ft.KeyboardType.EMAIL,
        prefix_icon=ft.Icons.EMAIL,
        width=300,
    )
    
    password_field = ft.TextField(
        label="Senha",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        width=300,
    )

    def handle_login(e):
        if not email_field.value or not password_field.value:
            status_text.value = "Preencha todos os campos!"
            page.update()
            return
        
        # Simple mock authentication
        if email_field.value == "teste@email.com" and password_field.value == "123456":
            status_text.color = ft.Colors.GREEN
            status_text.value = "Login realizado com sucesso!"
        else:
            status_text.color = ft.Colors.RED
            status_text.value = "E-mail ou senha incorretos."
        page.update()

    login_button = ft.ElevatedButton(
        text="Entrar",
        on_click=handle_login,
        width=300,
        height=45,
    )

    # Adding components inside a clean Column layout
    page.add(
        ft.Column(
            [
                ft.Icon(name=ft.Icons.LOCK_PERSON, size=80, color=ft.Colors.PRIMARY),
                ft.Text("Bem-vindo de volta!", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Faça login para continuar", size=14, color=ft.Colors.GREY_700),
                ft.Container(height=20),
                email_field,
                password_field,
                status_text,
                ft.Container(height=10),
                login_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)