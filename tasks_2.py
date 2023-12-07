import flet as ft
from task_input import TaskInput


class Task(ft.UserControl):

    def __init__(self,
                 task_name,
                 task_date,
                 task_time,
                 completed,
                 task_status_change,
                 task_delete,
                 task_input: TaskInput = None,
                 task_id = None,
                 db = None):
        super().__init__()
        # 컨트롤들
        self.display_view = None
        self.display_task = ft.Row()
        # 상태
        self.completed = completed
        # 할일
        self.task_name = task_name
        # 날짜
        self.task_date = task_date
        # 시각
        self.task_time = task_time
        # 상태 변경 콜백
        self.task_status_change = task_status_change
        # 삭제 콜백
        self.task_delete = task_delete
        # 입력 폼 객체
        self.task_input = task_input
        # DB와 호환을 위함
        self.task_id = task_id
        # DB 객체
        self.db = db

        # 텍스트 스타일 동적 적용을 위한 사전 정의
        self.text_style_cancel = ft.TextStyle(
            color = ft.colors.GREY,
            decoration = ft.TextDecoration.LINE_THROUGH
        )
        self.text_style_normal = ft.TextStyle(
            decoration = ft.TextDecoration.NONE
        )

    def build(self):

        self.display_task = ft.Row(
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            controls = [
                ft.Checkbox(
                    value=bool(self.completed),
                    on_change=self.status_changed
                ),
                ft.Text(width = 400, spans = [
                    ft.TextSpan(
                        self.task_name,
                        # 초기 상태에 따라 다른 스타일 적용
                        style = self.text_style_cancel \
                            if bool(self.completed) \
                            else self.text_style_normal
                    )
                ]),
                ft.Icon(ft.icons.ALARM),
                ft.Text(width = 200, spans = [
                    ft.TextSpan(self.task_date),
                    ft.TextSpan(' '),
                    ft.TextSpan(self.task_time)
                ]),
            ]
        )

        self.display_view = ft.Row(
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        return ft.Column(
            controls=[self.display_view]
        )

    # Task 객체의 edit 버튼 클릭 하였을 경우
    # TaskInput 객체로 Task 객체를 넘김
    def edit_clicked(self, e):
        self.task_input.set_update_data(self)

    # 완료된 할 일은 취소선 과 글자색 을 회색 으로 변경
    def status_changed(self, e):

        self.completed = self.display_task.controls[0].value
        if not self.completed:
            self.display_task.controls[1].spans[0].style = \
                self.text_style_normal
        else:
            self.display_task.controls[1].spans[0].style = \
                self.text_style_cancel

        # DB 반영
        data = {'task_id': self.task_id,
                'completed': self.completed}
        self.db.update_status(data)

        self.task_status_change()
        self.update()

    # 할일 내용과 날짜/시간 수정 시 화면을 갱신 하기 위한 메서드
    def ui_update(self):
        self.display_task.controls[1].spans[0].text = \
            self.task_name
        self.display_task.controls[3].spans[0].text = \
            self.task_date
        self.display_task.controls[3].spans[2].text = \
            self.task_time
        self.update()

    def delete_clicked(self, e):
        self.db.delete_todo(self.task_id)
        self.task_delete(self)

