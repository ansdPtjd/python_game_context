import pygame
import sys
import os
import random
import json

##############################################################
# 기본 초기화
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pygame.init()

screen_width = 720
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Horizon")
clock = pygame.time.Clock()

##############################################################
# 경로
py_path = resource_path(os.path.dirname(__file__))
image_path = str(py_path + r'/image')
font_path = (py_path + r'/Font')
pixel_pont_path = str(font_path + r'/neodgm.ttf')
save_path = (py_path + r'/save')
save_file = str(save_path + r'/mini_game_1.json')
music_path = (py_path + r'/music')

def load_image(name):
    """이미지를 로드하여 alpha 변환 후 반환한다."""
    return pygame.image.load(os.path.join(image_path, f"{name}.png")).convert_alpha()

# 이미지 로드
character = load_image("mini_game_spaceship")
enemy = load_image("mini_game_enemy_spaceship")
background = load_image("mini_game_backgroud")

# 마스크
player_mask_base = pygame.mask.from_surface(character)

# 폰트
score_font = pygame.font.Font(pixel_pont_path, 50)

##############################################################
# 변수
character_speed = 1
to_x = 0
score = 0

timer = 0.0
count = 0
max_delay = 3000  # 3초(ms)
next_delay = random.randrange(1000, max_delay + 100, 100)  # 0.1초 단위

fall_speed_min = 0.18
fall_speed_max = 0.2

enemies = []

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = 1015 - character_height

background_sound = pygame.mixer.Sound(os.path.join(music_path, "mini_game_background.mp3"))
background_sound.play(-1)

##############################################################
# 메인 루프
running = True
while running:
    dt = clock.tick(144)

    # 스폰 타이머
    timer += dt
    if timer >= next_delay:
        count += 1
        w, h = enemy.get_width(), enemy.get_height()
        x = random.randint(0, screen_width - w)
        y = -h
        spd = random.uniform(fall_speed_min, fall_speed_max)

        enemies.append({
            "rect": pygame.Rect(x, y, w, h),
            "spd": spd,
            "img": enemy,
            "mask": pygame.mask.from_surface(enemy)
        })

        # 다음 준비
        timer = 0.0
        max_delay = max(500, 3000 - count * 100)
        fall_speed_min = 0.25 + count * 0.05
        next_delay = random.randrange(500, max_delay + 100, 100)

    # 적 이동
    for e in enemies:
        e["rect"].y += int(e["spd"] * dt)

    # 화면 벗어난 적 제거 & 점수 증가
    new_enemies = []
    for e in enemies:
        if e["rect"].top <= screen_height:
            new_enemies.append(e)
        else:
            score += int(e["spd"] * 10)
    enemies = new_enemies

    # 충돌 체크
    player_rect = pygame.Rect(int(character_x_pos), int(character_y_pos), character_width, character_height)
    hit = False
    for e in enemies:
        offset = (player_rect.left - e["rect"].left, player_rect.top - e["rect"].top)
        if e["mask"].overlap(player_mask_base, offset):
            hit = True
            break

    if hit:
        running = False

    # 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_x -= character_speed
            elif event.key == pygame.K_d:
                to_x += character_speed
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                to_x = 0

    # 캐릭터 이동
    character_x_pos += to_x * dt
    character_x_pos = max(0, min(character_x_pos, screen_width - character_width))

    # 렌더
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    for e in enemies:
        screen.blit(e["img"], e["rect"].topleft)
    score_text = score_font.render(str("{0}점".format(score)), True, (0, 0, 0))
    screen.blit(score_text, (600, 0))
    pygame.display.update()

##############################################################
# 결과 저장
data = {"jud": 2, "score": score}
with open(save_file, "w", encoding="utf8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

pygame.quit()
sys.exit(0)
