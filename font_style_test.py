import flet as ft

txt: ft.Text = ft.Text(
    spans = [ft.TextSpan('텍스트 스타일 테스트', ft.TextStyle(decoration = ft.TextDecoration.NONE))]
)


def main(page: ft.Page):

    def cancel_text(e):
        txt.spans[0].style = ft.TextStyle(decoration = ft.TextDecoration.LINE_THROUGH)
        page.update()

    page.add(txt)
    page.add(
        ft.ElevatedButton('취소', on_click = cancel_text)
    )
    page.update()


ft.app(target = main)