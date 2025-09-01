import os
import pygame
import time
import random
import sys
import json
import subprocess

#https://opengameart.org/content/peaceful-sea 미니게임_1 bgm

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
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Horizon")

# FPS 관리를 위한 시계 객체
clock = pygame.time.Clock()
##############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
py_path = resource_path(os.path.dirname(__file__))  # 현재 파일의 위치 반환
image_path = str(py_path + r'/image')
save_path = (py_path + r'/save')
font_path = (py_path + r'/Font')
pixel_pont_path = str(font_path + r'/neodgm.ttf')
music_path = (py_path + r'/music')
save_file = str(save_path + r'/save_data.json')
save_file_mini_game_1 = str(save_path + r'/mini_game_1.json')

# 이미지 로드
background = pygame.image.load(os.path.join(image_path, "background.png"))
background_reset = pygame.image.load(os.path.join(image_path, "background1.png"))
fishing1 = pygame.image.load(os.path.join(image_path, "fishing.png"))
fishing2 = pygame.image.load(os.path.join(image_path, "fishing.png"))
fishing3 = pygame.image.load(os.path.join(image_path, "fishing.png"))
fishing4 = pygame.image.load(os.path.join(image_path, "fishing.png"))
gameover = pygame.image.load(os.path.join(image_path, "gameover.png"))
field_dic = pygame.image.load(os.path.join(image_path, "field.png"))
sand = pygame.image.load(os.path.join(image_path, "sand.png"))
flower_dic = pygame.image.load(os.path.join(image_path, "potato_1.png"))
flower_dic2 = pygame.image.load(os.path.join(image_path, "potato_2.png"))
flower_dic3 = pygame.image.load(os.path.join(image_path, "potato_3.png"))
flower_dic4 = pygame.image.load(os.path.join(image_path, "potato_4.png"))
sand2 = pygame.image.load(os.path.join(image_path, "sand2.png"))
house = pygame.image.load(os.path.join(image_path, "house.png"))
fish_gage_bar = pygame.image.load(os.path.join(image_path, "gage_bar.png"))
fish_gage_bar_select = pygame.image.load(os.path.join(image_path, "gage_bar_select.png"))
store = pygame.image.load(os.path.join(image_path, "store.png"))
character = pygame.image.load(os.path.join(image_path, "character.png"))
fish_tool = pygame.image.load(os.path.join(image_path, "fish_tool.png"))
fish_tool2 = pygame.image.load(os.path.join(image_path, "fish_tool1.png"))
coin_png = pygame.image.load(os.path.join(image_path, "coin.png"))
inventory_png = pygame.image.load(os.path.join(image_path, "inventory.png"))
seed_png = pygame.image.load(os.path.join(image_path, "potato_seed.png"))
flower_png = pygame.image.load(os.path.join(image_path, "potato_4.png"))
fish_png = pygame.image.load(os.path.join(image_path, "fish.png"))
field_png = pygame.image.load(os.path.join(image_path, "field.png"))
store_ESC = pygame.image.load(os.path.join(image_path, "ESC.png"))
store_UI_buy = pygame.image.load(os.path.join(image_path, "store_UI_buy.png"))
store_UI_sell = pygame.image.load(os.path.join(image_path, "store_UI_sell.png"))
store_UI = pygame.image.load(os.path.join(image_path, "store_ui.png"))
worker_3 = pygame.image.load(os.path.join(image_path, "worker_3.png"))
worker_2 = pygame.image.load(os.path.join(image_path, "worker_2.png"))
worker_1 = pygame.image.load(os.path.join(image_path, "worker_1.png"))
store_UI_unbuy = pygame.image.load(os.path.join(image_path, "store_UI_unbuy.png"))
Button_1 = pygame.image.load(os.path.join(image_path, "1.png"))
Button_2 = pygame.image.load(os.path.join(image_path, "2.png"))
Button_3 = pygame.image.load(os.path.join(image_path, "3.png"))
Button_f = pygame.image.load(os.path.join(image_path, "F.png"))
Button_space = pygame.image.load(os.path.join(image_path, "SPACEALTERNATIVE.png"))
ticket_UI = pygame.image.load(os.path.join(image_path, "ticket.png"))
mini_game_1_UI = pygame.image.load(os.path.join(image_path, "mini_game_1.png"))
play_button = pygame.image.load(os.path.join(image_path, "play_button.png"))
mini_game_icon = pygame.image.load(os.path.join(image_path, "mini_game_icon.png"))

tomato_1 = pygame.image.load(os.path.join(image_path, "tomato_1.png"))
tomato_2 = pygame.image.load(os.path.join(image_path, "tomato_2.png"))
tomato_3 = pygame.image.load(os.path.join(image_path, "tomato_3.png"))
tomato_4 = pygame.image.load(os.path.join(image_path, "tomato_4.png"))
tomato_seed_UI = pygame.image.load(os.path.join(image_path, "tomato_seed.png"))

pumpkin_1 = pygame.image.load(os.path.join(image_path, "pumpkin_1.png"))
pumpkin_2 = pygame.image.load(os.path.join(image_path, "pumpkin_2.png"))
pumpkin_3 = pygame.image.load(os.path.join(image_path, "pumpkin_3.png"))
pumpkin_4 = pygame.image.load(os.path.join(image_path, "pumpkin_4.png"))
pumpkin_seed_UI  = pygame.image.load(os.path.join(image_path, "pumpkin_seed.png"))

wheat_1 = pygame.image.load(os.path.join(image_path, "wheat_1.png"))
wheat_2 = pygame.image.load(os.path.join(image_path, "wheat_2.png"))
wheat_3 = pygame.image.load(os.path.join(image_path, "wheat_3.png"))
wheat_4 = pygame.image.load(os.path.join(image_path, "wheat_4.png"))
wheat_seed_UI  = pygame.image.load(os.path.join(image_path, "wheat_seed.png"))

left_button  = pygame.image.load(os.path.join(image_path, "arrow_left.png"))
right_button  = pygame.image.load(os.path.join(image_path, "arrow_right.png"))


# 이미지 크기
worker_3_UI = pygame.transform.scale(worker_3, (worker_3.get_width() * 2, worker_3.get_height() * 2))
worker_2_UI = pygame.transform.scale(worker_2, (worker_2.get_width() * 2, worker_2.get_height() * 2))
worker_1_UI = pygame.transform.scale(worker_1, (worker_1.get_width() * 2, worker_1.get_height() * 2))
Button_1_UI = pygame.transform.scale(Button_1, (Button_1.get_width() * 2, Button_1.get_height() * 2))
Button_2_UI = pygame.transform.scale(Button_2, (Button_2.get_width() * 2, Button_2.get_height() * 2))
Button_3_UI = pygame.transform.scale(Button_3, (Button_3.get_width() * 2, Button_3.get_height() * 2))
Button_f_UI = pygame.transform.scale(Button_f, (Button_f.get_width() * 2, Button_f.get_height() * 2))
Button_space_UI = pygame.transform.scale(Button_space, (Button_space.get_width() * 2, Button_space.get_height() * 2))
fish_UI = pygame.transform.scale(fish_png, (fish_png.get_width() //2 , fish_png.get_height() // 2))
seed_UI = pygame.transform.scale(seed_png, (seed_png.get_width() //2 , seed_png.get_height() // 2))

# 저장 내용 불러오기
if os.path.exists(save_file):
    with open(save_file, "r", encoding="utf8") as f:
        data = json.load(f)
else:
    data = {}

field_x = int(data.get("field_x", 0))
field_y = int(data.get("field_y", 0))
seed = int(data.get("seed", 0))
flower = int(data.get("flower", 0))
fish = int(data.get("fish", 0))
coin = int(data.get("coin", 0))
hp = int(data.get("hp", 0))
plants_time = data.get("plants_time", [])
plants_seat = data.get("plants_seat", [])
worker_3_jud = data.get("worker_3_jud", 0)
worker_3_seed = data.get("worker_3_seed", [])
worker_3_flower = data.get("worker_3_flower", [])
worker_2_jud = data.get("worker_2_jud", 0)
worker_2_seed = data.get("worker_2_seed", [])
worker_2_flower = data.get("worker_2_flower", [])
worker_1_jud = data.get("worker_1_jud", 0)
worker_1_fish = data.get("worker_1_fish", [0])
ticket = data.get("ticket", 0)
tomato = data.get("tomato", 0)
pumpkin = data.get("pumpkin", 0)
wheat = data.get("wheat", 0)
tomato_seed = data.get("tomato_seed", 0)
pumpkin_seed = data.get("pumpkin_seed", 0)
wheat_seed = data.get("wheat_seed", 0)


# Font 정의
game_font = pygame.font.Font(pixel_pont_path, 100)
gameover_font = pygame.font.Font(pixel_pont_path, 100)
inventory_font = pygame.font.Font(pixel_pont_path, 25)
UI_font = pygame.font.Font(pixel_pont_path, 50)
gameover_text = gameover_font.render(str("[피로도에 의해 캐릭터가 기절했습니다.]"), True, (255, 0, 0))
UI_key_pont = pygame.font.Font(pixel_pont_path, 25)

# 리스트
field_num = [field_x, field_y]
inventory = [seed, flower, fish, ticket, tomato_seed, tomato, pumpkin_seed, pumpkin, wheat_seed, wheat]  # 꽃 씨앗, 꽃, 물고기
inventory_text = [
    inventory_font.render(str(5), True, (255, 255, 255)),
    inventory_font.render(str(0), True, (255, 255, 255)),
    inventory_font.render(str(0), True, (255, 255, 255)),
    inventory_font.render(str(0), True, (255, 255, 255)),
    inventory_font.render(str(0), True, (255, 255, 255)),
    inventory_font.render(str(0), True, (255, 255, 255)),
    inventory_font.render(str(0), True, (255, 255, 255)),
    inventory_font.render(str(0), True, (255, 255, 255)),
    inventory_font.render(str(0), True, (255, 255, 255)),
    inventory_font.render(str(0), True, (255, 255, 255)),
]

# 크기
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height / 2) + (character_height / 2)
store_UI_x_pos = (screen_width / 2) - (character_width / 2)
store_UI_y_pos = (screen_height / 2) + (character_height / 2)
store_UI_size = store_UI.get_rect().size
store_UI_width = store_UI_size[0]
store_UI_height = store_UI_size[1]
background_size = background.get_rect().size
background_width = background_size[0]
background_height = background_size[1]

# 변수
background_x_pos = 0
background_y_pos = 2160
fish = 0
fish_x_pos = (screen_width / 2) - (character_width / 2)
fish_y_pos = (screen_height / 2) + (character_height / 2)
fish_x_pul = 0
fish_point = 0
fish_ran = 0
gameover_sig = 0
store_jud = 0
work_jud = 0
mini_game_jud = 0
maxhp = 100
to_x = 0
to_y = 0
background_speed = 1
mini_game_1 = 0
store_index = 0

# NPC 월드 좌표 (카메라와 분리)
worker_3_world_x = 1500
worker_3_world_y = -1550
worker_3_speed = 1
woker_3_pos_jud = 0
woker_3_prev_bucket = None
last_time = [0, 0, 0]
worker_2_world_x = 1500
worker_2_world_y = -1550
worker_2_speed = 5
worker_2_pos_jud = 0
worker_2_prev_bucket = None
last_time_2 = [0, 0, 0]
worker_1_world_x = 1500
worker_1_world_y = -1550
worker_1_speed = 5
worker_1_pos_jud = 0
worker_1_prev_bucket = None
last_time_1 = [0,0]
worker_1_fish_jud = 0

target1_x, target1_y = 1265, -1550  # 상점
target2_x, target2_y = 1500, -1560  # 밭
target3_x, target3_y = 1265, 1600

SEED_STOCK = 5


# 배경음악
background_sound = pygame.mixer.Sound(os.path.join(music_path, "background.mp3"))
background_sound.play(-1)

# 메인 게임 루프
running = True
while running:
    dt = clock.tick(144)  # FPS 설정 및 시간 기반 처리
    now_ms = pygame.time.get_ticks()  # ✅ 프레임당 1회만 시간 읽기

    coin_text = game_font.render(str(coin), True, (255, 255, 255))

    if mini_game_1 == 1:
        # 미니게임 실행 (끝날 때까지 기다림)
        background_sound.stop()
        subprocess.run([sys.executable, "mini_game_1.py"])
        mini_game_1 = 0

        # 결과 읽기
        if os.path.exists(save_file_mini_game_1):
            with open(save_file_mini_game_1, "r", encoding="utf8") as f:
                data_mini_game_1 = json.load(f)
        else:
            data_mini_game_1 = {}

        mini_game_1_jud = int(data_mini_game_1.get("jud", 0))
        if mini_game_1_jud == 2:
            score = int(data_mini_game_1.get("score", 0))
            coin += score

            # 상태 초기화
            data_mini_game_1 = {"jud": 0, "score": 0}
            with open(save_file_mini_game_1, "w", encoding="utf8") as f:
                json.dump(data_mini_game_1, f, ensure_ascii=False, indent=4)
        background_sound.play(-1)


    # 식물 성장 시간 업데이트
    for i in range(len(plants_time)):
        if plants_time[i] > 3:
            plants_time[i] -= 4

    # 체력 확인 및 게임 오버 처리
    if hp <= 0:
        coin -= 100
        background_x_pos = 0
        background_y_pos = 3000
        gameover_sig = 1

    # 식물 좌석 수 체크 및 초기화
    while len(plants_seat) < field_num[0] * field_num[1]:
        plants_seat.append(0)

    # 인벤토리 텍스트 업데이트
    for i in range(len(inventory_text)):
        inventory_text[i] = inventory_font.render(str(inventory[i]), True, (255, 255, 255))

    # 2. 이벤트 처리 (키보드, 마우스 등)
    cul = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            hp -= 0.01  # 체력 감소

            # 캐릭터 이동
            if event.key == pygame.K_a:
                to_x += background_speed
            elif event.key == pygame.K_d:
                to_x -= background_speed
            elif event.key == pygame.K_w:
                to_y += background_speed
            elif event.key == pygame.K_s:
                to_y -= background_speed

            # 꽃 심기 (플레이어 수동)
            if event.key == pygame.K_1:
                if -520 - field_num[0] * 100 < background_x_pos < -520 and 1855 - field_num[1] * 100 < background_y_pos < 2125:
                    if inventory[0] > 0:
                        for cul in range(field_num[0] * field_num[1]):
                            if plants_seat[cul] == 0:
                                plants_seat[cul] = 1
                                if len(plants_time) <= cul:
                                    plants_time.append(0)
                                plants_time[cul] = 1500  # 약 30초
                                hp -= 0.5
                                inventory[0] -= 1
                                inventory_text[0] = inventory_font.render(str(inventory[0]), True, (255, 255, 255))
                                break

            # 토마토 심기 (플레이어 수동)
            if event.key == pygame.K_5:
                if -520 - field_num[0] * 100 < background_x_pos < -520 and 1855 - field_num[1] * 100 < background_y_pos < 2125:
                    if inventory[4] > 0:
                        for cul in range(field_num[0] * field_num[1]):
                            if plants_seat[cul] == 0:
                                plants_seat[cul] = 2
                                if len(plants_time) <= cul:
                                    plants_time.append(0)
                                plants_time[cul] = 1500
                                hp -= 0.5
                                inventory[4] -= 1
                                inventory_text[4] = inventory_font.render(str(inventory[4]), True, (255, 255, 255))
                                break

            # 호박 심기 (플레이어 수동)
            if event.key == pygame.K_7:
                if -520 - field_num[0] * 100 < background_x_pos < -520 and 1855 - field_num[1] * 100 < background_y_pos < 2125:
                    if inventory[6] > 0:
                        for cul in range(field_num[0] * field_num[1]):
                            if plants_seat[cul] == 0:
                                plants_seat[cul] = 3
                                if len(plants_time) <= cul:
                                    plants_time.append(0)
                                plants_time[cul] = 1500
                                hp -= 0.5
                                inventory[6] -= 1
                                inventory_text[6] = inventory_font.render(str(inventory[6]), True, (255, 255, 255))
                                break

            # 밀 심기 (플레이어 수동)
            if event.key == pygame.K_9:
                if -520 - field_num[0] * 100 < background_x_pos < -520 and 1855 - field_num[1] * 100 < background_y_pos < 2125:
                    if inventory[8] > 0:
                        for cul in range(field_num[0] * field_num[1]):
                            if plants_seat[cul] == 0:
                                plants_seat[cul] = 4
                                if len(plants_time) <= cul:
                                    plants_time.append(0)
                                plants_time[cul] = 1500
                                hp -= 0.5
                                inventory[8] -= 1
                                inventory_text[8] = inventory_font.render(str(inventory[8]), True, (255, 255, 255))
                                break

            # 낚시 / 상점 / 일 시작
            if event.key == pygame.K_f:
                if background_y_pos < -900:
                    fish = 1
                elif -365 < background_x_pos < -225 and background_y_pos > 2150:
                    store_jud = 1
                elif -665 < background_x_pos < -525 and background_y_pos > 2150:
                    work_jud = 1
                elif -965 < background_x_pos < -825 and background_y_pos > 2150:
                    mini_game_jud = 1

            # 체력 회복
            if event.key == pygame.K_2:
                if inventory[1] >= 1 and hp < 100:
                    hp += 1
                    inventory[1] -= 1
            elif event.key == pygame.K_3:
                if inventory[2] >= 1 and hp < 100:
                    hp += 2
                    inventory[2] -= 1

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                to_x = 0
            elif event.key in [pygame.K_w, pygame.K_s]:
                to_y = 0

    # 카메라(배경) 이동
    background_x_pos += to_x * dt
    background_y_pos += to_y * dt

    # ====== 일꾼3 로직 ======
    if worker_3_jud == 1:    
        num = 0

        if woker_3_prev_bucket == 1:
            # 밭에 있었으면 씨앗이 남아있는 동안은 계속 밭 유지
            if worker_3_seed[num] > 0:
                current_bucket = 1   # 밭
            else:
                current_bucket = 0   # 씨앗 0 → 상점
        else:
            # 상점(또는 초기): 씨앗 목표치 못 채웠거나/꽃이 남아있으면 계속 상점
            if (worker_3_seed[num] < SEED_STOCK) or (worker_3_flower[num] > 0):
                current_bucket = 0   # 상점
            else:
                current_bucket = 1   # 밭

        is_first = (woker_3_prev_bucket is None)
        bucket_changed = is_first or (current_bucket != woker_3_prev_bucket)

        if current_bucket == 0:  # 상점으로 가기
            target_x = target1_x
            target_y = target1_y
        else:                    # 밭으로 가기
            target_x = target2_x
            target_y = target2_y

        # 목표 월드 좌표 동기화
        woker_3_target_x = target_x
        woker_3_target_y = target_y

        # 도착 판정(월드 좌표)
        arrived = (-2 < (worker_3_world_x - woker_3_target_x) < 2) and (-2 < (worker_3_world_y - woker_3_target_y) < 2)

        # 이동 상태 결정: 목표 바뀌었거나 도착 전이면 이동(1), 그 외 0
        if bucket_changed or (not arrived):
            woker_3_pos_jud = 1
        else:
            woker_3_pos_jud = 0
            # ✅ 도착했고 목표가 밭이면: 1초마다 1개 심기
            if (target_x == target2_x and target_y == target2_y):
                if worker_3_seed[num] > 0 and (now_ms - last_time[0] >= 1000):
                    for cul in range(field_num[0] * field_num[1]):
                        if (worker_3_seed[num] <= 0):
                            last_time[0] = now_ms
                            break
                        if plants_seat[cul] == 0 and (now_ms - last_time[0] >= 1000):  # 빈 자리
                            plants_seat[cul] = 1
                            if len(plants_time) <= cul:
                                plants_time.append(0)
                            plants_time[cul] = 1500
                            worker_3_seed[num] -= 1
                            last_time[0] = now_ms

            # ✅ 도착했고 목표가 상점이면: 1초마다 1개 판매(코인+)
            elif (target_x == target1_x and target_y == target1_y):
                if (coin > 0 and (now_ms - last_time[1] >= 1000) and (worker_3_seed[0] < SEED_STOCK)):
                    coin -= 10
                    worker_3_seed[num] += 1
                    last_time[1] = now_ms
                    
                    
                if worker_3_flower[num] > 0 and (now_ms - last_time[2] >= 1000):
                    coin += 30
                    worker_3_flower[num] -= 1
                    last_time[2] = now_ms
        # ========================

        # 이동(월드 좌표)
        if woker_3_pos_jud == 1:
            if worker_3_world_x < woker_3_target_x:
                worker_3_world_x += worker_3_speed
            elif worker_3_world_x > woker_3_target_x:
                worker_3_world_x -= worker_3_speed

            if worker_3_world_y < woker_3_target_y:
                worker_3_world_y += worker_3_speed
            elif worker_3_world_y > woker_3_target_y:
                worker_3_world_y -= worker_3_speed

        # 다음 프레임 비교용
        woker_3_prev_bucket = current_bucket

    # ====== 일꾼2 로직 ======
    if worker_2_jud == 1:
        num = 0

        if worker_2_prev_bucket == 1:
            if worker_2_seed[num] > 0:
                current_bucket_2 = 1
            else:
                current_bucket_2 = 0
        else:
            if (worker_2_seed[num] < SEED_STOCK) or (worker_2_flower[num] > 0):
                current_bucket_2 = 0   # 상점
            else:
                current_bucket_2 = 1
        is_first_2 = (worker_2_prev_bucket is None)
        bucket_changed_2 = is_first_2 or (current_bucket_2 != worker_2_prev_bucket)

        if current_bucket_2 == 0:
            target_x_2, target_y_2 = target1_x, target1_y
        else:
            target_x_2, target_y_2 = target2_x, target2_y

        woker_2_target_x = target_x_2
        woker_2_target_y = target_y_2

        # 도착 판정
        arrived_2 = (-6 < (worker_2_world_x - woker_2_target_x) < 6) and (-6 < (worker_2_world_y - woker_2_target_y) < 6)

        # 이동/정지 상태
        if bucket_changed_2 or (not arrived_2):
            worker_2_pos_jud = 1
        else:
            worker_2_pos_jud = 0
            # 밭에 도착 → 1초마다 씨앗 1개 심기
            if (target_x_2 == target2_x and target_y_2 == target2_y):
                if worker_2_seed[num] > 0 and (now_ms - last_time_2[0] >= 1000):
                    for cul in range(field_num[0] * field_num[1]):
                        if (worker_2_seed[num] <= 0):
                            last_time_2[0] = now_ms
                            break
                        if plants_seat[cul] == 0 and now_ms - last_time_2[0] >= 1000:
                            plants_seat[cul] = 1
                            if len(plants_time) <= cul:
                                plants_time.append(0)
                            plants_time[cul] = 1500
                            worker_2_seed[num] -= 1
                            last_time_2[0] = now_ms
                        
            # 상점에 도착 → 1초마다 꽃 1개 판매 (+코인)
            elif (target_x_2 == target1_x and target_y_2 == target1_y):
                # (참고) 아래 for-루프는 프레임 내에서는 1개만 동작합니다.
                if (coin > 0 and (now_ms - last_time_2[2] >= 1000) and (worker_2_seed[0] < SEED_STOCK)):
                        coin -= 10
                        worker_2_seed[num] += 1
                        last_time_2[2] = now_ms

                if worker_2_flower[num] > 0 and (now_ms - last_time_2[1] >= 1000):
                    coin += 30
                    worker_2_flower[num] -= 1
                    last_time_2[1] = now_ms

        # 이동 처리
        if worker_2_pos_jud == 1:
            if worker_2_world_x < woker_2_target_x:
                worker_2_world_x += worker_2_speed
            elif worker_2_world_x > woker_2_target_x:
                worker_2_world_x -= worker_2_speed
            if worker_2_world_y < woker_2_target_y:
                worker_2_world_y += worker_2_speed
            elif worker_2_world_y > woker_2_target_y:
                worker_2_world_y -= worker_2_speed

        # 다음 프레임 대비
        worker_2_prev_bucket = current_bucket_2

    # ====== 일꾼1 로직 ======
    if worker_1_jud == 1:
        num = 0
        
        if (worker_1_prev_bucket == 0 and worker_1_fish[num] > 0):
            current_bucket_1 = 0
        else:
            current_bucket_1 = 0 if (worker_1_fish[num] >= 5) else 1

        is_first_1 = (worker_1_prev_bucket is None)
        bucket_changed_1 = is_first_1 or (current_bucket_1 != worker_1_prev_bucket)

        if current_bucket_1 == 0:
            target_x_1, target_y_1 = target1_x, target1_y
        else:
            target_x_1, target_y_1 = target3_x, target3_y

        woker_1_target_x = target_x_1
        woker_1_target_y = target_y_1

        # 도착 판정
        arrived_1 = (-6 < (worker_1_world_x - woker_1_target_x) < 6) and (-6 < (worker_1_world_y - woker_1_target_y) < 6)
        cul2 = 0
        

        # 이동/정지 상태s
        if bucket_changed_1 or (not arrived_1):
            worker_1_pos_jud = 1
        else:
            worker_1_pos_jud = 0
            if (target_x_1 == target3_x and target_y_1 == target3_y):
                screen.blit(fish_tool, ((fish_x_pos - 30, fish_y_pos - 20)))
                if now_ms - last_time_1[0] >= 5000:
                    
                    if random.random() < 0.5:
                        worker_1_fish[num] += 1
                        if (worker_1_fish_jud == 0):
                            worker_1_fish_jud = 10
                    else:
                        worker_1_fish_jud == 0

            elif (target_x_1 == target1_x and target_y_1 == target1_y):
                if worker_1_fish[num] > 0 and (now_ms - last_time_1[1] >= 1000):
                    coin += 100
                    worker_1_fish[num] -= 1
                    last_time_1[1] = now_ms
            

        # 이동 처리
        if worker_1_pos_jud == 1:
            if worker_1_world_x < woker_1_target_x:
                worker_1_world_x += worker_1_speed
            elif worker_1_world_x > woker_1_target_x:
                worker_1_world_x -= worker_1_speed
            if worker_1_world_y < woker_1_target_y:
                worker_1_world_y += worker_1_speed
            elif worker_1_world_y > woker_1_target_y:
                worker_1_world_y -= worker_1_speed

        # 다음 프레임 대비
        worker_1_prev_bucket = current_bucket_1
        cul2 = 0


    # 3. 게임 배경 위치 정의 (클램프)
    background_x_pos = max(-5840, min(background_x_pos, 0))
    background_y_pos = max(-1080, min(background_y_pos, 2160))

    # 4. 충돌 처리 (없음)

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))  # 배경 초기화

    screen.blit(background, (int(background_x_pos), int(background_y_pos)))  # 배경
    screen.blit(background, (int(background_x_pos), int(background_y_pos - background_height)))
    screen.blit(background, (int(background_x_pos + background_width), int(background_y_pos)))
    screen.blit(background, (int(background_x_pos + background_width), int(background_y_pos - background_height)))
    screen.blit(fishing1, (int(background_x_pos), int(background_y_pos + 1680)))  # 강
    screen.blit(sand2, (int(background_x_pos + 865), int(background_y_pos - 1800)))
    screen.blit(house, (int(background_x_pos + 865), int(background_y_pos - 1800)))  # 집
    screen.blit(sand2, (int(background_x_pos + 1165), int(background_y_pos - 1800)))
    screen.blit(store, (int(background_x_pos + 1165), int(background_y_pos - 1800)))  # 가게
    screen.blit(sand2, (int(background_x_pos + 1465), int(background_y_pos - 1800)))
    screen.blit(store, (int(background_x_pos + 1465), int(background_y_pos - 1800)))
    screen.blit(mini_game_icon, (int(background_x_pos + 1765), int(background_y_pos - 1700)))

    # 밭 그리기
    for d in range(field_num[1]):
        for e in range(field_num[0]):
            screen.blit(field_dic, (int(background_x_pos + 1500 + e * 100),
                                    int(background_y_pos - 1560 + d * 100)))

    # 꽃 그리기/수확 처리
    for d in range(field_num[1]):
        for e in range(field_num[0]):
            index = d * field_num[0] + e
            x_position = int(background_x_pos + 1500 + e * 105)
            y_position = int(background_y_pos - background_height + 600 + d * 100)

            if plants_seat[index] == 1:
                if plants_time[index] > 1000:
                    screen.blit(flower_dic, (x_position, y_position))
                elif plants_time[index] > 100:
                    screen.blit(flower_dic2, (x_position, y_position))
                elif plants_time[index] > 0:
                    screen.blit(flower_dic3, (x_position, y_position))
                else:
                    screen.blit(flower_dic4, (x_position, y_position))

                    # 플레이어 수동 수확 구역
                    if (-815 - (field_num[0] - 3) * 110 < background_x_pos < -520 and 1855 < background_y_pos < 2125):
                        for a, plant_time in enumerate(plants_time):
                            if plant_time == 0 and plants_seat[a] == 1:
                                plants_seat[a] = 0
                                plants_time[a] = 1_000_000_000  # 오류 방지
                                inventory[1] += 1
                                inventory_text[1] = inventory_font.render(str(inventory[1]), True, (255, 255, 255))
                    # 일꾼 자동 수확(밭 도착 상태)
                    elif woker_3_pos_jud == 0  and worker_3_jud == 1:
                        if target_x == target2_x and target_y == target2_y:
                            for a, plant_time in enumerate(plants_time):
                                if plant_time == 0 and plants_seat[a] == 1:
                                    plants_seat[a] = 0
                                    plants_time[a] = 1_000_000_000  # 오류 방지
                                    worker_3_flower[0] += 1

                    elif worker_2_pos_jud == 0 and worker_2_jud == 1:
                        if target_x_2 == target2_x and target_y_2 == target2_y:
                            for a, plant_time in enumerate(plants_time):
                                if plant_time == 0 and plants_seat[a] == 1:
                                    plants_seat[a] = 0
                                    plants_time[a] = 1_000_000_000  # 오류 방지
                                    worker_2_flower[0] += 1

            elif plants_seat[index] == 2:
                if plants_time[index] > 1000:
                    screen.blit(tomato_1, (x_position, y_position))
                elif plants_time[index] > 100:
                    screen.blit(tomato_2, (x_position, y_position))
                elif plants_time[index] > 0:
                    screen.blit(tomato_3, (x_position, y_position))
                else:
                    screen.blit(tomato_4, (x_position, y_position))

                    if (-815 - (field_num[0] - 3) * 110 < background_x_pos < -520 and 1855 < background_y_pos < 2125):
                        for a, plant_time in enumerate(plants_time):
                            if plant_time == 0 and plants_seat[a] == 2:
                                plants_seat[a] = 0
                                plants_time[a] = 1_000_000_000
                                inventory[5] += 1
                                inventory_text[5] = inventory_font.render(str(inventory[5]), True, (255, 255, 255))
                    elif woker_3_pos_jud == 0 and worker_3_jud == 1:
                        if target_x == target2_x and target_y == target2_y:
                            for a, plant_time in enumerate(plants_time):
                                if plant_time == 0 and plants_seat[a] == 2:
                                    plants_seat[a] = 0
                                    plants_time[a] = 1_000_000_000
                                    inventory[5] += 1
                                    inventory_text[5] = inventory_font.render(str(inventory[5]), True, (255, 255, 255))
                    elif worker_2_pos_jud == 0 and worker_2_jud == 1:
                        if target_x_2 == target2_x and target_y_2 == target2_y:
                            for a, plant_time in enumerate(plants_time):
                                if plant_time == 0 and plants_seat[a] == 2:
                                    plants_seat[a] = 0
                                    plants_time[a] = 1_000_000_000
                                    inventory[5] += 1
                                    inventory_text[5] = inventory_font.render(str(inventory[5]), True, (255, 255, 255))

            elif plants_seat[index] == 3:
                if plants_time[index] > 1000:
                    screen.blit(pumpkin_1, (x_position, y_position))
                elif plants_time[index] > 100:
                    screen.blit(pumpkin_2, (x_position, y_position))
                elif plants_time[index] > 0:
                    screen.blit(pumpkin_3, (x_position, y_position))
                else:
                    screen.blit(pumpkin_4, (x_position, y_position))

                    if (-815 - (field_num[0] - 3) * 110 < background_x_pos < -520 and 1855 < background_y_pos < 2125):
                        for a, plant_time in enumerate(plants_time):
                            if plant_time == 0 and plants_seat[a] == 3:
                                plants_seat[a] = 0
                                plants_time[a] = 1_000_000_000
                                inventory[7] += 1
                                inventory_text[7] = inventory_font.render(str(inventory[7]), True, (255, 255, 255))
                    elif woker_3_pos_jud == 0 and worker_3_jud == 1:
                        if target_x == target2_x and target_y == target2_y:
                            for a, plant_time in enumerate(plants_time):
                                if plant_time == 0 and plants_seat[a] == 3:
                                    plants_seat[a] = 0
                                    plants_time[a] = 1_000_000_000
                                    inventory[7] += 1
                                    inventory_text[7] = inventory_font.render(str(inventory[7]), True, (255, 255, 255))
                    elif worker_2_pos_jud == 0 and worker_2_jud == 1:
                        if target_x_2 == target2_x and target_y_2 == target2_y:
                            for a, plant_time in enumerate(plants_time):
                                if plant_time == 0 and plants_seat[a] == 3:
                                    plants_seat[a] = 0
                                    plants_time[a] = 1_000_000_000
                                    inventory[7] += 1
                                    inventory_text[7] = inventory_font.render(str(inventory[7]), True, (255, 255, 255))

            elif plants_seat[index] == 4:
                if plants_time[index] > 1000:
                    screen.blit(wheat_1, (x_position, y_position))
                elif plants_time[index] > 100:
                    screen.blit(wheat_2, (x_position, y_position))
                elif plants_time[index] > 0:
                    screen.blit(wheat_3, (x_position, y_position))
                else:
                    screen.blit(wheat_4, (x_position, y_position))

                    if (-815 - (field_num[0] - 3) * 110 < background_x_pos < -520 and 1855 < background_y_pos < 2125):
                        for a, plant_time in enumerate(plants_time):
                            if plant_time == 0 and plants_seat[a] == 4:
                                plants_seat[a] = 0
                                plants_time[a] = 1_000_000_000
                                inventory[9] += 1
                                inventory_text[9] = inventory_font.render(str(inventory[9]), True, (255, 255, 255))
                    elif woker_3_pos_jud == 0 and worker_3_jud == 1:
                        if target_x == target2_x and target_y == target2_y:
                            for a, plant_time in enumerate(plants_time):
                                if plant_time == 0 and plants_seat[a] == 4:
                                    plants_seat[a] = 0
                                    plants_time[a] = 1_000_000_000
                                    inventory[9] += 1
                                    inventory_text[9] = inventory_font.render(str(inventory[9]), True, (255, 255, 255))
                    elif worker_2_pos_jud == 0 and worker_2_jud == 1:
                        if target_x_2 == target2_x and target_y_2 == target2_y:
                            for a, plant_time in enumerate(plants_time):
                                if plant_time == 0 and plants_seat[a] == 4:
                                    plants_seat[a] = 0
                                    plants_time[a] = 1_000_000_000
                                    inventory[9] += 1
                                    inventory_text[9] = inventory_font.render(str(inventory[9]), True, (255, 255, 255))

    # 일꾼 3 그리기 (월드→스크린 변환 + 정수화)
    if (worker_3_jud == 1):
        worker_3_screen_x = int(background_x_pos + worker_3_world_x)
        worker_3_screen_y = int(background_y_pos + worker_3_world_y)
        screen.blit(worker_3, (worker_3_screen_x, worker_3_screen_y))
        screen.blit(flower_dic4, (worker_3_screen_x - 30, worker_3_screen_y - 50))
        K_1_text = UI_key_pont.render(str(": {}개".format(worker_3_flower[0])), True, (255, 255, 255))
        screen.blit(K_1_text, (worker_3_screen_x + 10, worker_3_screen_y - 40))
        screen.blit(seed_UI, (worker_3_screen_x - 30, worker_3_screen_y - 100))
        K_1_text = UI_key_pont.render(str(": {}개".format(worker_3_seed[0])), True, (255, 255, 255))
        screen.blit(K_1_text, (worker_3_screen_x + 10, worker_3_screen_y - 85))

    if (worker_2_jud == 1):
        worker_2_screen_x = int(background_x_pos + worker_2_world_x)
        worker_2_screen_y = int(background_y_pos + worker_2_world_y)
        screen.blit(worker_2, (worker_2_screen_x, worker_2_screen_y))
        screen.blit(flower_dic4, (worker_2_screen_x - 30, worker_2_screen_y - 50))
        K_1_text = UI_key_pont.render(str(": {}개".format(worker_2_flower[0])), True, (255, 255, 255))
        screen.blit(K_1_text, (worker_2_screen_x, worker_2_screen_y - 50))
        screen.blit(seed_UI, (worker_2_screen_x - 30, worker_2_screen_y - 100))
        K_1_text = UI_key_pont.render(str(": {}개".format(worker_2_seed[0])), True, (255, 255, 255))
        screen.blit(K_1_text, (worker_2_screen_x + 10, worker_2_screen_y - 85))
    
    if (worker_1_jud == 1):
        worker_1_screen_x = int(background_x_pos + worker_1_world_x)
        worker_1_screen_y = int(background_y_pos + worker_1_world_y)
        screen.blit(worker_1, (worker_1_screen_x, worker_1_screen_y))
        screen.blit(fish_UI, (worker_1_screen_x - 30, worker_1_screen_y - 50))
        K_1_text = UI_key_pont.render(str(": {}개".format(worker_1_fish[0])), True, (255, 255, 255))
        screen.blit(K_1_text, (worker_1_screen_x, worker_1_screen_y - 50))

    # 캐릭터
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.draw.rect(screen, (0, 0, 0), (character_x_pos - (maxhp / 2.9), character_y_pos - 30, maxhp, 15))
    pygame.draw.rect(screen, (255, 0, 0), (character_x_pos - (maxhp / 3.2), character_y_pos - 27.5, hp - 5, 10))

    
    if (worker_1_fish_jud == 0 and worker_1_jud == 1):
        screen.blit(fish_tool, ((background_x_pos + worker_1_world_x - 30, background_y_pos + worker_1_world_y - 20)))
    elif (worker_1_jud == 1):
            worker_1_fish_jud -= 1
            screen.blit(fish_tool2, ((background_x_pos + worker_1_world_x - 30, background_y_pos + worker_1_world_y - 20)))

    cul4 = 250
    if fish == 1:
        fish_x_pos = (screen_width / 2) - (character_width / 2)
        hp -= 0.5
        screen.blit(fish_tool, ((fish_x_pos - 30, fish_y_pos - 20)))
        pygame.display.update()
        cul = 205
        time.sleep(random.randint(1, 3))
        cul2 = 0
        fish_running = 1
        cul3 = -1
        fish_point = 0
        cul4 = 250
        while cul > 0:
            screen.blit(background_reset, (0, 0))
            screen.blit(background, (int(background_x_pos), int(background_y_pos)))
            screen.blit(background, (int(background_x_pos), int(background_y_pos - background_height)))
            screen.blit(background, (int(background_x_pos + background_width), int(background_y_pos)))
            screen.blit(background, (int(background_x_pos + background_width), int(background_y_pos - background_height)))
            screen.blit(fishing1, (int(background_x_pos), int(background_y_pos + 1680)))
            
            K_1_text = UI_key_pont.render(str(": 낚기"), True, (0, 0, 0))
            screen.blit(K_1_text, (1700, 797.5))
            screen.blit(Button_space_UI, (1550, 797.5))
            if (worker_1_jud == 1):
                worker_1_screen_x = int(background_x_pos + worker_1_world_x)
                worker_1_screen_y = int(background_y_pos + worker_1_world_y)
                screen.blit(worker_1, (worker_1_screen_x, worker_1_screen_y))
            screen.blit(character, (character_x_pos, character_y_pos))
            if cul2 == 0:
                fish_x_pos -= 10
            if cul2 == 1:
                fish_x_pos += 10
            if cul2 == 2:
                cul2 = -1
            if cul4 + fish_x_pul > 1720:
                cul3 = -1
            if cul4 + fish_x_pul < 250:
                cul3 = 1
            if cul3 < 0:
                fish_x_pul -= 100
            if cul3 > 0:
                fish_x_pul += 100
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if cul4 + fish_x_pul < 520 or cul4 + fish_x_pul >= 1420:
                            fish_ran = random.randint(1, 3)
                            if fish_ran == 1:
                                fish_point = 1
                                fish_ran = 0
                                inventory[2] = inventory[2] + 1
                                inventory_text[2] = (inventory_font.render(str(inventory[2]), True, (0, 0, 0)))
                            cul = 0
                        elif 520 <= cul4 + fish_x_pul < 820 or 1120 <= cul4 + fish_x_pul < 1420:
                            fish_ran = random.randint(1, 2)
                            if fish_ran == 1:
                                fish_point = 1
                                fish_ran = 0
                                inventory[2] = inventory[2] + 1
                                inventory_text[2] = (inventory_font.render(str(inventory[2]), True, (0, 0, 0)))
                            cul = 0
                        elif 820 <= cul4 + fish_x_pul < 1120:
                            fish_point = 1
                            inventory[2] = inventory[2] + 1
                            inventory_text[2] = (inventory_font.render(str(inventory[2]), True, (0, 0, 0)))
                            cul = 0
            screen.blit(fish_tool, ((fish_x_pos - 30, fish_y_pos - 20)))
            screen.blit(fish_gage_bar, ((cul4, fish_y_pos + 300)))
            screen.blit(fish_gage_bar_select, ((cul4 + fish_x_pul, fish_y_pos + 300)))
            cul2 += 1
            cul -= 1
            pygame.display.update()
            time.sleep(0.001)
        fish = 0
        cul2 = 0
        fish_x_pul = 0

    screen.blit(inventory_png, (315, 940))
    screen.blit(seed_png, (330, 960))
    screen.blit(flower_png, (455, 960))
    screen.blit(fish_png, (580, 960))
    screen.blit(ticket_UI, (705, 990))
    screen.blit(tomato_seed_UI, (830, 970))
    screen.blit(tomato_4, (955, 970))
    screen.blit(pumpkin_seed_UI, (1080, 970))
    screen.blit(pumpkin_4, (1205, 970))
    screen.blit(wheat_seed_UI, (1330, 970))
    screen.blit(wheat_4, (1455, 980))

    cul = 0
    for i in range(len(inventory_text)):
        x_pos = (screen_width / 2) - (character_width / 2) - 535 + cul * 125
        screen.blit(inventory_text[i], (x_pos, screen_height - 120))
        cul += 1

    if (-815 - (field_num[0] - 3) * 110 < background_x_pos < -520 and 1855 < background_y_pos < 2125 and inventory[0] > 0):
        K_1_text = UI_key_pont.render(str(": 해바라기 심기"), True, (0, 0, 0))
        screen.blit(K_1_text, (1700, 900))
        screen.blit(Button_1_UI, (1650, 897.5))

    if (background_y_pos < -900):
        K_1_text = UI_key_pont.render(str(": 낚시하기"), True, (0, 0, 0))
        screen.blit(K_1_text, (1700, 850))
        screen.blit(Button_f_UI, (1650, 847.5))
    
    if (-365 < background_x_pos < -225 and background_y_pos > 2150):
        K_1_text = UI_key_pont.render(str(": 상점"), True, (0, 0, 0))
        screen.blit(K_1_text, (1700, 850))
        screen.blit(Button_f_UI, (1650, 847.5))

    if (-665 < background_x_pos < -525 and background_y_pos > 2150):    
        K_1_text = UI_key_pont.render(str(": 노동자 고용소"), True, (0, 0, 0))
        screen.blit(K_1_text, (1700, 850))
        screen.blit(Button_f_UI, (1650, 847.5))

    if (-965 < background_x_pos < -825 and background_y_pos > 2150):    
        K_1_text = UI_key_pont.render(str(": 오락실"), True, (0, 0, 0))
        screen.blit(K_1_text, (1700, 850))
        screen.blit(Button_f_UI, (1650, 847.5))

    if (inventory[1] > 0):
        K_1_text = UI_key_pont.render(str(": 해바라기 먹기"), True, (0, 0, 0))
        screen.blit(K_1_text, (1700, 750))
        screen.blit(Button_2_UI, (1650, 747.5))

    if (inventory[2] > 0):
        K_1_text = UI_key_pont.render(str(": 물고기 먹기"), True, (0, 0, 0))
        screen.blit(K_1_text, (1700, 700))
        screen.blit(Button_3_UI, (1650, 697.5))

    cul = 0
    if store_jud == 1:
        
        store_UI_y_pos -= 100
        screen.blit(store_UI, (store_UI_x_pos - store_UI_width / 2, store_UI_y_pos - store_UI_height / 2))
        screen.blit(store_ESC, (store_UI_x_pos - store_UI_width / 2, store_UI_y_pos - store_UI_height / 2))
        store_UI_x_pos -= 90
        store_UI_y_pos -= 50

        if (store_index == 0):
            screen.blit(right_button, (store_UI_x_pos - store_UI_width / 2 + 1675, store_UI_y_pos - store_UI_height / 2 + 200 + 275))
            
            # 아이템 아이콘 표시
            screen.blit(flower_png, (store_UI_x_pos - store_UI_width / 2 + 90, store_UI_y_pos - store_UI_height / 2 + 230))
            screen.blit(seed_png, (store_UI_x_pos - store_UI_width / 2 + 90, store_UI_y_pos - store_UI_height / 2 + 480))
            screen.blit(fish_png, (store_UI_x_pos - store_UI_width / 2 + 90, store_UI_y_pos - store_UI_height / 2 + 730))
            screen.blit(field_png, (store_UI_x_pos - store_UI_width / 2 + 1000, store_UI_y_pos - store_UI_height / 2 + 230))
            screen.blit(ticket_UI, (store_UI_x_pos - store_UI_width / 2 + 1000, store_UI_y_pos - store_UI_height / 2 + 505))

            # 가격 텍스트 생성
            flower_buy_text = inventory_font.render("50 coin", True, (255, 255, 255))
            flower_sell_text = inventory_font.render("30 coin", True, (255, 255, 255))
            seed_buy_text = inventory_font.render("10 coin", True, (255, 255, 255))
            seed_sell_text = inventory_font.render("5 coin", True, (255, 255, 255))
            fish_buy_text = inventory_font.render("200 coin", True, (255, 255, 255))
            fish_sell_text = inventory_font.render("100 coin", True, (255, 255, 255))
            field_price = str(field_num[1] * 500) + " coin"
            field_buy_text = inventory_font.render(field_price, True, (255, 255, 255))
            ticket_buy_text = inventory_font.render("500 coin", True, (255, 255, 255))

            # 구매 및 판매 UI 그리기
            for i in range(3):  # 꽃, 씨앗, 물고기
                screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 190, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))
                screen.blit(store_UI_sell, (store_UI_x_pos - store_UI_width / 2 + 500, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))
                cul += 1
            cul = 0

            # 땅 구매 UI
            screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 1200, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))
            screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 1200, store_UI_y_pos - store_UI_height / 2 + 200 + 250))

            # 가격 텍스트 표시
            screen.blit(flower_buy_text, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 180))
            screen.blit(flower_sell_text, (store_UI_x_pos - store_UI_width / 2 + 510, store_UI_y_pos - store_UI_height / 2 + 180))
            screen.blit(seed_buy_text, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 430))
            screen.blit(seed_sell_text, (store_UI_x_pos - store_UI_width / 2 + 510, store_UI_y_pos - store_UI_height / 2 + 430))
            screen.blit(fish_buy_text, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 680))
            screen.blit(fish_sell_text, (store_UI_x_pos - store_UI_width / 2 + 510, store_UI_y_pos - store_UI_height / 2 + 680))
            screen.blit(field_buy_text, (store_UI_x_pos - store_UI_width / 2 + 1210, store_UI_y_pos - store_UI_height / 2 + 180))
            screen.blit(ticket_buy_text, (store_UI_x_pos - store_UI_width / 2 + 1210, store_UI_y_pos - store_UI_height / 2 + 430))
            
        else:
            screen.blit(left_button, (store_UI_x_pos - store_UI_width / 2 - 50, store_UI_y_pos - store_UI_height / 2 + 200 + 275))
            screen.blit(tomato_4, (store_UI_x_pos - store_UI_width / 2 + 90, store_UI_y_pos - store_UI_height / 2 + 230))
            screen.blit(tomato_seed_UI, (store_UI_x_pos - store_UI_width / 2 + 90, store_UI_y_pos - store_UI_height / 2 + 480))
            screen.blit(wheat_4, (store_UI_x_pos - store_UI_width / 2 + 90, store_UI_y_pos - store_UI_height / 2 + 730))
            screen.blit(wheat_seed_UI, (store_UI_x_pos - store_UI_width / 2 + 800, store_UI_y_pos - store_UI_height / 2 + 230))
            screen.blit(pumpkin_4, (store_UI_x_pos - store_UI_width / 2 + 800, store_UI_y_pos - store_UI_height / 2 + 480))
            screen.blit(pumpkin_seed_UI, (store_UI_x_pos - store_UI_width / 2 + 800, store_UI_y_pos - store_UI_height / 2 + 730))

            # 가격 텍스트 생성
            tomato_buy_text = inventory_font.render("100 coin", True, (255, 255, 255))
            tomato_sell_text = inventory_font.render("90 coin", True, (255, 255, 255))
            tomato_seed_buy_text = inventory_font.render("20 coin", True, (255, 255, 255))
            tomato_seed_sell_text = inventory_font.render("15 coin", True, (255, 255, 255))
            wheat_buy_text = inventory_font.render("200 coin", True, (255, 255, 255))
            wheat_sell_text = inventory_font.render("100 coin", True, (255, 255, 255))
            wheat_seed_buy_text = inventory_font.render("30 coin", True, (255, 255, 255))
            wheat_seed_sell_text = inventory_font.render("25 coin", True, (255, 255, 255))
            pumpkin_buy_text = inventory_font.render("250 coin", True, (255, 255, 255))
            pumpkin_sell_text = inventory_font.render("200 coin", True, (255, 255, 255))
            pumpkin_seed_buy_text = inventory_font.render("100 coin", True, (255, 255, 255))
            pumpkin_seed_sell_text = inventory_font.render("90 coin", True, (255, 255, 255))

            # 구매 및 판매 UI 그리기
            for i in range(3):  # 꽃, 씨앗, 물고기
                screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 190, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))
                screen.blit(store_UI_sell, (store_UI_x_pos - store_UI_width / 2 + 500, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))
                cul += 1
            cul = 0

            # 땅 구매 UI
            for i in range(3):  # 꽃, 씨앗, 물고기
                screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 900, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))
                screen.blit(store_UI_sell, (store_UI_x_pos - store_UI_width / 2 + 1210, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))
                cul += 1
            cul = 0

            # 가격 텍스트 표시
            screen.blit(tomato_buy_text, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 180))
            screen.blit(tomato_sell_text, (store_UI_x_pos - store_UI_width / 2 + 510, store_UI_y_pos - store_UI_height / 2 + 180))
            screen.blit(tomato_seed_buy_text, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 430))
            screen.blit(tomato_seed_sell_text, (store_UI_x_pos - store_UI_width / 2 + 510, store_UI_y_pos - store_UI_height / 2 + 430))
            screen.blit(wheat_buy_text, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 680))
            screen.blit(wheat_sell_text, (store_UI_x_pos - store_UI_width / 2 + 510, store_UI_y_pos - store_UI_height / 2 + 680))

            screen.blit(wheat_seed_buy_text, (store_UI_x_pos - store_UI_width / 2 + 910, store_UI_y_pos - store_UI_height / 2 + 180))
            screen.blit(wheat_seed_sell_text, (store_UI_x_pos - store_UI_width / 2 + 1220, store_UI_y_pos - store_UI_height / 2 + 180))
            screen.blit(pumpkin_buy_text, (store_UI_x_pos - store_UI_width / 2 + 910, store_UI_y_pos - store_UI_height / 2 + 430))
            screen.blit(pumpkin_sell_text, (store_UI_x_pos - store_UI_width / 2 + 1220, store_UI_y_pos - store_UI_height / 2 + 430))
            screen.blit(pumpkin_seed_buy_text, (store_UI_x_pos - store_UI_width / 2 + 910, store_UI_y_pos - store_UI_height / 2 + 680))
            screen.blit(pumpkin_seed_sell_text, (store_UI_x_pos - store_UI_width / 2 + 1220, store_UI_y_pos - store_UI_height / 2 + 680))
        
        # UI 위치 초기화
        store_UI_x_pos = 975
        store_UI_y_pos = 575

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭 누를 때
                # 스토어 UI 클릭 감지
                if store_UI_x_pos - store_UI_width / 2 < pygame.mouse.get_pos()[0] < store_UI_x_pos - store_UI_width / 2 + 100:
                    if store_UI_y_pos - store_UI_height / 2 - 100 < pygame.mouse.get_pos()[1] < store_UI_y_pos - store_UI_height / 2:
                        store_jud = 0

                if 1785 < pygame.mouse.get_pos()[0] < 1885 and 475 < pygame.mouse.get_pos()[1] < 575:
                    store_index = 1
                elif 60 < pygame.mouse.get_pos()[0] < 160 and 475 < pygame.mouse.get_pos()[1] < 575:
                    store_index = 0

                if (store_index == 0):
                    # 아이템 구매 및 판매 처리
                    for cul in range(3):  # 0: 꽃, 1: 씨앗, 2: 물고기
                        if 290 < pygame.mouse.get_pos()[0] < 590:  # buy 영역
                            if cul * 250 + 200 < pygame.mouse.get_pos()[1] < cul * 250 + 350:
                                if cul == 0:  # 꽃
                                    if coin >= 50:
                                        inventory[1] += 1
                                        coin -= 50
                                elif cul == 1:  # 씨앗
                                    if coin >= 10:
                                        inventory[0] += 1
                                        coin -= 10
                                elif cul == 2:  # 물고기
                                    if coin >= 200:
                                        inventory[2] += 1
                                        coin -= 200

                        elif 600 < pygame.mouse.get_pos()[0] < 900:  # sell 영역
                            if cul * 250 + 200 < pygame.mouse.get_pos()[1] < cul * 250 + 350:
                                if cul == 0:  # 꽃
                                    if inventory[1] >= 1:
                                        inventory[1] -= 1
                                        coin += 30
                                elif cul == 1:  # 씨앗
                                    if inventory[0] >= 1:
                                        inventory[0] -= 1
                                        coin += 5
                                elif cul == 2:  # 물고기
                                    if inventory[2] >= 1:
                                        inventory[2] -= 1
                                        coin += 100

                    # 땅 구매 처리
                    if 1300 < pygame.mouse.get_pos()[0] < 1600:  # buy 영역
                        if 200 < pygame.mouse.get_pos()[1] < 300:  # 땅 구매 클릭 영역
                            if field_num[0] == field_num[1]:
                                if field_num[1] * 500 <= coin:
                                    coin -= field_num[1] * 500
                                    field_num[0] += 1
                            else:
                                if field_num[0] * 500 <= coin:
                                    coin -= field_num[1] * 500
                                    field_num[1] += 1

                    if 1300 < pygame.mouse.get_pos()[0] < 1600:  # buy 영역
                        if 450 < pygame.mouse.get_pos()[1] < 550:  # ticket
                            if coin >= 500:
                                        inventory[3] += 1
                                        coin -= 500
                
                else:
                    for cul in range(3):
                        if 290 < pygame.mouse.get_pos()[0] < 590:  # buy 영역
                            if cul * 250 + 200 < pygame.mouse.get_pos()[1] < cul * 250 + 350:
                                if cul == 0:
                                    if coin >= 100:
                                        inventory[5] += 1
                                        coin -= 100
                                elif cul == 1:
                                    if coin >= 20:
                                        inventory[4] += 1
                                        coin -= 20
                                elif cul == 2:
                                    if coin >= 200:
                                        inventory[9] += 1
                                        coin -= 200

                        elif 600 < pygame.mouse.get_pos()[0] < 900:  # sell 영역
                            if cul * 250 + 200 < pygame.mouse.get_pos()[1] < cul * 250 + 350:
                                if cul == 0: 
                                    if inventory[5] >= 1:
                                        inventory[5] -= 1
                                        coin += 90
                                elif cul == 1:
                                    if inventory[4] >= 1:
                                        inventory[4] -= 1
                                        coin += 15
                                elif cul == 2:
                                    if inventory[9] >= 1:
                                        inventory[9] -= 1
                                        coin += 100

                    for cul in range(3):
                        if 1010 < pygame.mouse.get_pos()[0] < 1310:  # buy 영역
                            if cul * 250 + 200 < pygame.mouse.get_pos()[1] < cul * 250 + 350:
                                if cul == 0:
                                    if coin >= 30:
                                        inventory[8] += 1
                                        coin -= 30
                                elif cul == 1:
                                    if coin >= 250:
                                        inventory[7] += 1
                                        coin -= 250
                                elif cul == 2:
                                    if coin >= 100:
                                        inventory[6] += 1
                                        coin -= 100

                        elif 1310 < pygame.mouse.get_pos()[0] < 1610:  # sell 영역
                            if cul * 250 + 200 < pygame.mouse.get_pos()[1] < cul * 250 + 350:
                                if cul == 0: 
                                    if inventory[8] >= 1:
                                        inventory[8] -= 1
                                        coin += 25
                                elif cul == 1:
                                    if inventory[7] >= 1:
                                        inventory[7] -= 1
                                        coin += 200
                                elif cul == 2:
                                    if inventory[6] >= 1:
                                        inventory[6] -= 1
                                        coin += 90

    # 일 (워커 구입 UI)
    if work_jud == 1:
        store_UI_y_pos -= 100
        screen.blit(store_UI, (store_UI_x_pos - store_UI_width / 2, store_UI_y_pos - store_UI_height / 2))
        screen.blit(store_ESC, (store_UI_x_pos - store_UI_width / 2, store_UI_y_pos - store_UI_height / 2))
        store_UI_x_pos -= 90
        store_UI_y_pos -= 50

        # 아이템 아이콘 표시
        screen.blit(worker_3_UI, (store_UI_x_pos - store_UI_width / 2 + 115, store_UI_y_pos - store_UI_height / 2 + 230))
        screen.blit(worker_2_UI, (store_UI_x_pos - store_UI_width / 2 + 115, store_UI_y_pos - store_UI_height / 2 + 480))
        screen.blit(worker_1_UI, (store_UI_x_pos - store_UI_width / 2 + 115, store_UI_y_pos - store_UI_height / 2 + 730))

        # 가격 텍스트 생성
        worker_3_buy = inventory_font.render("1000 coin", True, (255, 255, 255))
        worker_2_buy = inventory_font.render("5000 coin", True, (255, 255, 255))
        worker_1_buy = inventory_font.render("15000 coin", True, (255, 255, 255))

        # 구매 UI 그리기
        if (worker_3_jud == 0):
            screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 190, store_UI_y_pos - store_UI_height / 2 + 200))
        else:
            screen.blit(store_UI_unbuy, (store_UI_x_pos - store_UI_width / 2 + 190, store_UI_y_pos - store_UI_height / 2 + 200))
        if (worker_3_jud == 0):
            screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 190, store_UI_y_pos - store_UI_height / 2 + 200 + 250))
        else:
            screen.blit(store_UI_unbuy, (store_UI_x_pos - store_UI_width / 2 + 190, store_UI_y_pos - store_UI_height / 2 + 200 + 250))
        if (worker_3_jud == 0):
            screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 190, store_UI_y_pos - store_UI_height / 2 + 200 + 500))
        else:
            screen.blit(store_UI_unbuy, (store_UI_x_pos - store_UI_width / 2 + 190, store_UI_y_pos - store_UI_height / 2 + 200 + 500))
        # 가격 텍스트 표시
        screen.blit(worker_3_buy, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 180))
        screen.blit(worker_2_buy, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 200 + 230))
        screen.blit(worker_1_buy, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 200 + 480))

        # UI 위치 초기화
        store_UI_x_pos = 975
        store_UI_y_pos = 575

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭 누를 때
                # 워크 UI 클릭 감지
                if store_UI_x_pos - store_UI_width / 2 < pygame.mouse.get_pos()[0] < store_UI_x_pos - store_UI_width / 2 + 100:
                    if store_UI_y_pos - store_UI_height / 2 - 100 < pygame.mouse.get_pos()[1] < store_UI_y_pos - store_UI_height / 2:
                        work_jud = 0

                for cul in range(3):
                    if 290 < pygame.mouse.get_pos()[0] < 590:  # buy 영역
                        if cul * 250 + 200 < pygame.mouse.get_pos()[1] < cul * 250 + 350:
                            if cul == 0 and worker_3_jud == 0: #일꾼3
                                if coin >= 1000:
                                    worker_3_jud = 1
                                    worker_3_seed[0] += 5
                                    coin -= 1000
                            elif cul == 1 and worker_2_jud == 0: #일꾼2
                                if coin >= 5000:
                                    worker_2_jud = 1
                                    worker_2_seed[0] += 5
                                    coin -= 5000
                            elif cul == 2 and worker_1_jud == 0: #일꾼1
                                if coin >= 15000:
                                    worker_1_jud = 1
                                    coin -= 15000

    if mini_game_jud == 1:
        store_UI_y_pos -= 100
        screen.blit(store_UI, (store_UI_x_pos - store_UI_width / 2, store_UI_y_pos - store_UI_height / 2))
        screen.blit(store_ESC, (store_UI_x_pos - store_UI_width / 2, store_UI_y_pos - store_UI_height / 2))
        store_UI_x_pos -= 90
        store_UI_y_pos -= 50

        # 아이템 아이콘 표시
        screen.blit(mini_game_1_UI, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 275))

        screen.blit(ticket_UI, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 200))

        screen.blit(play_button, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 600))

        # UI 위치 초기화
        store_UI_x_pos = 975
        store_UI_y_pos = 575

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭 누를 때
                # 워크 UI 클릭 감지
                if store_UI_x_pos - store_UI_width / 2 < pygame.mouse.get_pos()[0] < store_UI_x_pos - store_UI_width / 2 + 100:
                    if store_UI_y_pos - store_UI_height / 2 - 100 < pygame.mouse.get_pos()[1] < store_UI_y_pos - store_UI_height / 2:
                        mini_game_jud = 0

                if 315 < pygame.mouse.get_pos()[0] < 600:  # buy 영역
                    if 600 < pygame.mouse.get_pos()[1] < 750:
                        if inventory[3] > 0:
                                mini_game_1 = 1
                                inventory[3] -= 1

    screen.blit(coin_png, (1550, 10))  # 코인 그리기
    screen.blit(coin_text, (1650, 20))  # 코인 갯수 표시
    if gameover_sig == 1:  # 게임오버 표시
        screen.blit(gameover, (0, 0))
        screen.blit(gameover_text, (50, 450))
        hp += 50
        coin -= 100
        pygame.display.update()
        time.sleep(3)
        gameover_sig = 0

    # 화면에 그린 모든 내용 표시
    pygame.display.update()

# 게임 종료 후 정보를 JSON 파일에 저장
data = {
    "coin": coin,
    "seed": inventory[0],
    "flower": inventory[1],
    "fish": inventory[2],
    "field_x": field_num[0],
    "field_y": field_num[1],
    "hp": int(hp),
    "plants_time": plants_time,
    "plants_seat": plants_seat,
    "worker_3_jud": worker_3_jud,
    "worker_3_seed": worker_3_seed,
    "worker_3_flower": worker_3_flower,
    "worker_2_jud": worker_2_jud,
    "worker_2_seed": worker_2_seed,
    "worker_2_flower": worker_2_flower,
    "worker_1_jud": worker_1_jud,
    "worker_1_fish": worker_1_fish,
    "ticket" : inventory[3],
    "tomato" : tomato,
    "tomato_seed" : tomato_seed,
    "pumpkin" : pumpkin,
    "pumpkin_seed" : pumpkin_seed,
    "wheat" : wheat,
    "wheat_seed" : wheat_seed,
}
with open(save_file, "w", encoding="utf8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
pygame.quit()