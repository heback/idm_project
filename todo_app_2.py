import flet as ft
from tasks import Task


def main(page: ft.Page):

    # Task 컨트롤 목록을 가지는 레이아웃
    tasks = ft.Column()

    # 남은 할일 개수 표시 컨트롤
    txt_left_active = ft.Text(f'0 active item(s) left')

    # 할일
    new_task = ft.TextField(
                        hint_text = "Whats needs to be done?",
                        expand = True
                    )

    # 함수 및 콜백 함수
    def add_clicked(e):
        task = Task(
            new_task.value,
            task_status_change,
            task_delete)
        tasks.controls.append(task)
        new_task.value = ""
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

    # 탭
    filter = ft.Tabs(
        selected_index = 0,
        on_change = tabs_changed,
        tabs = [
            ft.Tab(text = 'all'),
            ft.Tab(text = 'active'),
            ft.Tab(text = 'completed')
        ]
    )

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
                    new_task,
                    ft.FloatingActionButton(
                        icon = ft.icons.ADD,
                        on_click=add_clicked)
                ]
            ),
            ft.Column(
                spacing = 25,
                controls = [
                    filter,
                    tasks
                ]
            ),
            ft.Row(
                controls = [
                    txt_left_active,
                    ft.ElevatedButton(
                        'Clear completed',
                        on_click = clear_completed_tasks)
                ]
            )
        ],
    )

    page.horizontal_alignment = "center"
    page.add(view)
    page.update()


ft.app(target=main)


