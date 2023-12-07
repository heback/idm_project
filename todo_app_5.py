import flet as ft
from tasks_2 import Task
from task_input import TaskInput
from todo_db import TodoDB


def main(page: ft.Page):

    # 할 일 DB 객체
    db = TodoDB()

    # Task 컨트롤 목록을 가지는 레이아웃
    tasks = ft.Column()

    # 남은 할일 개수 표시 컨트롤
    txt_left_active = ft.Text(f'0 active item(s) left')

    # 함수 및 콜백 함수
    def add_clicked(e):
        task_inp: TaskInput = e

        if task_inp.is_new:     # 새로 입력할 때

            # 레코드 추가
            data = {'task_name': task_inp.new_task.value,
                    'task_date': task_inp.new_date.value,
                    'task_time': task_inp.new_time.value}
            db.insert_todo(data)

        else:   # 기존 할 일 수정할 때,

            # 레코드 수정
            data = {'task_name': task_inp.new_task.value,
                    'task_date': task_inp.new_date.value,
                    'task_time': task_inp.new_time.value,
                    'task_id': task_inp.task_id}
            db.update_todo(data)

        task_inp.new_task.value = ''
        task_inp.new_date.value = ''
        task_inp.new_time.value = ''
        task_inp.is_new = True
        task_inp.task_id = None
        task_inp.update()

        # todos 새로 불러 와서 Task 객체 리스트 생성
        refresh_tasks()

        # filter 적용
        update()

    def task_status_change():
        update()

    def task_delete(task):
        tasks.controls.remove(task)
        update()

    def update():

        status = filter.tabs[filter.selected_index].text
        for task in tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and not task.completed)
                or (status == "completed" and task.completed)
            )
        txt_left_active.value = (f'{get_active_todo_count()} '
                                 f'active item(s) left')
        page.update()

    def refresh_tasks():

        # 기존 Task 객체 비우기
        tasks.controls.clear()

        rows = db.get_todos()
        for row in rows:
            task = Task(
                row['task_name'],
                row['task_date'],
                row['task_time'],
                row['completed'],
                task_status_change,
                task_delete,
                task_input = task_input,
                task_id = row['id'],
                db = db
            )
            tasks.controls.append(task)

        page.update()

    def tabs_changed(e):
        update()

    def get_active_todo_count():
        count = 0
        for task in tasks.controls:
            if not task.completed:
                count += 1
        return count

    def clear_completed_tasks(e):
        for task in tasks.controls:
            if task.completed:
                tasks.controls.remove(task)
        update()

    # 할 일 입력
    task_input = TaskInput(page, add_clicked)

    # 탭
    filter = ft.Tabs(
        selected_index = 0,
        on_change = tabs_changed,
        tabs = [
            ft.Tab(text = 'all',
                   icon = ft.icons.LIST_ALT),
            ft.Tab(text = 'active',
                   icon = ft.icons.NOTIFICATIONS_ACTIVE),
            ft.Tab(text = 'completed',
                   icon = ft.icons.CHECK_BOX)
        ]
    )

    view = ft.Column(
        width=800,
        controls=[
            ft.Container(
                bgcolor = ft.colors.AMBER_50,
                padding = 10,
                content = ft.Row(
                    # alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        ft.Text(
                            'Todos',
                            expand = True,
                            text_align = ft.TextAlign.CENTER,
                            style = \
                            ft.TextThemeStyle.HEADLINE_MEDIUM
                        )
                    ]
                )
            ),
            task_input,
            ft.Container(
                margin = ft.margin.only(10, 0, 10, 0),
                content = ft.Column(
                    spacing = 25,
                    controls = [
                        filter,
                        tasks
                    ]
                )
            ),
            ft.Divider(
                thickness = 3,
                color = ft.colors.GREY_300
            ),
            ft.Container(
                margin = ft.margin.only(10, 0, 10, 0),
                content = ft.Row(
                    alignment = \
                        ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls = [
                        txt_left_active,
                        ft.ElevatedButton(
                            'Clear completed',
                            on_click = clear_completed_tasks)
                    ]
                )
            )
        ],
    )

    page.padding = 0
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.add(view)
    # Task 컨트롤 리스트 초기화
    refresh_tasks()
    # UI 새로고침
    page.update()


ft.app(target=main)

