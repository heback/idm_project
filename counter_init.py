import flet as ft


class Counter(ft.UserControl):

    def __init__(self, initial_count):
        super().__init__()
        self.counter = initial_count
        self.text = ft.Text(str(self.counter))

    def add_click(self, e: ft.ControlEvent):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        return ft.Row(
            [
                self.text,
                ft.ElevatedButton(
                    "Add",
                    on_click=self.add_click
                )
            ]
        )


# then use the control
def main(page):
    page.add(
        Counter(100),
        Counter(200))


ft.app(target=main)

