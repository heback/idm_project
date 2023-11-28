import flet as ft

def main(page: ft.Page):
    # 창 크기 설정
    page.window_width = 600
    page.window_height = 400

    # 텍스트 필드 상태
    txt_name = ft.TextField(label="Your name", width=200)
    txt_email = ft.TextField(label="Your email", width=200)
    txt_message = ft.TextField(label="Your message", multiline=True, expand=True)

    # 버튼 이벤트 핸들러
    def send_click(e):
        page.dialog(ft.AlertDialog(
            title="Submission received!",
            content=ft.Text(f"Name: {txt_name.value}\nEmail: {txt_email.value}\nMessage: {txt_message.value}"),
            actions=[ft.TextButton("Close", on_click=lambda e: page.dialog_close())]
        ))

    # 레이아웃과 컨트롤
    main_column = ft.Column(
        controls=[
            ft.Row(controls=[
                ft.Column(controls=[
                    ft.Text("Contact Form", size=20),
                    txt_name,
                    txt_email,
                    txt_message,
                    ft.ElevatedButton("Send", on_click=send_click)
                ], width=300),
                ft.Column(controls=[
                    ft.Checkbox(label="Subscribe to newsletter"),
                    ft.RadioButton(label="Male", group_name="gender"),
                    ft.RadioButton(label="Female", group_name="gender"),
                    ft.RadioButton(label="Other", group_name="gender"),
                    ft.Toggle(label="Enable notifications"),
                    ft.Dropdown(
                        label="Select your country",
                        options=[
                            ft.DropdownItem(text="United States"),
                            ft.DropdownItem(text="Canada"),
                            ft.DropdownItem(text="Australia"),
                        ]
                    ),
                    ft.Slider(value=50, min=0, max=100),
                    ft.Icon(name="face", size=50)
                ], width=300),
            ])
        ],
        expand=True,
    )

    # 페이지에 메인 레이아웃 추가
    page.add(main_column)

ft.app(target=main)
