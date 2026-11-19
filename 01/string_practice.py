
# 1. 문자열 기본 활용 문제

# 사용할 문자열과 검색할 단어를 각각 저장합니다.
message = "GAME START"
word = "GO!"
keyword = "START"

# 1. 문자열 "GAME START" 뒤에 느낌표(!)를 연결하여 출력합니다.
print(message + "!")

# 2. 문자열 "GO!"를 3번 반복하여 출력합니다.
print(word * 3)

# 3. 공백 1개를 포함한 "GAME START"의 전체 글자 수인 10을 출력합니다.
print(len(message))

# 4. 인덱스 0에 있는 첫 번째 글자 "G"를 가져와 출력합니다.
print(message[0])

# 5. 인덱스 5부터 9까지의 글자 "START"를 가져와 출력합니다.
# 슬라이싱에서는 끝 인덱스인 10은 포함되지 않습니다.
print(message[5:10])

# 6. "START"가 message에 포함되어 있다면 "찾았습니다!"를 출력합니다.
if keyword in message:
    print("찾았습니다!")
# 앞의 조건이 거짓이고 "ERROR"가 포함되어 있다면 오류 메시지를 출력합니다.
elif "ERROR" in message:
    print("오류가 발생했습니다!")
# 위의 두 조건이 모두 거짓이라면 아래 메시지를 출력합니다.
else:
    print("일치하는 단어가 없습니다!")

# 7. "GO!"를 구성하는 3개의 글자 G, O, !를 차례대로 가져옵니다.
for letter in word:
    # 반복할 때마다 가져온 글자를 한 줄씩 출력합니다.
    print(letter)


# 2. 보물 상자의 비밀번호 찾기

# 보물 상자의 메시지를 저장합니다.
treasure_message = "BOX-7392-OPEN"

# 인덱스 4부터 7까지의 숫자 "7392"를 추출합니다.
password = treasure_message[4:8]

# 추출한 비밀번호를 출력합니다.
print(password)

# 인덱스 0에 있는 첫 번째 숫자 "7"을 출력합니다.
print(password[0])

# 비밀번호의 전체 글자 수인 4를 출력합니다.
print(len(password))

# "OPEN"이 포함되어 있다면 성공 메시지를 출력합니다.
if "OPEN" in treasure_message:
    print("보물 상자 열기 성공!")
# 앞의 조건이 거짓이고 "LOCK"이 포함되어 있다면 잠금 메시지를 출력합니다.
elif "LOCK" in treasure_message:
    print("보물 상자가 잠겨 있습니다!")
