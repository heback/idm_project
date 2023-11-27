# 차시 1: 파이선 기본

# 변수와 기본 자료형

# 변수 할당
x = 10          # 정수
y = 20.5        # 실수

x: int = 10     # 타입 힌트
y: float = 20.5

name: str = "Alice"  # 문자열

# 출력
print(x)
print(y)
print(name)

# 연산자

# 산술 연산자
a = 10
b = 3
print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a / b)  # 나눗셈
print(a % b)  # 나머지
print(a ** b) # 거듭제곱

# 비교 연산자
print(a == b)  # 같다
print(a != b)  # 다르다
print(a > b)   # 크다
print(a < b)   # 작다

# 입력과 출력

# 사용자 입력 받기
user_input = input("당신의 이름은 무엇인가요? ")
print("안녕하세요,", user_input)

# 리스트

# 리스트 생성 및 접근
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # 첫 번째 요소
print(my_list[-1]) # 마지막 요소

# 리스트 수정
my_list[1] = 10

# 리스트에 요소 추가
my_list.append(6)


# 튜플

# 튜플 생성
my_tuple = (1, 2, 3)

# 튜플은 수정할 수 없음
# my_tuple[1] = 10  # 이 코드는 에러를 발생시킴

# 딕셔너리

# 딕셔너리 생성 및 접근
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
print(my_dict['apple'])  # 'apple'의 값을 출력

# 딕셔너리에 새로운 키-값 쌍 추가
my_dict['grape'] = 10

# 집합

# 집합 생성
my_set = {1, 2, 3, 4, 5}

# 집합에 요소 추가
my_set.add(6)

# 요소가 집합에 있는지 확인
print(1 in my_set)  # True

# 집합 연산
another_set = {4, 5, 6, 7}
print(my_set.union(another_set))        # 합집합
print(my_set.intersection(another_set)) # 교집합
print(my_set.difference(another_set))   # 차집합

# 제어구조

# 조건문 (if, elif, else)
# 조건문은 주어진 조건의 참, 거짓에 따라 코드의 실행 흐름을 제어합니다.

# 단순 if 문
age = 18
if age >= 18:
    print("성인입니다.")

# if-else 문
age = 16
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# if-elif-else 문
score = 85
if score >= 90:
    print("A등급입니다.")
elif score >= 80:
    print("B등급입니다.")
elif score >= 70:
    print("C등급입니다.")
else:
    print("D등급입니다.")

# 중첩된 if 문
age = 20
has_license = True
if age >= 18:
    if has_license:
        print("운전할 수 있습니다.")
    else:
        print("운전면허가 필요합니다.")
else:
    print("운전할 수 없습니다.")

# 반복문 (for, while)
# 반복문은 지정된 조건이 만족되는 동안 코드 블록을 반복해서 실행합니다.

# for 문을 이용한 반복
for i in range(5): # 0부터 4까지 반복
    print(i)

# while 문을 이용한 반복
count = 0
while count < 5:
    print(count)
    count += 1

# for 문과 if 문의 조합
for number in range(10):
    if number % 2 == 0:
        print(f"{number}는 짝수입니다.")
    else:
        print(f"{number}는 홀수입니다.")

# for 문을 이용한 리스트의 요소 접근
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}.")

# while 문으로 조건이 False가 될 때까지 반복
number = 0
while number < 5:
    print(number)
    number += 1
else:
    print("반복이 종료되었습니다.")

# 리스트 컴프리헨션
# 리스트 컴프리헨션은 리스트 내에 for 문과 if 문을 함께 사용하여 리스트를 생성하는 간결한 방법입니다.

# 기본 리스트 컴프리헨션
squares = [x**2 for x in range(10)] # 0부터 9까지 숫자의 제곱으로 리스트 생성
print(squares)

# 조건을 포함한 리스트 컴프리헨션
even_squares = [x**2 for x in range(10) if x % 2 == 0] # 짝수의 제곱만 리스트 생성
print(even_squares)

# 중첩된 for 문을 이용한 리스트 컴프리헨션
flat_list = [item for sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]] for item in sublist]
print(flat_list)

# if-else 문을 포함한 리스트 컴프리헨션
grades = [85, 92, 78, 90, 100]
grade_letters = ["A" if score >= 90 else "B" if score >= 80 else "C" for score in grades]
print(grade_letters)

# 문제 1: 사용자 데이터 입력 및 처리
# 사용자로부터 이름, 나이, 그리고 좋아하는 색상을 입력 받습니다.
# 이 데이터를 딕셔너리에 저장한 후, 사용자가 입력한 나이가 18세 이상이면 "성인입니다."라고 출력하고,
# 18세 미만이면 "미성년자입니다."라고 출력하는 프로그램을 작성하세요.

# 사용자 데이터 입력
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
color = input("좋아하는 색상을 입력하세요: ")

# 데이터 딕셔너리에 저장
user_info = {
    '이름': name,
    '나이': age,
    '좋아하는 색상': color
}

# 나이에 따른 출력
if user_info['나이'] >= 18:
    print(f"{user_info['이름']}님은 성인입니다.")
else:
    print(f"{user_info['이름']}님은 미성년자입니다.")


# 문제 2: 다양한 자료형의 조합
# 한 반에 학생들의 정보를 저장하는 프로그램을 작성하세요.
# 학생의 정보는 학생의 이름, 성적 리스트(국어, 수학, 영어),
# 그리고 출석 여부를 포함합니다.
# 이름은 문자열, 성적은 리스트, 출석 여부는 불린 값으로 표현합니다.
# 이 정보를 리스트에 모든 학생들의 정보를 포함하여 저장하세요.
# 그리고 특정 학생의 모든 정보를 출력하는 기능을 구현하세요.

# 학생 데이터 리스트
students_info = []

# 데이터 입력 예시
students_info.append(('지민', [90, 80, 70], True))
students_info.append(('태형', [85, 75, 95], False))

# 특정 학생 정보 출력 함수
def print_student_info(name):
    for student in students_info:
        if student[0] == name:
            print(f"이름: {student[0]}, 성적: {student[1]}, 출석: {'출석' if student[2] else '결석'}")
            break
    else:
        print("해당 학생을 찾을 수 없습니다.")

# 함수 호출 예시
print_student_info('지민')

# 문제 3: 기본 제어 구조를 사용한 알고리즘 문제
# 정수를 입력받아서 그 정수가 소수(prime number)인지 아닌지를 판별하는 프로그램을 작성하세요.
# 소수는 1과 자기 자신으로만 나누어지는 1보다 큰 정수를 말합니다.

# 소수 판별 함수
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# 사용자로부터 정수 입력 받기
num = int(input("정수를 입력하세요: "))

# 소수 여부 출력
if is_prime(num):
    print(f"{num}은(는) 소수입니다.")
else:
    print(f"{num}은(는) 소수가 아닙니다.")
