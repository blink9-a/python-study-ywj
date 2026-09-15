# 문제 1. 게임 직업 선택

start = input("직업을 선택하세요 (전사/마법사/궁수): ")

a = "우진님은 검을 받았습니다"

if start == "전사":
    print(a)
elif start == "마법사":
    print("우진님은 마법 지팡이를 받았습니다.")
elif start == "궁수":
    print("우진님은 활을 받았습니다.")



# 문제 2. 놀이기구 탑승 검사

print("놀이기구 탑승 검사")
height = input("자신의 키를 입력하세요: ")
start2 = int(height)

a = "혼자 탑승할 수 있습니다."
b = "보호자와 함께 탑승할 수 있습니다."
c = "탑승할 수 없습니다."

if start2 >= 150:
    print(a)
elif start2 >= 130:
    print(b)
elif start2 < 130:
    print(c)