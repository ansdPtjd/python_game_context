# 게임 배경 크기 3960*2160 4개
# 캐릭터 크기 30*50
import os
import pygame
import time
import random
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 1980 # 가로 크기
screen_height = 1080 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("힐링 게임")

# FPS
clock = pygame.time.Clock()
##############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
py_path = os.path.dirname(__file__) # 현재 파일의 위치 반환 
image_path = str(py_path + r'/image')
save_path = (py_path + r'/save')
font_path = (py_path + r'/Font')
music_path = (py_path + r'/music')
pixel_pont_path = str(font_path + r'/neodgm.ttf')
coin_path = str(save_path + r'/coin.txt')
seed_path = str(save_path + r'/seed.txt')
flower_path = str(save_path + r'/flower.txt')
fish_path = str(save_path + r'/fish.txt')
field_x_path = str(save_path + r'/field_x.txt')
field_y_path = str(save_path + r'/field_y.txt')
flower_time = str(save_path + r'/flower_time.txt')

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
flower_dic = pygame.image.load(os.path.join(image_path, "flower1.png"))
flower_dic2 = pygame.image.load(os.path.join(image_path, "flower2.png"))
flower_dic3 = pygame.image.load(os.path.join(image_path, "flower3.png"))
flower_dic4 = pygame.image.load(os.path.join(image_path, "flower4.png"))
sand2 = pygame.image.load(os.path.join(image_path, "sand2.png"))
house = pygame.image.load(os.path.join(image_path, "house.png"))
fish_gage_bar = pygame.image.load(os.path.join(image_path, "gage_bar.png"))
fish_gage_bar_select = pygame.image.load(os.path.join(image_path, "gage_bar_select.png"))
store = pygame.image.load(os.path.join(image_path, "store.png"))
character = pygame.image.load(os.path.join(image_path, "character.png"))
fish_tool = pygame.image.load(os.path.join(image_path, "fish_tool.png"))
coin_png = pygame.image.load(os.path.join(image_path, "coin.png"))
inventory_png = pygame.image.load(os.path.join(image_path, "inventory.png"))
seed_png = pygame.image.load(os.path.join(image_path, "seed.png"))
flower_png = pygame.image.load(os.path.join(image_path, "flower5.png"))
fish_png = pygame.image.load(os.path.join(image_path, "fish.png"))
field_png = pygame.image.load(os.path.join(image_path, "field.png"))
store_ESC = pygame.image.load(os.path.join(image_path, "ESC.png"))
store_UI_buy = pygame.image.load(os.path.join(image_path, "store_UI_buy.png"))
store_UI_sell = pygame.image.load(os.path.join(image_path, "store_UI_sell.png"))
store_UI = pygame.image.load(os.path.join(image_path, "store_ui.png"))
press = pygame.image.load(os.path.join(image_path, "press.png")) 

# 저장 내용 불러오기
with open (field_x_path, "r", encoding="utf8") as f:
    field_x = int(f.read())
with open (field_y_path, "r", encoding="utf8") as f:
    field_y = int(f.read())
with open (seed_path, "r", encoding="utf8") as f:
    seed = int(f.read())
with open (flower_path, "r", encoding="utf8") as f:
    flower = int(f.read())
with open (fish_path, "r", encoding="utf8") as f:
    fish = int(f.read())
with open (coin_path, "r", encoding="utf8") as f:
    coin = float(f.read())
    coin = int(coin)

# Font 정의
game_font = pygame.font.Font(pixel_pont_path, 100)
gameover_font = pygame.font.Font(pixel_pont_path, 100)
inventory_font = pygame.font.Font(pixel_pont_path, 25)
UI_font = pygame.font.Font(pixel_pont_path, 50)
gameover_text = gameover_font.render(str("[피로도에 의해 캐릭터가 기절했습니다.]"), True, (255, 0, 0))
press_button = 0
UI_text = gameover_font.render(str("Press {0}".format(str(press_button))), True, (0, 0, 0))

# 리스트
field_num = [field_x,field_y]
plants_time = []
plants_seat = []
inventory = [seed, flower, fish, 0, 0, 0, 0, 0, 0] # 꽃 씨앗, 꽃, 물고기
inventory_text = []
inventory_text.append(inventory_font.render(str(5), True, (255, 255, 255)))
inventory_text.append(inventory_font.render(str(0), True, (255, 255, 255)))
inventory_text.append(inventory_font.render(str(0), True, (255, 255, 255)))

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
maxhp = 100
hp = 100
to_x = 0
to_y = 0
background_speed = 1


# 배경음악
# background_sound = pygame.mixer.Sound(os.path.join(music_path, "background.mp3"))
# background_sound.play(-1)

running = True
while running:
    dt = clock.tick(144)  # FPS 설정
    coin_text = game_font.render(str(coin), True, (255, 255, 255))

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
    for i in range(3):
        inventory_text[i] = inventory_font.render(str(inventory[i]), True, (255, 255, 255))

        
    # 2. 이벤트 처리 (키보드, 마우스 등)
    cul = 0
    for event in pygame.event.get():  # 이벤트가 진행중인가?
        if event.type == pygame.QUIT:  # 이벤트가 QUIT인가
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            hp -= 0.01  # 체력 감소
            
            # 캐릭터 이동
            if event.key == pygame.K_a:  # 캐릭터를 왼쪽으로
                to_x += background_speed
            elif event.key == pygame.K_d:  # 캐릭터를 오른쪽으로
                to_x -= background_speed
            elif event.key == pygame.K_w:  # 캐릭터를 위로
                to_y += background_speed
            elif event.key == pygame.K_s:  # 캐릭터를 아래로
                to_y -= background_speed
            
            # 꽃 심기
            if event.key == pygame.K_1:
                if -520 - field_num[0] * 100 < background_x_pos < -520 and 1855 - field_num[1] * 100 < background_y_pos < 2125:
                    if inventory[0] > 0:
                        for cul in range(field_num[0] * field_num[1]):
                            if plants_seat[cul] == 0:  # 현재 좌석이 비어있다면
                                plants_seat[cul] = 1
                                if len(plants_time) <= cul:
                                    plants_time.append(0)
                                plants_time[cul] = 1500  # 약 30초
                                hp -= 0.5
                                inventory[0] -= 1
                                inventory_text[0] = inventory_font.render(str(inventory[0]), True, (255, 255, 255))
                                break

            # 낚시
            if event.key == pygame.K_f:
                if background_y_pos < -900:
                    fish = 1
                elif -365 < background_x_pos < -225:
                    store_jud = 1
            
            # 체력 회복 아이템 사용
            if event.key == pygame.K_2:
                if inventory[1] >= 1 and hp < 100:
                    hp += 1
                    inventory[1] -= 1
                    
            elif event.key == pygame.K_3:  # 추가적인 체력 회복
                if inventory[2] >= 1 and hp < 100:
                    hp += 2
                    inventory[2] -= 1

        if event.type == pygame.KEYUP:  # 방향키 뗄 때 멈춤
            if event.key in [pygame.K_a, pygame.K_d]:
                to_x = 0
            elif event.key in [pygame.K_w, pygame.K_s]:
                to_y = 0

    background_x_pos += to_x * dt # FPS가 달라짐에 따라 속도가 변하는 것을 방지
    background_y_pos += to_y * dt

    # 3. 게임 배경 위치 정의
    # 배경 X 좌표 제한
    background_x_pos = max(-5840, min(background_x_pos, 0))

    # 배경 Y 좌표 제한
    background_y_pos = max(-1080, min(background_y_pos, 2160))

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0)) # 배경 초기화
    screen.blit(background, (background_x_pos, background_y_pos)) # 배경
    screen.blit(background, (background_x_pos, background_y_pos - background_height))
    screen.blit(background, (background_x_pos + background_width, background_y_pos))
    screen.blit(background, (background_x_pos + background_width, background_y_pos - background_height))
    screen.blit(fishing1, (background_x_pos, background_y_pos + 1680)) # 강
    screen.blit(sand2, (background_x_pos + 865, background_y_pos - 1800))
    screen.blit(house, (background_x_pos + 865, background_y_pos - 1800)) # 집 그리기
    screen.blit(sand2, (background_x_pos + 1165, background_y_pos - 1800))
    screen.blit(store, (background_x_pos + 1165, background_y_pos - 1800)) # 가게 그리기

    for d in range(field_num[1]):  # 밭 그리기
        for e in range(field_num[0]):
            screen.blit(field_dic, (background_x_pos + 1500 + e * 100, background_y_pos - 1560 + d * 100))

    for d in range(field_num[1]):  # 꽃 그리기
        for e in range(field_num[0]):
            index = d * field_num[0] + e
            x_position = background_x_pos + 1500 + e * 105
            y_position = background_y_pos - background_height + 600 + d * 100
            
            if plants_seat[index] == 1:
                if plants_time[index] > 1000:
                    screen.blit(flower_dic, (x_position, y_position))
                elif plants_time[index] > 100:
                    screen.blit(flower_dic2, (x_position, y_position))
                elif plants_time[index] > 0:
                    screen.blit(flower_dic3, (x_position, y_position))
                else:
                    screen.blit(flower_dic4, (x_position, y_position))
                    
                    if (-815 - (field_num[0] - 3) * 110 < background_x_pos < -520 and
                            1855 < background_y_pos < 2125):
                        for a, plant_time in enumerate(plants_time):
                            if plant_time == 0:
                                plants_seat[a] = 0
                                plants_time[a] = 1_000_000_000  # 오류 방지
                                inventory[1] += 1
                                inventory_text[1] = inventory_font.render(str(inventory[1]), True, (255, 255, 255))
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터를 그리기
    pygame.draw.rect(screen, (0 ,0 ,0), (character_x_pos - (maxhp / 2.9) , character_y_pos - 30, maxhp, 15)) # hp바 배경
    pygame.draw.rect(screen, (255 ,0 ,0), (character_x_pos - (maxhp / 3.2) , character_y_pos - 27.5, hp - 5, 10)) # hp바 표시
    
    
    cul4 = 250
    if fish == 1 :
        fish_x_pos = (screen_width / 2) - (character_width / 2)
        hp -= 0.5
        screen.blit(fish_tool,((fish_x_pos - 30, fish_y_pos - 20)))
        pygame.display.update()
        cul = 205
        time.sleep(random.randint(1,3))
        cul2 = 0
        fish_running = 1
        cul3 = -1
        fish_point = 0
        cul4 = 250
        while cul > 0:
            if -520 - field_num[0] * 100 < background_x_pos < -520 and 1855 - field_num[1] * 100 < background_y_pos < 2125:
                press_button = 'l;,,.space bar'
                UI_text = UI_font.render(str("Press {0} button".format(str(press_button))), True, (0, 0, 0))
                screen.blit(UI_text, (character_x_pos + 50, character_y_pos))
            screen.blit(background_reset, (0,0))
            screen.blit(background, (background_x_pos, background_y_pos))
            screen.blit(background, (background_x_pos, background_y_pos - background_height))
            screen.blit(background, (background_x_pos + background_width, background_y_pos))
            screen.blit(background, (background_x_pos + background_width, background_y_pos - background_height))
            screen.blit(fishing1, (background_x_pos, background_y_pos + 1680))
            screen.blit(character, (character_x_pos, character_y_pos))
            if cul2 == 0:
                fish_x_pos -= 10
            if cul2 == 1:
                fish_x_pos += 10
            if cul2 == 2:
                cul2 = -1
            if cul4 + fish_x_pul> 1720:
                cul3 = -1
            if  cul4 + fish_x_pul < 250:
                cul3 = 1
            if cul3 < 0:
                fish_x_pul -= 100
            if cul3 > 0:
                fish_x_pul += 100
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if cul4 + fish_x_pul < 520 or cul4 + fish_x_pul >= 1420:
                            fish_ran = random.randint(1,3)
                            if fish_ran == 1:
                                fish_point = 1
                                fish_ran = 0
                                inventory[2] = inventory[2] + 1
                                inventory_text[2] = (inventory_font.render(str(inventory[2]), True, (0, 0, 0)))
                            cul = 0
                        elif 520 <= cul4 + fish_x_pul < 820 or 1120 <= cul4 + fish_x_pul < 1420:
                            fish_ran = random.randint(1,2)
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
            screen.blit(fish_tool,((fish_x_pos - 30, fish_y_pos - 20)))
            screen.blit(fish_gage_bar, ((cul4, fish_y_pos + 300)))
            screen.blit(fish_gage_bar_select, ((cul4 + fish_x_pul, fish_y_pos + 300)))
            cul2 += 1
            cul -= 1
            pygame.display.update()
            time.sleep(0.001)
        fish = 0
        cul2 = 0
        fish_x_pul = 0
    
    screen.blit(inventory_png, ((screen_width / 2) - (character_width / 2) - 630, screen_height - 140))
    screen.blit(seed_png, ((screen_width / 2) - (character_width / 2) - 630 + 15, 0 + screen_height - 120))
    screen.blit(flower_png, ((screen_width / 2) - (character_width / 2) - 630 + 140, 0 + screen_height - 120))
    screen.blit(fish_png, ((screen_width / 2) - (character_width / 2) - 630 + 275, 0 + screen_height - 120))    
    
    cul = 0
    for i in range(len(inventory_text)):
        x_pos = (screen_width / 2) - (character_width / 2) - 535 + cul * 125
        screen.blit(inventory_text[i], (x_pos, screen_height - 120))
        cul += 1
    
    cul = 0
    if store_jud == 1:
        store_UI_y_pos -= 100
        screen.blit(store_UI, (store_UI_x_pos - store_UI_width / 2, store_UI_y_pos - store_UI_height / 2))
        screen.blit(store_ESC, (store_UI_x_pos - store_UI_width / 2, store_UI_y_pos - store_UI_height / 2))
        store_UI_x_pos -= 90
        store_UI_y_pos -= 50
        
        # 아이템 아이콘 표시
        screen.blit(flower_png, (store_UI_x_pos - store_UI_width / 2 + 90, store_UI_y_pos - store_UI_height / 2 + 230))
        screen.blit(seed_png, (store_UI_x_pos - store_UI_width / 2 + 90, store_UI_y_pos - store_UI_height / 2 + 480))
        screen.blit(fish_png, (store_UI_x_pos - store_UI_width / 2 + 90, store_UI_y_pos - store_UI_height / 2 + 730))
        screen.blit(field_png, (store_UI_x_pos - store_UI_width / 2 + 1000, store_UI_y_pos - store_UI_height / 2 + 230))
        
        # 가격 텍스트 생성
        flower_buy_text = inventory_font.render("100 coin", True, (255, 255, 255))
        flower_sell_text = inventory_font.render("90 coin", True, (255, 255, 255))
        seed_buy_text = inventory_font.render("10 coin", True, (255, 255, 255))
        seed_sell_text = inventory_font.render("5 coin", True, (255, 255, 255))
        fish_buy_text = inventory_font.render("300 coin", True, (255, 255, 255))
        fish_sell_text = inventory_font.render("250 coin", True, (255, 255, 255))
        field_price = str(field_num[1] * 500) + " coin"
        field_buy_text = inventory_font.render(field_price, True, (255, 255, 255))
        
        # 구매 및 판매 UI 그리기
        for i in range(3):  # 꽃, 씨앗, 물고기
            screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 190, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))
            screen.blit(store_UI_sell, (store_UI_x_pos - store_UI_width / 2 + 500, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))
            cul += 1
        cul = 0

        # 땅 구매 UI
        screen.blit(store_UI_buy, (store_UI_x_pos - store_UI_width / 2 + 1200, store_UI_y_pos - store_UI_height / 2 + 200 + cul * 250))

        # 가격 텍스트 표시
        screen.blit(flower_buy_text, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 180))
        screen.blit(flower_sell_text, (store_UI_x_pos - store_UI_width / 2 + 510, store_UI_y_pos - store_UI_height / 2 + 180))
        screen.blit(seed_buy_text, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 200 + 230))
        screen.blit(seed_sell_text, (store_UI_x_pos - store_UI_width / 2 + 510, store_UI_y_pos - store_UI_height / 2 + 200 + 230))
        screen.blit(fish_buy_text, (store_UI_x_pos - store_UI_width / 2 + 200, store_UI_y_pos - store_UI_height / 2 + 200 + 480))
        screen.blit(fish_sell_text, (store_UI_x_pos - store_UI_width / 2 + 510, store_UI_y_pos - store_UI_height / 2 + 200 + 480))
        screen.blit(field_buy_text, (store_UI_x_pos - store_UI_width / 2 + 1210, store_UI_y_pos - store_UI_height / 2 + 180))

        # UI 위치 초기화
        store_UI_x_pos = 975
        store_UI_y_pos = 575

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭 누를 때
                # 스토어 UI 클릭 감지
                if store_UI_x_pos - store_UI_width / 2 < pygame.mouse.get_pos()[0] < store_UI_x_pos - store_UI_width / 2 + 100:
                    if store_UI_y_pos - store_UI_height / 2 - 100 < pygame.mouse.get_pos()[1] < store_UI_y_pos - store_UI_height / 2:
                        store_jud = 0
                
                # 아이템 구매 및 판매 처리
                for cul in range(3):  # 0: 꽃, 1: 씨앗, 2: 물고기
                    if 290 < pygame.mouse.get_pos()[0] < 590:  # buy 영역
                        if cul * 250 + 200 < pygame.mouse.get_pos()[1] < cul * 250 + 350:
                            if cul == 0:  # 꽃
                                if coin >= 100:
                                    inventory[1] += 1
                                    coin -= 100
                            elif cul == 1:  # 씨앗
                                if coin >= 10:
                                    inventory[0] += 1
                                    coin -= 10
                            elif cul == 2:  # 물고기
                                if coin >= 300:
                                    inventory[2] += 1
                                    coin -= 300
                    
                    elif 600 < pygame.mouse.get_pos()[0] < 900:  # sell 영역
                        if cul * 250 + 200 < pygame.mouse.get_pos()[1] < cul * 250 + 350:
                            if cul == 0:  # 꽃
                                if inventory[1] >= 1:
                                    inventory[1] -= 1
                                    coin += 90
                            elif cul == 1:  # 씨앗
                                if inventory[0] >= 1:
                                    inventory[0] -= 1
                                    coin += 5
                            elif cul == 2:  # 물고기
                                if inventory[2] >= 1:
                                    inventory[2] -= 1
                                    coin += 250

                # 땅 구매 처리
                if 1200 < pygame.mouse.get_pos()[0] < 1500:  # buy 영역
                    if 200 < pygame.mouse.get_pos()[1] < 300:  # 땅 구매 클릭 영역
                        if field_num[0] == field_num[1]:
                            if field_num[1] * 500 <= coin:
                                coin -= field_num[1] * 500
                                field_num[0] += 1
                        else:
                            if field_num[0] * 500 <= coin:
                                coin -= field_num[1] * 500
                                field_num[1] += 1

    if -520 - field_num[0] * 100 < background_x_pos < -520 and 1855 - field_num[1] * 100 < background_y_pos < 2125:
        press_button = 1
        UI_text = UI_font.render(str("Press {0} button".format(str(press_button))), True, (0, 0, 0))
        screen.blit(UI_text, (character_x_pos + 50, character_y_pos))

    screen.blit(coin_png, (1550,10)) # 코인 그리기
    screen.blit(coin_text, (1650,20)) # 코인 갯수 표시
    if gameover_sig == 1: # 게임오버가 되었을 때 게임오버 표시
        screen.blit(gameover, (0,0))
        screen.blit(gameover_text, (50, 450))
        hp += 50
        coin -= 100
        pygame.display.update()
        time.sleep(3)
        gameover_sig = 0

    pygame.display.update()
with open (coin_path, "w", encoding="utf8") as f:
    f.write(str(coin))
with open (seed_path, "w", encoding="utf8") as f:
    f.write(str(inventory[0]))
with open (flower_path, "w", encoding="utf8") as f:
    f.write(str(inventory[1]))
with open (fish_path, "w", encoding="utf8") as f:
    f.write(str(inventory[2]))
with open (field_x_path, "w", encoding="utf8") as f:
    f.write(str(field_num[0]))
with open (field_y_path, "w", encoding="utf8") as f:
    f.write(str(field_num[1]))
pygame.quit() # 게임 종료