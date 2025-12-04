import pyautogui
import time 
import warnings
import os
from pathlib import Path

debug = True

BUILDING_FILENAMES = ['test_building']
BUFF_IDS = ['fish_bowl', 'irma_basket', 'settler_add']
IMG_DIR = Path(f'{os.getcwd()}/img/')

def trollFunction():
    troll_string = 'twoja stara'
    window_coords = {'firefox_input_bar' : [902,57]}
    pyautogui.moveTo(window_coords['firefox_input_bar'][0],window_coords['firefox_input_bar'][1])
    pyautogui.click()
    pyautogui.write(troll_string, interval=0.25)

class SettlerBot:
    class Debug:
        @staticmethod
        def getCursorPos(duration):
            while duration>0:
                print(f'cursor pos={pyautogui.position()}')
                time.sleep(1)
                duration-=1

    @staticmethod
    def locateStarWindow():
        try:
            for i in range(2):
                star_win = pyautogui.locateOnScreen('star_menu.png', grayscale=False, confidence=0.75)
                pyautogui.moveTo(star_win.left+60, star_win.top+120)
                print(f'star menu window located at x={star_win.left}, y={star_win.top}.')
                pyautogui.drag(895-star_win.left,373-star_win.top, duration=2)
        except pyautogui.ImageNotFoundException:
            print('star menu window not found.')

    @staticmethod
    def imgIntegrityCheck():
        for i in BUFF_IDS:
            file_path = Path(f'{IMG_DIR}{i}.png')
            if file_path.is_file():
                print(f'plik dla "{i}" istnieje.')
            else: 
                print(f'! coś się zjebało. plik dla "{i}" nie istnieje. !')

    @staticmethod
    def starObjectLocate(buff_image):
        buff_image = f'img/{buff_image}.png'
        while True:
            try:
            #dostosuj parametr confidence dla poszcz. premii, aby nie mylił z innymi premiami
                target_image = pyautogui.locateOnScreen(buff_image, confidence=0.75)
                pyautogui.moveTo(target_image.left+20, target_image.top+20)
            except pyautogui.ImageNotFoundException:
                pyautogui.moveTo(1214,586)
                pyautogui.drag(0,60, duration=2)
                continue
            break

    @staticmethod
    # do poprawki (trzeba poprawić system rozszerzeń plików)
    def starObjectApply(buff_image, building_image):
        building_image = f'img/{building_image}.png'

        SettlerBot.starObjectLocate(buff_image)

        pyautogui.click(clicks=2, interval=1)
        try:
            target_building = pyautogui.locateOnScreen(building_image, grayscale=False ,confidence=0.5)
            pyautogui.moveTo(target_building.left+100, target_building.top+100)
            print('building found.')
        except pyautogui.ImageNotFoundException:
            print('building not found')
                

# 4 zoomy w tył
# 1214, 589

SettlerBot.locateStarWindow()
SettlerBot.starObjectApply('irma_basket', 'test_building')
# SettlerBot.Debug.getCursorPos(10)

