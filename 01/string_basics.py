
# 1. 문자열 연결과 반복

# 두 개의 문자열을 저장합니다.
s01_first = "GAME"
s01_second = "START"

# 두 문자열을 연결합니다.
s01_message = s01_first + " " + s01_second

# 연결한 문자열을 출력합니다.
print(s01_message)

# 문자열을 세 번 반복합니다.
print("GO! " * 3)

# 구분선을 출력합니다.
print("-" * 20)


# 2. 문자열 길이 확인하기

# 게임 메시지를 저장합니다.
s02_message = "GAME START"

# 문자열의 길이를 출력합니다.
print(len(s02_message))


# 3. 문자열 인덱스로 접근하기

# 게임 메시지를 저장합니다.
s03_message = "PYTHON"

# 첫 번째 글자를 가져옵니다.
print(s03_message[0])

# 세 번째 글자를 가져옵니다.
print(s03_message[2])


# 4. 문자열 슬라이싱하기

# 게임 메시지를 저장합니다.
s04_message = "GAME START"

# 인덱스 0부터 3까지 가져옵니다.
print(s04_message[0:4])

# 인덱스 5부터 마지막까지 가져옵니다.
print(s04_message[5:])

# 처음부터 인덱스 3까지 가져옵니다.
print(s04_message[:4])


# 5. 문자열 포함 여부 확인하기

# 게임 메시지를 저장합니다.
s05_message = "GAME START"

# START라는 문자열이 있는지 확인합니다.
if "START" in s05_message:
    print("게임 시작 메시지입니다!")
else:
    print("시작 메시지가 아닙니다!")
