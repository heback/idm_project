# 클래스와 객체의 개념
# 클래스는 객체를 만들어내기 위한 설계도 혹은 틀로 이해할 수 있습니다.
# 속성(attribute)과 메소드(method)를 정의함으로써 해당 클래스의 객체들이 공통적으로 가지게 될 구조와 동작을 설명합니다.
#
# 객체는 클래스에 의해 생성되며, 클래스의 인스턴스(instance)라고 합니다.
# 각 객체는 클래스에서 정의한 속성과 메소드를 가지며,
# 독립적인 상태(인스턴스 변수)를 유지할 수 있습니다.

# 클래스의 정의와 객체 생성
# 클래스를 정의하는 것은 새로운 타입을 만드는 것과 같으며, 객체는 클래스를 기반으로 생성됩니다.

# 클래스 정의
class Person:
    # 클래스 변수: 모든 인스턴스가 공유하는 변수
    species = 'Homo Sapiens'

    # 초기화 메소드: 객체가 생성될 때 초기 상태를 정의
    def __init__(self, name, age):
        # 인스턴스 변수: 각 인스턴스 고유의 변수
        self.name = name
        self.age = age

# 객체 생성
person1 = Person("김철수", 30)

# 메소드: 인스턴스 메소드, 클래스 메소드, 정적 메소드
# 인스턴스 메소드: 인스턴스 변수에 접근하거나 인스턴스 상태를 변경할 수 있는 메소드입니다.
# 클래스 메소드: @classmethod 데코레이터로 정의되며,
# 클래스 변수에 접근하거나 클래스 상태를 변경할 수 있습니다.
# 정적 메소드: @staticmethod 데코레이터로 정의되며,
# 인스턴스나 클래스 변수에 접근하지 않는, 독립적인 기능을 수행하는 메소드입니다.

class Person:
    species = 'Homo Sapiens'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 인스턴스 메소드
    def introduce(self):
        return f"내 이름은 {self.name}이고, 나이는 {self.age}살입니다."

    # 클래스 메소드
    @classmethod
    def get_species(cls):
        return cls.species

    # 정적 메소드
    @staticmethod
    def is_adult(age):
        return age >= 18

# 인스턴스 메소드 호출
person1 = Person("김철수", 30)
print(person1.introduce())

# 클래스 메소드 호출
print(Person.get_species())

# 정적 메소드 호출
print(Person.is_adult(30))

# 속성: 인스턴스 변수, 클래스 변수
# 인스턴스 변수는 각 객체가 개별적으로 가지고 있는 데이터를 위한 변수입니다.
# 클래스 변수는 클래스에 속하며, 모든 인스턴스가 공유하는 데이터를 위한 변수입니다.
#
# 상속: 기본 개념, 메소드 오버라이딩
# 상속은 한 클래스가 다른 클래스의 속성과 메소드를 물려받는 메커니즘입니다.
# 상속을 통해 기존 코드의 재사용과 확장성을 높일 수 있습니다.
# 메소드 오버라이딩은 자식 클래스에서 부모 클래스의 메소드를 재정의하는 것을 의미합니다.

# 부모 클래스
class Animal:
    def speak(self):
        raise NotImplementedError("자식 클래스에서 이 메소드를 구현해야 합니다.")

# 자식 클래스
class Dog(Animal):
    def speak(self):
        return "멍멍!"

# 자식 클래스에서 메소드 오버라이딩
dog = Dog()
print(dog.speak())  # 출력: 멍멍!

# 여기서 Dog 클래스는 Animal 클래스로부터 speak 메소드를 상속받아 오버라이딩하고 있습니다.
# 이를 통해 Dog 클래스는 자신만의 speak 메소드의 동작을 정의할 수 있습니다.

# 1. 주어진 요구 사항에 맞는 클래스 설계
# 문제:
# 은행 계좌를 모델링하는 BankAccount 클래스를 설계하세요. 이 클래스는 다음과 같은 속성을 가져야 합니다:
#
# account_number: 계좌 번호 (문자열)
# balance: 계좌 잔액 (실수형)
# owner: 계좌 소유자 이름 (문자열)
# 그리고 다음과 같은 메서드를 가져야 합니다:
#
# deposit(amount): amount 만큼 돈을 예금합니다. amount가 유효하지 않으면 (음수일 경우), 예외를 발생시킵니다.
# withdraw(amount): amount 만큼 돈을 인출합니다. 만약 잔액보다 많은 금액을 인출하려고 하면 예외를 발생시킵니다.
# get_balance(): 현재 잔액을 반환합니다.

class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("예금액은 0보다 커야 합니다.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액이 부족합니다.")
        self.balance -= amount

    def get_balance(self):
        return self.balance

# 사용 예시
account = BankAccount("123-456-789", "홍길동", 10000)
account.deposit(5000)
print(account.get_balance())
account.withdraw(3000)
print(account.get_balance())

# 2. 클래스 상속을 활용한 문제
# 문제:
# 위에서 정의한 BankAccount 클래스를 상속받아 MinimumBalanceAccount라는 새로운 클래스를 만드세요.
# 이 새로운 클래스는 최소 잔액(minimum_balance)을 유지해야 하며,
# withdraw 메서드를 오버라이드하여 최소 잔액 이하로 내려가지 않게 합니다.

class MinimumBalanceAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0.0, minimum_balance=0.0):
        super().__init__(account_number, owner, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            raise ValueError("최소 잔액보다 낮을 수 없습니다.")
        super().withdraw(amount)

# 사용 예시
min_account = MinimumBalanceAccount("987-654-321", "이순신", 10000, 2000)
min_account.withdraw(8000)
print(min_account.get_balance())
try:
    min_account.withdraw(6000)
except ValueError as e:
    print(e)

# 3. 클래스와 객체의 속성을 조작하는 문제
# 문제:
# 주어진 Car 클래스가 있습니다. 이 클래스는 초기에 fuel_level 속성만 가지고 있습니다.
# fuel_level의 값을 변경하는 add_fuel 메서드와 현재 연료 레벨을 반환하는 get_fuel_level 메서드를 추가하세요.
# 또한, 연료가 특정 수준(10 이하)으로 떨어지면 경고 메시지를 출력하는 로직을 추가하세요.

class Car:
    def __init__(self, fuel_level):
        self.fuel_level = fuel_level

    def add_fuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100

    def get_fuel_level(self):
        if self.fuel_level <= 10:
            print("경고: 연료가 거의 다 되었습니다!")
        return self.fuel_level

# 사용 예시
car = Car(50)
print(car.get_fuel_level())
car.add_fuel(30)
print(car.get_fuel_level())
car.add_fuel(30)  # 100을 초과하여도 연료 레벨은 100으로 유지
print(car.get_fuel_level())
car.add_fuel(-70)
print(car.get_fuel_level())  # 연료가 10 이하로 떨어져 경고 메시지 출력
