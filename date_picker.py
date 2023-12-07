from datetime import datetime
import flet as ft


def main(page: ft.Page):

    # 올해
    this_year = datetime.now().year

    # 이번 달
    this_month = datetime.now().month

    # 오늘
    this_date = datetime.now().day

    # date_picker 에서 날짜를 선택 하고 OK 클릭 하면
    def change_date(e):
        txt_date.value = str(date_picker.value.date())
        page.update()

    # date_picker 에서 cancel 클릭 하면
    def date_picker_dismissed(e):
        print(f"Date picker dismissed, value is")
        print(f"{date_picker.value}")

    # DatePicker 생성
    date_picker = ft.DatePicker(
        # OK
        on_change = change_date,
        # Cancel
        on_dismiss = date_picker_dismissed,
        # 달력 표시 시작 날짜
        first_date = datetime(1970, 1, 1),
        # 달력 표시 마지막 날짜
        last_date = datetime(this_year + 1, 12, 31),
        current_date = datetime(
            this_year, this_month, this_date),
        # 날짜 입력 방법 모드
        date_picker_entry_mode = \
            ft.DatePickerEntryMode.CALENDAR_ONLY
    )

    # 모달 대화창에 등록
    page.overlay.append(date_picker)

    # 선택한 날짜 표시 텍스트 컨트롤
    txt_date = ft.Text(width = 120)

    # 대화창 표시
    def pick_date(e):
        date_picker.pick_date()

    # 대화창 버튼
    date_button = ft.ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=pick_date
    )

    page.add(
        ft.Row(
            controls=[txt_date, date_button]
        )
    )


ft.app(target=main)

