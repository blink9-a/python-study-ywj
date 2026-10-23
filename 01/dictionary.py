
# 캐릭터의 정보를 딕셔너리로 저장합니다.
player = {
    "name": "마법사",
    "level": 10,
    "hp": 80
}

# 딕셔너리 전체를 출력합니다.
print(player)

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
player = {
    "name": "기사",
    "level": 5
}

# 새로운 키와 값을 추가합니다.
player["hp"] = 100

# 또 다른 키와 값을 추가합니다.
player["gold"] = 50

# 추가된 정보를 출력합니다.
print(player)




# 캐릭터의 정보를 저장합니다.
player = {
    "name": "기사",
    "level": 5,
    "hp": 100
}

# 캐릭터의 레벨을 변경합니다.
player["level"] = 6

# 공격을 받아 체력이 20 감소합니다.
player["hp"] -= 20

# 변경된 정보를 출력합니다.
print(player)



# 캐릭터의 정보를 저장합니다.
player = {
    "name": "기사",
    "level": 5,
    "hp": 100,
    "gold": 50
}

# gold 키와 연결된 값을 삭제합니다.
del player["gold"]


# 남아 있는 정보를 출력합니다.
print(player)


# 저장된 키와 값의 쌍 개수를 출력합니다.
print(len(player))
