import flet as ft

def main(page: ft.Page):

    page.add(
        ft.Stack(
            [
                ft.Container(
                    bgcolor="red",
                    width=100,
                    height=100,
                    left=100,
                    top=100,
                    offset=ft.transform.Offset(-1, -2),
                )
            ],
            width=1000,
            height=1000,
        )
    )

ft.app(target=main)