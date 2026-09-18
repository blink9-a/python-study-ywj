start = input("보물상자의 비밀번호를 입력하세요")
a = "보물상자가 열렸습니다."
b = "보물찾기를 종료합니다."
c = "금을 영어로 입력하세요"

if start == "gold":
    print(a)

elif start == "hint":
    print(c)

elif start == "exit":
    print(b)