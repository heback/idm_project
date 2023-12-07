import flet as ft


def main(page: ft.Page):

    # date_picker 에서 날짜를 선택 하고 OK 클릭 하면
    def change_time(e):
        txt_time.value = \
            time_picker.value.strftime('%H:%M')
        page.update()

    # date_picker 에서 cancel 클릭 하면
    def time_picker_dismissed(e):
        print(f"Date picker dismissed, value is")
        print(f"{time_picker.value}")

    # DatePicker 생성
    time_picker = ft.TimePicker(
        # OK
        on_change = change_time,
        # Cancel
        on_dismiss = time_picker_dismissed,
    )

    # 모달 대화창에 등록
    page.overlay.append(time_picker)

    # 선택한 날짜 표시 텍스트 컨트롤
    txt_time = ft.Text(width = 120)

    # 대화창 표시
    def pick_time(e):
        time_picker.pick_time()

    # 대화창 버튼
    date_button = ft.ElevatedButton(
        "Pick time",
        icon=ft.icons.TIMER,
        on_click=pick_time
    )

    page.add(
        ft.Row(
            controls=[txt_time, date_button]
        )
    )


ft.app(target=main)

