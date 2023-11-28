# 객체지향 프로그래밍(OOP)의 기본 원리

# 캡슐화(Encapsulation): 객체의 데이터를 외부에서 직접 접근하지 못하도록 숨기고,
# 해당 데이터를 조작할 수 있는 메서드를 제공하는 것입니다.
# 이를 통해 객체 내부의 구현을 숨기고 외부 인터페이스만을 제공하여 객체 간의 상호작용을 단순화합니다.

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.__account_number = account_number  # 캡슐화를 위해 속성을 비공개(private)로 선언
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


# 상속(Inheritance): 한 클래스가 다른 클래스의 속성과 메소드를 상속받아 사용할 수 있게 하는 것입니다.
# 코드의 재사용성을 높여주고, 클래스 간의 관계를 설정하는데 도움을 줍니다.

class SavingAccount(BankAccount):  # BankAccount로부터 상속
    def __init__(self, account_number, owner, balance=0):
        super().__init__(account_number, owner, balance)

# 다형성(Polymorphism): 동일한 인터페이스나 메서드 호출이 서로 다른 클래스의 객체들에 대해 다른 동작을 할 수 있도록 하는 원리입니다.
# 메서드 오버라이딩이나 오버로딩을 통해 구현됩니다.

class CheckingAccount(BankAccount):
    def withdraw(self, amount):  # 메소드 오버라이딩
        if self.get_balance() >= amount:
            print("Checking account withdrawal")
            super().deposit(-amount)

# 추상화(Abstraction): 복잡한 내부 구현을 숨기고,
# 필요한 부분만을 간략화하여 표현하는 것입니다.
# 추상 클래스와 인터페이스를 통해 구현할 수 있습니다.

from abc import ABC, abstractmethod

class Account(ABC):  # 추상 클래스
    @abstractmethod
    def account_type(self):
        pass

class DepositAccount(Account):  # 구체적인 클래스
    def account_type(self):
        print("Deposit Account")

# 2. 생성자와 소멸자
# 생성자(Constructor): 객체가 생성될 때 자동으로 호출되는 특수 메소드로,
# 객체의 초기화를 담당합니다.
# Python에서는 __init__이 이에 해당합니다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 소멸자(Destructor): 객체가 소멸될 때 자동으로 호출되는 메소드로,
# 필요한 정리 작업을 수행합니다.
# Python에서는 __del__이 이에 해당합니다.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{self.name} 객체가 소멸됩니다.")

# 3. 특수 메소드
# __str__: 객체를 문자열로 표현할 때 사용되는 메소드로,
# print() 함수에 객체를 넘겼을 때 어떻게 출력될지 정의합니다.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person({self.name}, {self.age})"

# __repr__: 객체의 '공식적인' 문자열 표현을 위한 메소드로,
# 주로 개발자가 해당 객체를 어떻게 만들었는지를 보여주는 데 사용됩니다.
# 인터프리터에서 객체를 입력하면 이 메소드가 호출됩니다.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

# 4. 접근 제어자
# 파이썬에서 접근 제어자는 변수명 앞에 밑줄을 사용함으로써 구현됩니다. 여기에는 세 가지 주요한 형태가 있습니다:
#
# Public 멤버: 어디서든 접근이 가능합니다. 파이썬에서는 기본적으로 모든 클래스 멤버가 public입니다.
# Protected 멤버: 앞에 하나의 언더스코어 (_)를 붙여 표현하며,
# 이는 해당 멤버가 서브 클래스에 의해서만 접근되어야 함을 나타냅니다.
# 하지만 파이썬은 강제적이지 않아서 여전히 외부에서 접근할 수 있습니다.
# Private 멤버: 앞에 두 개의 언더스코어 (__)를 붙여 표현합니다.
# 이는 클래스 외부에서는 접근할 수 없음을 나타냅니다.
# 파이썬은 이를 강제하기 위해 이름 변경(name mangling)을 사용합니다.
# 클래스 내부에서는 이러한 변수에 접근할 수 있지만,
# 외부에서는 _ClassName__variableName의 형태로 접근해야 합니다.

class Car:
    def __init__(self, make, model):
        self.make = make        # Public 속성
        self._model = model     # Protected 속성
        self.__engine_type = "V8"  # Private 속성

    def drive(self):
        return f"This {self.make} {self._model} with a {self.__engine_type} engine is driving."

    def __private_method(self):
        return "This is a private method."

    def _protected_method(self):
        return "This is a protected method."

    def public_method(self):
        return "This is a public method."

# 객체 생성
car = Car("Toyota", "Supra")

# Public 속성과 메서드에 접근
print(car.make)            # "Toyota"
print(car.drive())         # "This Toyota Supra with a V8 engine is driving."
print(car.public_method()) # "This is a public method."

# Protected 속성과 메서드에 접근
# 이는 권장되지 않지만, 파이썬에서는 기술적으로 가능합니다.
print(car._model)             # "Supra"
print(car._protected_method()) # "This is a protected method."

# Private 속성과 메서드에 접근
# 이 코드는 오류를 발생시킵니다.
# print(car.__engine_type)      # AttributeError
# print(car.__private_method()) # AttributeError

# 이름 변경을 통한 private 속성에 접근
# 이것은 파이썬의 private 멤버를 우회하는 방법입니다.
# 하지만 일반적으로 좋은 방법은 아니며, private 멤버를 이런 식으로 사용하는 것을 피해야 합니다.
print(car._Car__engine_type)      # "V8"
print(car._Car__private_method()) # "This is a private method."

# 5. OOP 디자인 패턴
# 싱글턴(Singleton) 패턴: 클래스의 인스턴스가 하나만 생성되도록 제한하는 패턴입니다.
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

# 팩토리(Factory) 패턴: 객체 생성을 서브클래스에게 맡기는 패턴으로,
# 클라이언트 코드에서는 어떤 서브클래스의 인스턴스를 생성할지 몰라도 됩니다.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def get_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None

# 옵저버(Observer) 패턴: 객체의 상태 변화를 관찰하는 관찰자들에게 자동으로 알림을 보내는 패턴입니다.
class Subject:
    def __init__(self):
        self.__observers = []

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, message):
        for observer in self.__observers:
            observer.notify(message)

class Observer:
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f"{self.name} received message: {message}")

subject = Subject()
observer_a = Observer("Observer A")
subject.register_observer(observer_a)
subject.notify_observers("Hello!")
