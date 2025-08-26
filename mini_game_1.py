import pygame
import sys
import os
import random

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
screen_width = 720
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("미니게임1")

# FPS 관리를 위한 시계 객체
clock = pygame.time.Clock()
##############################################################
#사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
py_path = resource_path(os.path.dirname(__file__))
image_path = str(py_path + r'/image')
font_path = (py_path + r'/Font')

# 이미지 로드
character = pygame.image.load(os.path.join(image_path, "mini_game_spaceship.png"))
enemy = pygame.image.load(os.path.join(image_path, "mini_game_enemy_spaceship.png"))
background = pygame.image.load(os.path.join(image_path, "mini_game_backgroud.png"))

#마스크생성
player_mask_base = pygame.mask.from_surface(character)

# 변수
character_speed = 1
to_x = 0
to_y = 0

timer = 0.0
count = 0 
max_delay = 3000 #3초
next_delay = round(random.uniform(1000, max_delay + 100), 100)


spawn_timer = 0.0
spawn_rate = 1.2  # 초당 스폰(대략)
fall_speed_min = 0.18
fall_speed_max = 0.32

#리스트
enemies = []
obstacles = []


# 크기
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = 1015 - character_height 


# 메인 게임 루프
running = True
while running:
    dt = clock.tick(144)

    timer += dt
    if timer >= next_delay:
        count += 1
        # 적 하나 스폰
        w, h = enemy.get_width(), enemy.get_height()

        x = random.randint(0, screen_width - w)
        y = -h  # 화면 위에서 등장
        spd = random.uniform(fall_speed_min, fall_speed_max)  # px/ms

        enemies.append({
            "rect": pygame.Rect(x, y, w, h),
            "spd": spd,
            "img": enemy,
            "mask": pygame.mask.from_surface(enemy)
        })

        # 다음 스폰 준비
        timer = 0.0
        max_delay = max(500, 3000 - count * 100)  # 실행마다 최대값 0.1s씩 감소, 최소 1.0s
        fall_speed_min = 0.25 + count * 0.01
        fall_speed_max = 0.32 + count * 0.01
        next_delay = random.randrange(500, max_delay + 100, 100)

    # ---- 적 이동/제거 ----
    for e in enemies:
        e["rect"].y += int(e["spd"] * dt)
    enemies = [e for e in enemies if e["rect"].top <= screen_height]

    # ---- 충돌 체크 → 즉시 게임 종료 ----
    player_rect = pygame.Rect(int(character_x_pos), int(character_y_pos), character_width, character_height)
    hit = False
    for e in enemies:
        # enemy 기준에서 player의 상대 좌표(= offset)
        offset = (player_rect.left - e["rect"].left, player_rect.top - e["rect"].top)
        # e["mask"] 기준으로 player_mask_base가 겹치는 픽셀이 있는가?
        if e["mask"].overlap(player_mask_base, offset):
            hit = True
            break

    if hit:
        running = False  # 게임 오버

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_x -= character_speed
            elif event.key == pygame.K_d:
                to_x += character_speed

    if event.type == pygame.KEYUP:
        if event.key in [pygame.K_a, pygame.K_d]:
            to_x = 0

    character_x_pos += to_x * dt

    character_x_pos = max(0, min(character_x_pos, 620))

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    for e in enemies:
        screen.blit(e["img"], e["rect"].topleft)
    pygame.display.update()
pygame.quit()