import flet as ft


def main(page: ft.Page):

    # Task 컨트롤 목록을 가지는 레이아웃
    tasks = ft.Column()

    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls = [
                    ft.Text('Todos'),
                ]
            ),
            ft.Row(
                controls = [
                    ft.TextField(
                        hint_text = "Whats needs to be done?",
                        expand = True
                    ),
                    ft.FloatingActionButton(icon = ft.icons.ADD)
                ]
            ),
            ft.Column(
                controls = [
                    ft.Tabs(
                        tabs = [
                            ft.Tab(text = 'all'),
                            ft.Tab(text = 'active'),
                            ft.Tab(text = 'completed')
                        ]
                    ),
                    ft.Column(
                        controls = []
                    )
                ]
            ),
            ft.Row(
                controls = [
                    ft.Text('1 active item(s) left'),
                    ft.ElevatedButton('Clear completed')
                ]
            )
        ],
    )

    def add_clicked(e):
        pass

    page.horizontal_alignment = "center"
    page.add(view)


ft.app(target=main)

