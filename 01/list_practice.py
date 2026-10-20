# 1. 리스트 기본 개념 및 활용

items = ["검", "방패", "물약"]

print(items)

print(items[0])
print(items[1])
print(items[2])

items[0] = "마법 지팡이"
print(items)

for item in items:
    print(item)

if "물약" in items:
    print("물약을 가지고 있습니다!")
else:
    print("물약이 없습니다!")


# 2. RPG 게임 - 인벤토리 관리

items = ["검", "방패", "물약"]

items.append("활")
items[0] = "마법 검"
items.remove("물약")

print("현재 인벤토리:", items)
print("아이템 개수:", len(items))


# 3. 몬스터 도감 - 보스 몬스터 찾기

monsters = ["슬라임", "고블린", "드래곤", "해골"]

for monster in monsters:
    print(monster)

if "드래곤" in monsters:
    print("보스 몬스터 발견!")