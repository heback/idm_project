import flet as ft
from flet import (Page, Column, Row, Text, TextField,
                  FloatingActionButton, Tabs, Tab, icons,
                  ElevatedButton)



def main(page: Page):

    view = Column(
        width=600,
        controls=[
            Row(
                controls = [
                    Text('Todos'),
                ]
            ),
            Row(
                controls = [
                    TextField(
                        hint_text = "Whats needs to be done?",
                        expand = True
                    ),
                    FloatingActionButton(icon = icons.ADD)
                ]
            ),
            Column(
                controls = [
                    Tabs(
                        tabs = [
                            Tab(text = 'all'),
                            Tab(text = 'active'),
                            Tab(text = 'completed')
                        ]
                    ),
                    Column(
                        controls = []
                    )
                ]
            ),
            Row(
                controls = [
                    Text('1 active item(s) left'),
                    ElevatedButton('Clear completed')
                ]
            )
        ],
    )

    page.horizontal_alignment = "center"
    page.add(view)


ft.app(target=main)

