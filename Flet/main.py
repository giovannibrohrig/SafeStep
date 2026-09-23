#pip install flet

import flet as ft


def main(page: ft.Page):
    page.title = "SafeStep" #titulo da aplicação
    page.add(ft.SafeArea(content=ft.Text("Bem-Vindo")))
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #alinhamento Y
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #alinhamento X
    # page.padding = 20
    # page.theme = ft.ThemeMode.LIGHT #cor do tema

    status_text = ft.Text(value='', color=ft.Colors.RED) #nao sei oq faz ainda

    campo_email = ft.TextField(
        label='E-mail',
        keyboard_type=ft.KeyboardType.EMAIL,
        prefix_icon=ft.Icons.EMAIL,
        width=300,


    )


    page.add(
        ft.Button('Login')
    )


if __name__ == "__main__":
    ft.run(main)