import os
import pygame
import time
import random
import sys
import json
import subprocess
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)

def resource_path(relative_path):
    """실행 환경에 상관없이 리소스의 절대 경로를 반환한다."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 900
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Horizon")

# FPS 관리를 위한 시계 객체
clock = pygame.time.Clock()
FPS = 144
##############################################################
py_path = resource_path(os.path.dirname(__file__))  # 현재 파일의 위치 반환
image_path = str(py_path + r'/image')
save_path = (py_path + r'/save')
font_path = (py_path + r'/Font')
pixel_pont_path = str(font_path + r'/neodgm.ttf')
music_path = (py_path + r'/music')
save_file = str(save_path + r'/save_data.json')
save_file_mini_game_1 = str(save_path + r'/mini_game_1.json')

def load_image(name):
    """이미지를 로드하여 alpha 변환 후 반환한다."""
    return pygame.image.load(os.path.join(image_path, f"{name}.png")).convert_alpha()

background = load_image("room")
character = load_image("character")
bed = load_image("bed")
character = pygame.transform.scale(character, (character.get_width() * 2, character.get_height() * 2))
Button_f = load_image("F")
Button_f_UI = pygame.transform.scale(Button_f, (Button_f.get_width() * 2, Button_f.get_height() * 2))

UI_key_pont = pygame.font.Font(pixel_pont_path, 25)


# 변수
# game.py에서 넘겨준 현재 hp
start_hp = 100

start_hp = 100
bed_jud = 0
if len(sys.argv) >= 2:
    try:
        start_hp = int(float(sys.argv[1]))
    except ValueError:
        pass
if len(sys.argv) >= 3:
    try:
        bed_jud = int(sys.argv[2])
    except ValueError:
        pass

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height / 2) + (character_height / 2)
to_x = 0
to_y = 0
speed = 1
maxhp = 100

sleeping = False
fade_alpha = 0
fade_direction = 0
fade_start_time = 0
fade_surface = pygame.Surface((screen_width, screen_height))
fade_surface.fill((0, 0, 0))

running = True
while running:
    dt = clock.tick(FPS)  # FPS 설정 및 시간 기반 처리

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # 캐릭터 이동
            if event.key == pygame.K_a:
                to_x -= speed
            elif event.key == pygame.K_d:
                to_x += speed
            elif event.key == pygame.K_w:
                to_y -= speed
            elif event.key == pygame.K_s:
                to_y += speed

            if event.key == pygame.K_f:
                if (0 <= character_x_pos <= 90 and 400 <= character_y_pos <= 600):
                    sleeping = True
                    fade_direction = 1   # 화면 어둡게
                    fade_alpha = 0

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                to_x = 0
            elif event.key in [pygame.K_w, pygame.K_s]:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    print(character_x_pos, character_y_pos)

    character_x_pos = max(0, min(character_x_pos, 845))
    character_y_pos = max(0, min(character_y_pos, 750))

    screen.blit(background, (0,0))
    if bed_jud == 1:
        screen.blit(bed, (0, (screen_height / 2) + (character_height / 2)))

    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.draw.rect(screen, (0, 0, 0), (character_x_pos - (maxhp / 2.9) + 15, character_y_pos - 30, maxhp, 15))
    pygame.draw.rect(screen, (255, 0, 0), (character_x_pos - (maxhp / 3.2) + 15, character_y_pos - 27.5, start_hp - 5, 10))

    if (0 <= character_x_pos <= 90 and 600 >= character_y_pos >= 400) and bed_jud == 1:    
        K_1_text = UI_key_pont.render(str(": 잠자기"), True, (0, 0, 0))
        screen.blit(K_1_text, (800, (screen_height / 2) + (character_height / 2 + 300)))
        screen.blit(Button_f_UI, (750, (screen_height / 2) + (character_height / 2 + 300)))

    if (330 <= character_x_pos <= 515 and character_y_pos == 750):
        running = False

    # 수면 페이드 처리
    if sleeping:
        if fade_direction == 1:  # 어둡게
            fade_alpha += 5
            if fade_alpha >= 255:
                fade_alpha = 255
                fade_direction = 2
                fade_start_time = pygame.time.get_ticks()  # 3초 대기 시작
        elif fade_direction == 2:  # 3초 대기
            if pygame.time.get_ticks() - fade_start_time >= 3000:
                start_hp = 100  # hp 회복
                fade_direction = 3
        elif fade_direction == 3:  # 밝게
            fade_alpha -= 5
            if fade_alpha <= 0:
                fade_alpha = 0
                sleeping = False
                fade_direction = 0

        # 블랙 오버레이 그리기
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

    pygame.display.update()
pygame.quit()
with open("hp.tmp", "w") as f:
    f.write(f"{start_hp} {bed_jud}")