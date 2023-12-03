import flet as ft


class Greeting(ft.UserControl):
    def build(self):
        return ft.Column(
            controls = [
                ft.Text("Hello control"),
                ft.ElevatedButton('Login')
            ]
        )


def main(page: ft.Page):
    page.add(Greeting())


ft.app(target = main)

