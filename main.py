import pyautogui
import time 
import os
from pathlib import Path

IMG_DIR = f'{os.getcwd()}/img/'

BUFF_IDS = ['irma_basket']
UI_COORDS = {'expand_settings_btn': (32, 467),
               'camera_settings_btn': (106, 475),
               'star_slider_default': (1902,767),
               'star_default': (1596,670)}


class SettlerBot:

    class Debug:

        @staticmethod
        def getCursorPos(duration):
            while duration>0:
                print(f'cursor position={pyautogui.position()}')
                time.sleep(1)
                duration-=1
        
    @staticmethod
    def imgIntegrityCheck():
        for i in BUFF_IDS:
            file_path = Path(f'{IMG_DIR}+{i}.png')
            if file_path.is_file():
                print(f'image file for "{i}" exists.')
            else: 
                print(f'! image file for "{i}" doesnt exist !')

    #Locates star menu window and drags it to a convenient position (bottom right corner).
    @staticmethod
    def starWindowLocate():
        # max zoom out
        pyautogui.scroll(-10)
        try:
            # Dragging must be done twice, as TSO window dragging response is delayed.
            for i in range(2):
                star_window = pyautogui.locateOnScreen(IMG_DIR+'star_menu.png', grayscale=False, confidence=0.6)
                pyautogui.moveTo(star_window.left+40, star_window.top+150)
                pyautogui.dragTo(UI_COORDS['star_default'][0], UI_COORDS['star_default'][1], duration=2)
        except pyautogui.ImageNotFoundException:
            print('star menu window not found.')

    @staticmethod
    def starBuffSelect(buff_img):
        buff_img = IMG_DIR+f'{buff_img}.png'
        while True:
            try:
            # + Add exclusive `confidence` parameter value for each image in the future to avoid recognition errors
                target_img = pyautogui.locateOnScreen(buff_img, confidence=0.8)
                pyautogui.moveTo(target_img.left+20, target_img.top+20)
            except pyautogui.ImageNotFoundException:
                pyautogui.moveTo(UI_COORDS['star_slider_default'][0], UI_COORDS['star_slider_default'][1])
                pyautogui.drag(0,70, duration=2)
                continue
            break

    @staticmethod
    # Create building map system utilizing fixed coordinates stored in json files.
    def starBuffApply(buff_img):
        SettlerBot.starBuffSelect(buff_img)
        pyautogui.click(clicks=2, interval=0.75)


if __name__ == '__main__':
    SettlerBot.starWindowLocate()
