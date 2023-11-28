# 차시 2: 파이선 함수

# 간단한 함수의 선언과 호출 예제
# 함수 선언은 def 키워드를 사용하여 수행하며, 이후 함수를 호출하여 실행할 수 있습니다.

# 간단한 인사말을 출력하는 함수
def greet():
    print("안녕하세요!")


# 함수 호출
greet()


# 매개변수와 결과를 반환하는 함수
def greet(name):
    return f"안녕, {name}!"

print(greet("철수"))


# 매개변수가 다양한 함수 예제
# 함수는 여러 매개변수를 가질 수 있으며, 이는 필수 매개변수, 기본값을 가진 매개변수, 가변 매개변수 등이 될 수 있습니다.

# 세 개의 매개변수를 받아서 각각을 처리하는 함수
def introduce(name, age=0, *interests):
    print(f"이름: {name}")
    if age > 0:
        print(f"나이: {age}")
    print("관심사:")
    for interest in interests:
        print(f"- {interest}")

# 함수 호출
introduce("지민", 25, "축구", "음악", "여행")
# 이 예제에서 name은 필수 매개변수, age는 기본값이 있는 선택적 매개변수,
# 그리고 interests는 가변 매개변수로, 여러 개의 인자를 튜플로 받아 처리합니다.


# 키워드 매개변수
def describe_pet(animal_type, pet_name):
    return f"나의 {animal_type}의 이름은 {pet_name}입니다."

# 함수를 호출할 때 매개변수의 이름을 명시적으로 지정할 수 있습니다.
# 이를 통해 매개변수의 순서를 바꿀 수 있습니다.
print(describe_pet(animal_type="햄스터", pet_name="해리"))
print(describe_pet(pet_name="해리", animal_type="햄스터"))


# **키워드 가변 매개변수 (kwargs):
# **kwargs를 사용하면 함수가 임의의 수의 키워드 매개변수를 받을 수 있습니다.
def build_profile(**user_info):
    return user_info


user_profile = build_profile(name="철수", age=30, city="서울")
print(user_profile)  # {'name': '철수', 'age': 30, 'city': '서울'}


# lambda를 사용한 간단한 연산 예제
# lambda 함수는 이름 없이 간단한 함수를 한 줄로 표현할 수 있게 해주는 파이썬의 기능입니다.

# 두 수를 더하는 lambda 함수
add = lambda x, y: x + y

# 람다 함수 호출
result = add(10, 20)
print(result)  # 출력: 30

# 리스트 정렬을 위한 lambda 함수 예제
names = ['김철수', '박지민', '이태형', '정호석']
sorted_names = sorted(names, key=lambda name: len(name))

print(sorted_names)  # 이름의 길이에 따라 정렬된 리스트를 출력합니다.
# 위의 예제에서 첫 번째 lambda는 두 개의 매개변수를 받아서 더한 결과를 반환하고,
# 두 번째 예제에서는 sorted 함수의 key 매개변수에 lambda 함수를 사용하여 리스트의 각 요소(이름)를 길이에 따라 정렬합니다.

# map 함수와 함께 사용
# 리스트의 각 요소에 연산을 적용할 때 lambda 함수를 map 함수와 함께 사용할 수 있습니다.
# 각 숫자의 제곱을 계산하는 예제
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)

print(list(squared))  # 출력: [1, 4, 9, 16, 25]

# filter 함수와 함께 사용
# 특정 조건에 맞는 요소만 필터링할 때 lambda 함수를 filter 함수와 함께 사용할 수 있습니다.

# 짝수만 필터링하는 예제
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))  # 출력: [2, 4, 6]

# 정렬 기준 설정
# 객체의 리스트를 특정 속성으로 정렬할 때 lambda 함수를 사용할 수 있습니다.
# 이름에 따라 사용자를 정렬하는 예제
users = [{'name': '홍길동', 'age': 50}, {'name': '김철수', 'age': 30}, {'name': '이영희', 'age': 40}]
sorted_users = sorted(users, key=lambda user: user['name'])

print(sorted_users)  # 출력: 이름 순으로 정렬된 사용자 리스트

# 즉시 실행 함수
# lambda 함수를 정의하자마자 실행하는 즉시 실행 함수(IIFE, Immediately Invoked Function Expression) 패턴을 사용할 수 있습니다.
# 즉시 실행되는 lambda 함수
result = (lambda x, y: x + y)( 5, 3)  # x와 y를 더하고 결과를 튜플로 반환

print(result)  # 출력: 8

# 연습 문제 1: 다양한 유형의 매개변수를 가진 함수 작성
# 주어진 사람의 정보를 처리하는 함수 process_person_info를 작성하세요. 이 함수는 다음 매개변수를 가져야 합니다:
#
# name: 필수 문자열 매개변수로 사람의 이름입니다.
# age: 선택적 정수 매개변수로 기본값은 None입니다.
# **kwargs: 사람의 추가 정보를 처리할 수 있는 가변 키워드 인자입니다.
# 함수는 다음과 같은 문자열을 반환해야 합니다:
#
# "Name: [name], Age: [age], Details: [details]"
# 여기서 [name]은 전달된 이름, [age]는 전달된 나이(나이가 없으면 'Unknown'),
# [details]는 kwargs에 전달된 추가 정보의 키와 값을 포함하는 문자열입니다.
# 추가 정보가 없으면 'None'이 출력되어야 합니다.

def process_person_info(name, age=None, **kwargs):
    age_str = 'Unknown' if age is None else age
    details_str = ', '.join(f"{key}={value}" for key, value in kwargs.items()) if kwargs else 'None'
    return f"Name: {name}, Age: {age_str}, Details: {details_str}"

# 함수 사용 예제
print(process_person_info("김철수", 30, height=180, location="서울"))

# 연습 문제 2: lambda 함수를 활용한 데이터 처리
#
# 리스트 data에는 각각의 튜플로 이루어진 여러 사람들의 이름과 나이가 포함되어 있습니다.
# lambda 함수와 filter 함수를 사용하여 20세 이상의 사람들만을 필터링하는 코드를 작성하세요.

data = [("지민", 25), ("태형", 23), ("유나", 19), ("정국", 22)]

# 20세 이상인 사람들을 필터링하는 lambda 함수
filtered_data = filter(lambda x: x[1] >= 20, data)

# 결과를 리스트로 변환하여 출력
filtered_list = list(filtered_data)
print(filtered_list)  # 출력: [('지민', 25), ('태형', 23), ('정국', 22)]

