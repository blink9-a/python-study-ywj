# Pygame이 이미 설치되어 있는지 확인합니다.
try:
    # 게임 창, 키 입력, 도형 그리기에 사용하는 Pygame을 가져옵니다.
    import pygame

# Pygame을 찾지 못했다면 자동 설치를 준비합니다.
except ModuleNotFoundError as error:
    # 다른 라이브러리가 없어 발생한 오류라면 그대로 알립니다.
    if error.name != "pygame":
        # 실제 오류를 다시 발생시켜 원인을 확인할 수 있게 합니다.
        raise

    # 파이썬에서 설치 명령을 실행할 수 있는 도구를 가져옵니다.
    import subprocess
    # 현재 VS Code에서 실행 중인 파이썬의 경로를 가져옵니다.
    import sys
    # 설치 후 새 라이브러리를 다시 검색할 수 있는 도구를 가져옵니다.
    import importlib

    # 현재 파이썬(sys.executable)으로 pip(-m pip)를 실행하고, pygame-ce 2.5 이상 3 미만 버전을 설치합니다.
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame-ce>=2.5,<3"])
    # 방금 설치한 Pygame을 파이썬이 다시 찾도록 검색 정보를 갱신합니다.
    importlib.invalidate_caches()
    # 설치된 Pygame을 가져옵니다.
    import pygame

# 같은 폴더의 engine.py에서 게임을 실행하는 CoinGame 클래스를 가져옵니다.
from .engine import CoinGame
