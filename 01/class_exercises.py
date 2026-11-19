# Hero 클래스를 정의합니다.
class Hero:

    # 캐릭터의 이름과 체력을 설정합니다.
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    # 캐릭터의 정보를 출력합니다.
    def show_info(self):
        print("이름:", self.name)
        print("체력:", self.hp)

    # 캐릭터의 체력을 회복합니다.
    def heal(self, amount):
        self.hp += amount

    # 캐릭터의 체력을 감소시킵니다.
    def take_damage(self, damage):
        self.hp -= damage

        # 체력이 0 이하라면 0으로 변경하고 메시지를 출력합니다.
        if self.hp <= 0:
            self.hp = 0
            print("캐릭터가 쓰러졌습니다!")


# 캐릭터 객체를 생성합니다.
hero = Hero("기사", 100)

# 캐릭터의 정보를 출력합니다.
hero.show_info()

# 캐릭터의 체력을 20 회복합니다.
hero.heal(20)

# 캐릭터의 체력을 30 감소시킵니다.
hero.take_damage(30)

# 변경된 정보를 출력합니다.
hero.show_info()
