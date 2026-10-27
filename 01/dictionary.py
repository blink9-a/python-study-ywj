
# 캐릭터의 정보를 딕셔너리로 저장합니다.
mage = {
    "name": "마법사",
    "level": 10,
    "hp": 80
}

# 딕셔너리 전체를 출력합니다.
print(mage)

# 아무 값도 없는 딕셔너리를 만듭니다.
empty = {}

# 빈 딕셔너리를 출력합니다.
print(empty)


# 캐릭터의 정보를 저장합니다.
player = {
    "name": "기사",
    "level": 5,
    "hp": 100
}

# 각 키에 연결된 값을 가져옵니다.
print(player["name"])
print(player["level"])
print(player["hp"])


# 캐릭터의 정보를 저장합니다.
player_add = {
    "name": "기사",
    "level": 5
}

# 새로운 키와 값을 추가합니다.
player_add["hp"] = 100

# 또 다른 키와 값을 추가합니다.
player_add["gold"] = 50

# 추가된 정보를 출력합니다.
print(player_add)


# 캐릭터의 정보를 저장합니다.
player_update = {
    "name": "기사",
    "level": 5,
    "hp": 100
}

# 캐릭터의 레벨을 변경합니다.
player_update["level"] = 6

# 공격을 받아 체력이 20 감소합니다.
player_update["hp"] -= 20

# 변경된 정보를 출력합니다.
print(player_update)


# 캐릭터의 정보를 저장합니다.
player_delete = {
    "name": "기사",
    "level": 5,
    "hp": 100,
    "gold": 50
}

# gold 키와 연결된 값을 삭제합니다.
del player_delete["gold"]

# 남아 있는 정보를 출력합니다.
print(player_delete)

# 저장된 키와 값의 쌍 개수를 출력합니다.
print(len(player_delete))


# 상점의 아이템과 가격을 저장합니다.
shop = {
    "검": 100,
    "방패": 150,
    "물약": 50
}

# 반복문을 사용하여 키와 값을 함께 출력합니다.
for item, price in shop.items():
    print(item, price)


# 체력 정보가 있는 캐릭터를 저장합니다.
player1 = {
    "name": "기사",
    "level": 5,
    "hp": 100
}

# 체력 정보가 없는 캐릭터를 저장합니다.
player2 = {
    "name": "기사",
    "level": 5
}

# player1에 hp 키가 있는지 확인합니다.
if "hp" in player1:
    print("정보가 있습니다!")
else:
    print("정보가 없습니다!")

# player2에 hp 키가 있는지 확인합니다.
if "hp" in player2:
    print("정보가 있습니다!")
else:
    print("정보가 없습니다!")

# player1에 gold 키가 없는지 확인합니다.
if "gold" not in player1:
    print("골드 정보가 없습니다!")
