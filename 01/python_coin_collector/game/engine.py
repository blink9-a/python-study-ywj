# 게임 창, 키보드 입력, 도형 그리기를 처리하는 Pygame 라이브러리를 가져옵니다.
import pygame


# 코인 한 개의 위치와 점수를 저장하는 클래스를 만듭니다.
class Coin:
    # x와 y는 코인의 중심 좌표이고, value는 코인을 먹을 때 얻는 점수입니다.
    def __init__(self, x, y, value):
        # 코인 중심의 가로 좌표를 저장합니다.
        self.x = x
        # 코인 중심의 세로 좌표를 저장합니다.
        self.y = y
        # 이 코인을 수집했을 때 얻는 점수를 저장합니다.
        self.value = value
        # 충돌 검사에 사용할 사각형을 만듭니다: 왼쪽=x-14, 위쪽=y-14, 너비=28, 높이=28입니다.
        self.rect = pygame.Rect(x - 14, y - 14, 28, 28)


# 게임 창과 게임 기능을 관리하는 클래스를 만듭니다.
class CoinGame:
    # title은 게임 창 제목이고, time_limit은 게임의 제한 시간(초)입니다.
    def __init__(self, title="Coin Collector", time_limit=60):
        # Pygame의 화면과 키보드 기능을 사용할 수 있도록 초기화합니다.
        pygame.init()
        # 가로 760픽셀, 세로 480픽셀 크기의 게임 창을 만듭니다.
        self.screen = pygame.display.set_mode((760, 480))
        # title로 전달받은 문자열을 게임 창의 제목으로 표시합니다.
        pygame.display.set_caption(title)
        # 게임이 너무 빠르게 반복되지 않도록 속도를 관리하는 시계를 만듭니다.
        self.clock = pygame.time.Clock()
        # 기본 글꼴(None)을 28픽셀 크기로 준비합니다.
        self.font = pygame.font.Font(None, 28)
        # 게임 창의 가로 크기를 저장합니다.
        self.width = 760
        # 게임 창의 세로 크기를 저장합니다.
        self.height = 480
        # 게임이 실행 중인지 기록합니다. True이면 반복문을 계속 실행합니다.
        self.running = True
        # 승리하거나 패배했는지 기록합니다. 시작할 때는 False입니다.
        self.finished = False
        # 승리 또는 패배 후 화면에 표시할 문구를 저장합니다.
        self.result = ""
        # 제한 시간을 초 단위로 저장합니다.
        self.time_limit = time_limit
        # 처음 남은 시간은 제한 시간과 같습니다.
        self.time_left = time_limit
        # 게임을 시작한 시각을 밀리초 단위로 저장합니다.
        self.start_time = pygame.time.get_ticks()
        # 캐릭터의 사각형을 만듭니다: 왼쪽=70, 위쪽=240, 너비=34, 높이=34입니다.
        self.player = pygame.Rect(70, 240, 34, 34)
        # 게임에 배치한 코인들을 보관할 빈 리스트를 만듭니다.
        self.coins = []

    # x와 y로 전달받은 숫자를 캐릭터의 시작 위치에 적용합니다.
    def add_player(self, x, y):
        # x는 화면 왼쪽에서부터 떨어진 거리(픽셀)입니다.
        self.player.x = x
        # y는 화면 위쪽에서부터 떨어진 거리(픽셀)입니다.
        self.player.y = y

    # x와 y는 코인의 중심 위치이고, value는 해당 코인의 점수입니다.
    def add_coin(self, x, y, value=10):
        # x, y, value를 Coin 클래스에 전달해 코인 한 개를 만듭니다.
        coin = Coin(x, y, value)
        # 만든 코인을 게임의 코인 리스트에 추가합니다.
        self.coins.append(coin)

    # 게임의 시간과 창 닫기 요청을 처리하는 함수를 만듭니다.
    def update(self):
        # 게임 반복 횟수를 1초에 최대 60번으로 제한합니다.
        self.clock.tick(60)
        # 창 닫기 또는 키보드 입력 등 발생한 이벤트를 하나씩 확인합니다.
        for event in pygame.event.get():
            # 창의 닫기 버튼을 눌렀는지 확인합니다.
            if event.type == pygame.QUIT:
                # 게임 반복을 끝내도록 running을 False로 바꿉니다.
                self.running = False
            # 키를 누른 이벤트이고, 누른 키가 ESC인지 확인합니다.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # ESC를 누른 경우에도 게임 반복을 끝냅니다.
                self.running = False
        # 아직 승리하거나 패배하지 않았다면 남은 시간을 갱신합니다.
        if not self.finished:
            # 현재 시각에서 시작 시각을 빼고 1000으로 나눠 지난 초를 구합니다.
            elapsed = (pygame.time.get_ticks() - self.start_time) // 1000
            # 제한 시간에서 지난 초를 빼되, 0보다 작아지지 않도록 합니다.
            self.time_left = max(0, self.time_limit - elapsed)

    # name으로 전달받은 방향의 키가 눌렸는지 확인합니다.
    def key(self, name):
        # 현재 눌린 키들의 상태를 가져옵니다.
        pressed = pygame.key.get_pressed()
        # name이 "left"인지 확인합니다.
        if name == "left":
            # 왼쪽 방향키 또는 A가 눌렸다면 True를 돌려줍니다.
            return pressed[pygame.K_LEFT] or pressed[pygame.K_a]
        # name이 "right"인지 확인합니다.
        if name == "right":
            # 오른쪽 방향키 또는 D가 눌렸다면 True를 돌려줍니다.
            return pressed[pygame.K_RIGHT] or pressed[pygame.K_d]
        # name이 "up"인지 확인합니다.
        if name == "up":
            # 위쪽 방향키 또는 W가 눌렸다면 True를 돌려줍니다.
            return pressed[pygame.K_UP] or pressed[pygame.K_w]
        # name이 "down"인지 확인합니다.
        if name == "down":
            # 아래쪽 방향키 또는 S가 눌렸다면 True를 돌려줍니다.
            return pressed[pygame.K_DOWN] or pressed[pygame.K_s]
        # 네 방향 중 어떤 것도 아니라면 False를 돌려줍니다.
        return False

    # dx는 가로 이동 거리이고, dy는 세로 이동 거리입니다.
    def move_player(self, dx, dy):
        # 이미 승리하거나 패배했다면 움직이지 않습니다.
        if self.finished:
            # 함수를 여기서 끝냅니다.
            return
        # 현재 가로 위치에 dx를 더합니다. 음수이면 왼쪽, 양수이면 오른쪽입니다.
        self.player.x = self.player.x + dx
        # 현재 세로 위치에 dy를 더합니다. 음수이면 위쪽, 양수이면 아래쪽입니다.
        self.player.y = self.player.y + dy
        # 캐릭터가 화면의 왼쪽 0과 오른쪽 끝 사이에 있도록 제한합니다.
        self.player.x = max(0, min(self.player.x, self.width - self.player.width))
        # 캐릭터가 상단 정보 표시줄(70) 아래와 화면의 아래쪽 끝 사이에 있도록 제한합니다.
        self.player.y = max(70, min(self.player.y, self.height - self.player.height))

    # 캐릭터와 닿아 있는 코인들을 찾아 돌려주는 함수를 만듭니다.
    def touching_coins(self):
        # 캐릭터와 닿은 코인들을 담을 빈 리스트를 만듭니다.
        touched = []
        # 게임이 끝났다면 코인을 더 이상 수집하지 않습니다.
        if self.finished:
            # 빈 리스트를 돌려줍니다.
            return touched
        # 현재 게임에 남아 있는 코인을 하나씩 확인합니다.
        for coin in self.coins:
            # 캐릭터 사각형과 코인 사각형이 겹치는지 검사합니다.
            if self.player.colliderect(coin.rect):
                # 서로 겹친 코인을 touched 리스트에 추가합니다.
                touched.append(coin)
        # 캐릭터와 닿은 코인 리스트를 돌려줍니다.
        return touched

    # coin은 화면에서 제거할 코인 객체입니다.
    def remove_coin(self, coin):
        # 전달받은 코인이 실제로 리스트에 있는지 확인합니다.
        if coin in self.coins:
            # 해당 코인을 리스트에서 제거해 다시 그려지지 않도록 합니다.
            self.coins.remove(coin)

    # 승리 상태로 변경하는 함수를 만듭니다.
    def win(self):
        # 아직 게임이 끝나지 않았다면 승리 처리를 진행합니다.
        if not self.finished:
            # 게임이 끝났다고 기록합니다.
            self.finished = True
            # 승리 문구를 저장합니다.
            self.result = "YOU WIN!"

    # 패배 상태로 변경하는 함수를 만듭니다.
    def lose(self):
        # 아직 게임이 끝나지 않았다면 패배 처리를 진행합니다.
        if not self.finished:
            # 게임이 끝났다고 기록합니다.
            self.finished = True
            # 패배 문구를 저장합니다.
            self.result = "TIME UP!"

    # message는 글자 내용, x와 y는 시작 위치, color는 RGB 글자 색상입니다.
    def show_text(self, message, x, y, color):
        # message를 문자열로 바꾸고, True로 글자를 부드럽게 하며, color로 글자 색상을 정합니다.
        image = self.font.render(str(message), True, color)
        # 글자 그림(image)을 게임 화면(screen)의 (x, y) 위치에 붙입니다.
        self.screen.blit(image, (x, y))

    # name은 캐릭터 이름, score는 현재 점수, goal은 목표 점수입니다.
    def draw(self, name="Hero", score=0, goal=50):
        # 화면 전체를 RGB 색상 (29, 41, 67)로 채웁니다.
        self.screen.fill((29, 41, 67))
        # 화면(screen)에 RGB 색상 (18, 26, 48)인 정보 표시줄을 (왼쪽=0, 위=0, 너비=760, 높이=70)에 그립니다.
        pygame.draw.rect(self.screen, (18, 26, 48), (0, 0, 760, 70))
        # 캐릭터 이름(name)을 (20, 20)에 흰색 계열 RGB로 표시합니다.
        self.show_text(name, 20, 20, (238, 243, 255))
        # 현재 점수(score)와 목표 점수(goal)를 (245, 20)에 노란색 계열 RGB로 표시합니다.
        self.show_text(f"Score: {score} / {goal}", 245, 20, (255, 220, 114))
        # 남은 시간(time_left)을 (585, 20)에 밝은 파란색 계열 RGB로 표시합니다.
        self.show_text(f"Time: {self.time_left}s", 585, 20, (192, 223, 249))
        # 게임에 남아 있는 코인들을 하나씩 그립니다.
        for coin in self.coins:
            # 화면(screen)에 노란색 RGB 원을 중심=(coin.x, coin.y), 반지름=14로 그립니다.
            pygame.draw.circle(self.screen, (255, 203, 75), (coin.x, coin.y), 14)
        # 화면(screen)에 파란색 RGB 사각형을 캐릭터 위치(player)에 그립니다.
        pygame.draw.rect(self.screen, (91, 185, 252), self.player)
        # 이동 방법과 종료 키를 (20, 448)에 회색 계열 RGB로 표시합니다.
        self.show_text("Move: arrows / WASD     ESC: exit", 20, 448, (170, 190, 210))
        # 승리 또는 패배 상태인지 확인합니다.
        if self.finished:
            # 결과를 잘 보이게 할 짙은 색 사각형을 (230, 170, 300, 125)에 그립니다.
            pygame.draw.rect(self.screen, (18, 26, 48), (230, 170, 300, 125))
            # 결과 문구(result)를 (315, 205)에 노란색 계열 RGB로 표시합니다.
            self.show_text(self.result, 315, 205, (255, 220, 114))
            # 종료 안내 문구를 (290, 248)에 흰색 계열 RGB로 표시합니다.
            self.show_text("Press ESC to exit", 290, 248, (238, 243, 255))
        # 지금까지 그린 화면을 게임 창에 보여줍니다.
        pygame.display.flip()

    # 게임을 종료할 때 호출하는 함수를 만듭니다.
    def close(self):
        # Pygame에서 사용하던 기능을 정리하고 종료합니다.
        pygame.quit()
