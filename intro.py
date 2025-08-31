import sys
import subprocess
import pygame
import os

def resource_path(relative_path):
    """실행 환경에 상관없이 리소스의 절대 경로를 반환한다."""
    try:
        base_path = sys._MEIPASS  # PyInstaller 환경
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 경로들
py_path = resource_path(os.path.dirname(__file__))
font_path = os.path.join(py_path, "Font")
pixel_font_path = os.path.join(font_path, "neodgm.ttf")
image_path = os.path.join(py_path, "image")
background_path = os.path.join(image_path, "Horizon.png")

background_1= pygame.image.load(os.path.join(image_path, "story_1.png"))
background_2 = pygame.image.load(os.path.join(image_path, "story_2.png"))
background_3 = pygame.image.load(os.path.join(image_path, "story_3.png"))
background_4 = pygame.image.load(os.path.join(image_path, "story_4.png"))

# ✅ 스토리 (원하는 대사로 바꾸세요)
STORY_LINES = [
    "도시의 빠른 생활에 지쳐, 나는 모든 걸 내려놓기로 했다...",
    "수년간 모은 돈을 들고, 고향 근처의 작은 시골 마을로 돌아왔다.",
    "이곳에서는 농사를 짓고, 낚시를 하며 조용히 살아가려 한다.",
    "이제, 나만의 새로운 삶이 시작된다."
]

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 853))
    pygame.display.set_caption("Intro")

    # 폰트 준비
    try:
        story_font = pygame.font.Font(pixel_font_path, 32)
        hint_font = pygame.font.Font(pixel_font_path, 22)
    except Exception:
        story_font = pygame.font.SysFont(None, 32)
        hint_font = pygame.font.SysFont(None, 22)

    idx = 0  # 현재 줄 인덱스
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                idx += 1
                if idx >= len(STORY_LINES):  # 마지막 줄 끝나면
                    running = False

        screen.fill((0, 0, 0))
        
        if 0 == idx:
            screen.blit(background_1, (0,0))
        elif (1 == idx):
            screen.blit(background_2, (0,0))
        elif (2 == idx):
            screen.blit(background_3, (0,0))
        else:
            screen.blit(background_4, (0,0))

        # 스토리 텍스트 (화면 맨 아래 중앙)
        if idx < len(STORY_LINES):
            text = story_font.render(STORY_LINES[idx], True, (255, 255, 255))
            text_rect = text.get_rect(center=(640, 800))  # ⬅️ y=650 → 화면 하단 중앙
            screen.blit(text, text_rect)

        # 안내 텍스트
        hint = hint_font.render("클릭하거나 아무 키나 누르세요", True, (200, 200, 200))
        hint_rect = hint.get_rect(center=(640, 840))
        screen.blit(hint, hint_rect)

        pygame.display.update()
        clock.tick(144)

    pygame.quit()

    # ✅ 게임 실행
    subprocess.run([sys.executable, os.path.join(py_path, "game.py")], cwd=py_path)

if __name__ == "__main__":
    main()
