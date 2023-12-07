import sqlite3


class TodoDB:

    def __init__(self):

        # DB 연결, 파일이 없으면 새로 생성
        self.conn = sqlite3.connect('todo.db',
                                    check_same_thread = False)

        # 결과 처리할 때 속성 이름 사용 설정
        self.conn.row_factory = sqlite3.Row

        # 커서 객체 생성
        self.cursor = self.conn.cursor()

        # 테이블 생성(없다면, 있으면 패스)
        self.db_create()

    # 테이블 생성
    def db_create(self):

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            task_date TEXT,
            task_time TEXT,
            completed INTEGER default 0,
            createdAt TEXT default CURRENT_DATE,
            modifiedAt TEXT default CURRENT_DATE
        )
        ''')

        # 변경 사항 저장
        self.conn.commit()

    def insert_testdata(self):
        # 데이터 삽입 SQL 쿼리
        self.cursor.execute(
            "INSERT INTO todos (task_name, task_date, task_time) "
            "VALUES ('할 일 테스트 1', '2023-12-06', '10:00')"
        )
        self.cursor.execute(
            "INSERT INTO todos (task_name, task_date, task_time) "
            "VALUES ('할 일 테스트 2', '2023-12-07', '10:00')"
        )
        self.cursor.execute(
            "INSERT INTO todos (task_name, task_date, task_time) "
            "VALUES ('할 일 테스트 3', '2023-12-07', '10:00')"
        )
        # 변경 사항 저장
        self.conn.commit()

    def insert_todo(self, data):
        self.cursor.execute(
            f'''
            INSERT INTO todos (task_name, task_date, task_time) 
            VALUES (
            '{data["task_name"]}', 
            '{data["task_date"]}', 
            '{data["task_time"]}'
            )
            '''
        )
        self.conn.commit()
        return self.cursor.lastrowid

    # 할일 모두 가져 오기
    def get_todos(self):

        self.cursor.execute(
            "SELECT * FROM todos ORDER BY modifiedAt DESC"
        )
        return self.cursor.fetchall()

    # 할일 수정 하기
    def update_todo(self, data):

        # data 는 딕셔너리 형식
        self.cursor.execute(f'''
            UPDATE todos SET 
                task_name='{data["task_name"]}',
                task_date='{data["task_date"]}',
                task_time='{data["task_time"]}',
                modifiedAt=CURRENT_DATE 
            WHERE id={data["task_id"]}
        ''')
        self.conn.commit()

    # 상태 수정 하기
    def update_status(self, data):
        # data 는 딕셔너리 형식
        self.cursor.execute(
            f'''
            UPDATE todos SET 
                completed='{data["completed"]}',
                modifiedAt=CURRENT_DATE 
            WHERE id={data["task_id"]}
        '''
            )
        self.conn.commit()

    # 할 일 삭제 하기
    def delete_todo(self, todo_id):
        self.cursor.execute(
            f'''
            DELETE FROM todos WHERE id={todo_id}
            '''
        )
        self.conn.commit()

    # 완료된 할 일 모두 삭제 하기
    def delete_completed_todos(self):
        self.cursor.execute(
            f'''
            DELETE FROM todos WHERE isCompleted=1
            '''
        )
        self.conn.commit()

