import flet as ft


def main(page: ft.Page):
    page.add(
        # 텍스트 줄임표
        ft.Text(
            "Plain text with default style",
            width = 100,
            no_wrap = True,
            overflow = ft.TextOverflow.ELLIPSIS),

        # 중첩된 TextSpan
        ft.Text(
            "Some text",
            size=30,
            spans=[
                ft.TextSpan(
                    "here goes italic",
                    ft.TextStyle(
                        italic=True,
                        size=20,
                        color=ft.colors.GREEN
                    ),
                    spans=[
                        ft.TextSpan(
                            "bold and italic",
                            ft.TextStyle(
                                weight=ft.FontWeight.BOLD
                            ),
                        ),
                        ft.TextSpan(
                            "just italic",
                            spans=[
                                ft.TextSpan(
                                    "smaller italic",
                                    ft.TextStyle(size=15)
                                )
                            ],
                        ),
                    ],
                )
            ],
        ),
        ft.Text(
            # disabled=True,
            spans=[
                ft.TextSpan(
                    "underlined and clickable",
                    ft.TextStyle(
                        decoration=ft.TextDecoration.UNDERLINE
                    ),
                    on_click=lambda e: print(f"Clicked span: {e.control.uid}"),
                    on_enter=lambda e: print(f"Entered span: {e.control.uid}"),
                    on_exit=lambda e: print(f"Exited span: {e.control.uid}"),
                ),
                ft.TextSpan(" "),
                ft.TextSpan(
                    "underlined red wavy",
                    ft.TextStyle(
                        decoration=ft.TextDecoration.UNDERLINE,
                        decoration_color=ft.colors.RED,
                        decoration_style=ft.TextDecorationStyle.WAVY,
                    ),
                    on_enter=lambda e: print(f"Entered span: {e.control.uid}"),
                    on_exit=lambda e: print(f"Exited span: {e.control.uid}"),
                ),
                ft.TextSpan(" "),
                ft.TextSpan(
                    "overlined blue",
                    ft.TextStyle(
                        decoration=ft.TextDecoration.OVERLINE,
                        decoration_color="blue"
                    ),
                ),
                ft.TextSpan(" "),
                ft.TextSpan(
                    "overlined and underlined",
                    ft.TextStyle(
                        decoration=ft.TextDecoration.OVERLINE
                        | ft.TextDecoration.UNDERLINE
                    ),
                ),
                ft.TextSpan(" "),
                ft.TextSpan(
                    "line through thick",
                    ft.TextStyle(
                        decoration=ft.TextDecoration.LINE_THROUGH,
                        decoration_thickness=3,
                    ),
                ),
            ],
        ),
    )

    def highlight_link(e):
        e.control.style.color = ft.colors.BLUE
        e.control.update()

    def unhighlight_link(e):
        e.control.style.color = None
        e.control.update()

    page.add(
        ft.Row(
            width = 200,
            controls = [
                ft.Text(
                    disabled = False,
                    selectable = True,
                    no_wrap = True,
                    overflow = ft.TextOverflow.ELLIPSIS,
                    spans = [
                        ft.TextSpan("AwesomeApp 1.0 "),
                        ft.TextSpan(
                            "Visit our website",
                            ft.TextStyle(
                                decoration = ft.TextDecoration.UNDERLINE
                            ),
                            url = "https://google.com",
                            on_enter = highlight_link,
                            on_exit = unhighlight_link,
                        ),
                        ft.TextSpan(" All rights reserved. "),
                        ft.TextSpan(
                            "Documentation",
                            ft.TextStyle(
                                decoration = ft.TextDecoration.UNDERLINE
                            ),
                            url = "https://google.com",
                            on_enter = highlight_link,
                            on_exit = unhighlight_link,
                        ),
                    ],
                ),
            ]
        )

    )


ft.app(main)

