import flet as ft

def main(page: ft.Page):
    imagem = ft.Image(
        src="blue-brush-stroke-frame.jpg",
        width=100,
        height=100,
    )

    page.add(imagem)

if __name__ == "__main__":
    ft.run(main)