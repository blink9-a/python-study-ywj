fuel = 100

for planet in range(1, 6):
    use = int(input(str(planet) + "번째 행성까지 필요한 연료: "))

    fuel = fuel - use

    print("남은 연료:", fuel)

    if fuel >= 50:
        print("탐사 계속!")

    elif fuel >= 20:
        print("연료가 부족합니다.")

    elif fuel < 20:
        print("위험! 지구로 돌아가야 합니다.")
