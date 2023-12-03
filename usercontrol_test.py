import flet as ft


class Greeting(ft.UserControl):
    def build(self):
        return ft.Text("Hello control")


def main(page: ft.Page):
    page.add(Greeting())


ft.app(target = main)

