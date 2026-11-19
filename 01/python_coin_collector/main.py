# game 폴더의 __init__.py에서 공개한 CoinGame 클래스를 가져옵니다.
from game import CoinGame


# 캐릭터의 이름, 이동 속도, 점수를 저장하는 클래스를 만듭니다.
class Hero:
    # name은 캐릭터 이름이고, speed는 한 번에 움직일 거리입니다.
    def __init__(self, name, speed):
        # 전달받은 name을 캐릭터의 이름으로 저장합니다.
        self.name = name
        # 전달받은 speed를 캐릭터의 이동 속도로 저장합니다.
        self.speed = speed
        # 게임을 시작할 때 점수를 0점으로 정합니다.
        self.score = 0


# Hero 클래스에 이름 "Hero"와 이동 속도 5를 전달해 캐릭터를 만듭니다.
hero = Hero("Hero", 5)

# 승리하는 데 필요한 목표 점수를 50점으로 정합니다.
goal = 50

# 게임 제한 시간을 60초로 정합니다.
time_limit = 60

# 게임 창 제목(title)으로 "Coin Collector"를, 제한 시간(time_limit)으로 60을 전달합니다.
game = CoinGame(title="Coin Collector", time_limit=time_limit)

# 캐릭터의 시작 위치를 가로 좌표 x=70, 세로 좌표 y=240으로 정합니다.
game.add_player(x=70, y=240)


# i가 0부터 4까지 변하는 동안 아래 코드를 5번 반복합니다.
for i in range(5):
    # x는 150에서 시작해 110씩 늘리고, y는 240으로 고정하며, 각 코인의 점수는 10점으로 정합니다.
    game.add_coin(x=150 + i * 110, y=240, value=10)


# 게임 창이 열려 있는 동안 들여쓴 코드를 계속 반복합니다.
while game.running:
    # 창 닫기, 키 입력, 제한 시간 계산 등 게임의 기본 상태를 갱신합니다.
    game.update()

    # "left" 키(왼쪽 방향키 또는 A)를 누르고 있는지 확인합니다.
    if game.key("left"):
        # 가로 이동량 dx에 -5, 세로 이동량 dy에 0을 전달해 왼쪽으로 움직입니다.
        game.move_player(-hero.speed, 0)

    # "right" 키(오른쪽 방향키 또는 D)를 누르고 있는지 확인합니다.
    if game.key("right"):
        # 가로 이동량 dx에 5, 세로 이동량 dy에 0을 전달해 오른쪽으로 움직입니다.
        game.move_player(hero.speed, 0)

    # "up" 키(위쪽 방향키 또는 W)를 누르고 있는지 확인합니다.
    if game.key("up"):
        # 가로 이동량 dx에 0, 세로 이동량 dy에 -5를 전달해 위쪽으로 움직입니다.
        game.move_player(0, -hero.speed)

    # "down" 키(아래쪽 방향키 또는 S)를 누르고 있는지 확인합니다.
    if game.key("down"):
        # 가로 이동량 dx에 0, 세로 이동량 dy에 5를 전달해 아래쪽으로 움직입니다.
        game.move_player(0, hero.speed)

    # 캐릭터와 닿은 코인을 하나씩 꺼내 coin 변수에 저장하며 반복합니다.
    for coin in game.touching_coins():
        # 현재 점수에 해당 코인의 점수(value)를 더해 다시 저장합니다.
        hero.score = hero.score + coin.value
        # 수집한 코인 객체(coin)를 전달해 게임 화면에서 제거합니다.
        game.remove_coin(coin)

    # 현재 점수가 목표 점수보다 크거나 같으면 승리 조건을 만족합니다.
    if hero.score >= goal:
        # 게임 상태를 승리로 변경합니다.
        game.win()

    # 남은 시간(time_left)이 0초 이하라면 패배 조건을 만족합니다.
    if game.time_left <= 0:
        # 아직 승리하지 않았다면 게임 상태를 패배로 변경합니다.
        game.lose()

    # name에는 캐릭터 이름, score에는 현재 점수, goal에는 목표 점수를 전달해 화면에 표시합니다.
    game.draw(name=hero.name, score=hero.score, goal=goal)


# 게임 창을 닫았을 때 Pygame의 사용을 종료합니다.
game.close()
