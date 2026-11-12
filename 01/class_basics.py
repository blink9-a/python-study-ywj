
# 1. 기본 생성자를 활용한 클래스

# Hero03 클래스를 정의합니다.
class Hero03:

    # 객체가 생성될 때 초기 정보를 설정합니다.
    def __init__(self):
        self.name = "기사"
        self.hp = 100


# Hero03 객체를 생성합니다.
c03_hero = Hero03()

# 객체에 저장된 이름을 출력합니다.
print(c03_hero.name)

# 객체에 저장된 체력을 출력합니다.
print(c03_hero.hp)


# 2. 매개변수를 활용한 생성자

# Hero04 클래스를 정의합니다.
class Hero04:

    # 전달받은 이름과 체력을 객체에 저장합니다.
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

        # 마나의 초기값을 설정합니다.
        self.mp = 50


# 기사 객체를 생성합니다.
c04_hero1 = Hero04("기사", 100)

# 마법사 객체를 생성합니다.
c04_hero2 = Hero04("마법사", 80)

# 두 객체의 정보를 출력합니다.
print(c04_hero1.name, c04_hero1.hp)
print(c04_hero2.name, c04_hero2.hp)


# 3. 객체의 속성 추가 및 변경

# 기사 객체의 이름과 체력을 변경합니다.
c04_hero1.name = "전사"
c04_hero1.hp = 120

# 변경된 정보를 출력합니다.
print(c04_hero1.name, c04_hero1.hp)

# 두 객체의 마나를 출력합니다.
print(c04_hero1.mp)
print(c04_hero2.mp)


# 4. 메서드 기본 개념

# Hero05 클래스를 정의합니다.
class Hero05:

    # 캐릭터의 이름을 설정합니다.
    def __init__(self, name):
        self.name = name

    # 캐릭터가 인사하는 메서드를 정의합니다.
    def introduce(self):
        print("안녕하세요! 저는", self.name, "입니다.")


# 기사 객체를 생성합니다.
c05_hero = Hero05("기사")

# 객체의 introduce 메서드를 호출합니다.
c05_hero.introduce()
