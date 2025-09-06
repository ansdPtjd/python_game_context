          
import sys
import subprocess
import pygame
import os
import json

def resource_path(relative_path):
    """실행 환경에 상관없이 리소스의 절대 경로를 반환한다."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

py_path = resource_path(os.path.dirname(__file__))
font_path = os.path.join(py_path, "Font")
pixel_pont_path = os.path.join(font_path, "neodgm.ttf")
image_path = os.path.join(py_path, "image")
save_path = (py_path + r'/save')
save_file = str(save_path + r'/save_data.json')

if os.path.exists(save_file):
    with open(save_file, "r", encoding="utf8") as f:
        data = json.load(f)
else:
    data = {}
jud = data.get("jud", 0)

           
background = pygame.image.load(os.path.join(image_path, "Horizon.png"))

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Horizon")

                                  
    try:
        game_font = pygame.font.Font(pixel_pont_path, 28)
    except Exception:
        game_font = pygame.font.SysFont(None, 28)

            
    button_text = game_font.render("touch to start", True, (255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False

                      
        screen.blit(background, (0, 0))
        screen.blit(button_text, (540, 690))
        pygame.display.update()

              
    pygame.quit()

    if (jud == 1):
        game_path = os.path.join(py_path, "game.py")
        subprocess.run([sys.executable, game_path], cwd=py_path)
        data = {
            "coin": 0,
            "seed": 5,
            "flower": 0,
            "fish": 0,
            "field_x": 3,
            "field_y": 3,
            "hp": 100,
            "plants_time": [
                0
            ],
            "plants_seat": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "worker_3_jud": 0,
            "worker_3_seed": [
                0,
                0,
                0,
                0
            ],
            "worker_3_flower": [
                0,
                0,
                0,
                0
            ],
            "worker_2_jud": 0,
            "worker_2_seed": [
                0,
                0,
                0,
                0
            ],
            "worker_2_flower": [
                0,
                0,
                0,
                0
            ],
            "worker_1_jud": 0,
            "worker_1_fish": 0,
            "ticket": 0,
            "tomato": 0,
            "tomato_seed": 0,
            "pumpkin": 0,
            "pumpkin_seed": 0,
            "wheat": 0,
            "wheat_seed": 0,
            "jud": 0,
            "god": 0,
            "bed": 0
        }
        with open(save_file, "w", encoding="utf8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        game_path = os.path.join(py_path, "intro.py")
        subprocess.run([sys.executable, game_path], cwd=py_path)
        data = {
            "coin": 0,
            "seed": 5,
            "flower": 0,
            "fish": 0,
            "field_x": 3,
            "field_y": 3,
            "hp": 100,
            "plants_time": [
                0
            ],
            "plants_seat": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "worker_3_jud": 0,
            "worker_3_seed": [
                0,
                0,
                0,
                0
            ],
            "worker_3_flower": [
                0,
                0,
                0,
                0
            ],
            "worker_2_jud": 0,
            "worker_2_seed": [
                0,
                0,
                0,
                0
            ],
            "worker_2_flower": [
                0,
                0,
                0,
                0
            ],
            "worker_1_jud": 0,
            "worker_1_fish": 0,
            "ticket": 0,
            "tomato": 0,
            "tomato_seed": 0,
            "pumpkin": 0,
            "pumpkin_seed": 0,
            "wheat": 0,
            "wheat_seed": 0,
            "jud": 1,
            "god": 0,
            "bed": 0
                }
        with open(save_file, "w", encoding="utf8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
