import flet as ft
from datetime import datetime


class TaskInput(ft.UserControl):

    def __init__(self, page, add_click):

        super().__init__()

        # 새로 입력 여부
        self.is_new = True

        # 할 일 레코드 인덱스
        self.task_id = None

        # todo_app main 에 정의된 메서드
        self.add_click = add_click

        # 올해
        self.this_year = datetime.now().year

        # 이번 달
        self.this_month = datetime.now().month

        # 오늘
        self.this_date = datetime.now().day

        # 할일
        self.new_task = ft.TextField(
            hint_text = "Whats needs to be done?",
            expand = True
        )
        # 날짜
        self.new_date = ft.TextField(
            width = 120,
            hint_text = "Date",
            read_only = True
        )
        # 시간
        self.new_time = ft.TextField(
            width = 80,
            hint_text = "Time",
            read_only = True
        )

        # DatePicker 생성
        self.date_picker = ft.DatePicker(
            # OK
            on_change = self.change_date,
            # Cancel
            on_dismiss = self.date_picker_dismissed,
            # 달력 표시 시작 날짜
            first_date = datetime(1970, 1, 1),
            # 달력 표시 마지막 날짜
            last_date = datetime(
                self.this_year + 1, 12, 31),
            current_date = datetime(
                self.this_year,
                self.this_month,
                self.this_date
            ),
            # 날짜 입력 방법 모드
            date_picker_entry_mode = \
                ft.DatePickerEntryMode.CALENDAR_ONLY
        )

        # TimePicker 생성
        self.time_picker = ft.TimePicker(
            # OK
            on_change = self.change_time,
            # Cancel
            on_dismiss = self.time_picker_dismissed,
        )

        # 모달 대화창에 등록
        page.overlay.append(self.date_picker)
        page.overlay.append(self.time_picker)

    # date_picker 에서 날짜를 선택 하고 OK 클릭 하면
    def change_date(self, e):
        self.new_date.value = \
            self.date_picker.value.date().\
                strftime('%Y-%m-%d')
        self.update()

    # date_picker 에서 cancel 클릭 하면
    def date_picker_dismissed(self, e):
        print(f"Date picker dismissed, value is")
        print(f"{self.date_picker.value}")

    # time_picker 에서 날짜를 선택 하고 OK 클릭 하면
    def change_time(self, e):
        self.new_time.value = \
            self.time_picker.value.strftime('%H:%M')
        self.update()

    # time_picker 에서 cancel 클릭 하면
    def time_picker_dismissed(self, e):
        print(f"Date picker dismissed, value is")
        print(f"{self.time_picker.value}")

    # 수정 데이터 입력
    # Task 객체와 연동 하기 위한 메서드
    def set_update_data(self, task):
        self.new_task.value = task.task_name
        self.new_date.value = task.task_date
        self.new_time.value = task.task_time
        self.task_id = task.task_id
        self.is_new = False
        self.data = task
        self.update()

    def add_clicked(self, e):
        self.add_click(self)

    def build(self):

        return ft.Container(
            padding = 10,
            margin = ft.margin.only(10, 0, 10, 0),
            border = ft.border.all(3, ft.colors.GREY_300),
            border_radius = ft.border_radius.all(10),
            content = ft.Row(
                controls = [
                    self.new_task,
                    self.new_date,
                    ft.IconButton(
                        icon = ft.icons.CALENDAR_TODAY,
                        on_click = lambda _:
                        self.date_picker.pick_date()),
                    self.new_time,
                    ft.IconButton(
                        icon = ft.icons.TIMER,
                        on_click = lambda _:
                        self.time_picker.pick_time()),
                    ft.FloatingActionButton(
                        icon = ft.icons.ADD,
                        on_click = self.add_clicked
                    )
                ]
            )
        )

