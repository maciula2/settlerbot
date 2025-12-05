import pyautogui
import time 
import os
from pathlib import Path
import customtkinter


IMG_DIR = f'{os.getcwd()}/img/'

BUFF_IDS = ['irma_basket']
UI_COORDS = {'expand_settings_btn': (32, 467),
               'camera_settings_btn': (106, 475),
               'camera_window_default': (959,515),
               'camera_zoom_out_btn': (977, 587),
               'camera_up_btn': (960,526), # ? currently not in use
               'camera_down_btn': (960, 561), # ? currently not in use
               'camera_left_btn': (943, 543), # ? currently not in use
               'camera_right_btn': (977,543), # ? currently not in use
               'movement_mouse_reset': (944,158),
               'star_slider_default': (1902,767),
               'star_default': (1596,670),
               'chat_hide_btn': (315,769),
               'friends_hide_btn': (959,938)}

star_window_positioned = False


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
            file_path = Path(f'{IMG_DIR}{i}.png')
            if file_path.is_file():
                print(f'image file for "{i}" exists.')
            else: 
                print(f'! image file for "{i}" doesnt exist !')

    @staticmethod
    def cameraSetPos():
        pyautogui.click(UI_COORDS['expand_settings_btn'][0],UI_COORDS['expand_settings_btn'][1], duration=0.5)
        pyautogui.click(UI_COORDS['camera_settings_btn'][0],UI_COORDS['camera_settings_btn'][1], duration=0.5)
        pyautogui.moveTo(UI_COORDS['camera_zoom_out_btn'][0],UI_COORDS['camera_zoom_out_btn'][1], duration=0.5)
        pyautogui.click(clicks=10, interval=0.2)

    #Locates star menu window and drags it to a convenient position (bottom right corner).
    @staticmethod
    def starWindowLocate():
        pyautogui.click(UI_COORDS['friends_hide_btn'][0],UI_COORDS['friends_hide_btn'][1], duration=0.5)
        pyautogui.click(UI_COORDS['chat_hide_btn'][0],UI_COORDS['chat_hide_btn'][1],  duration=0.5)
        # max zoom out
        pyautogui.scroll(-10)
        try:
            # * Dragging must be done twice, as TSO window dragging response is delayed.
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
            # TODO: Add exclusive `confidence` parameter value for each image in the future to avoid recognition errors
                target_img = pyautogui.locateOnScreen(buff_img, confidence=0.8)
                pyautogui.moveTo(target_img.left+20, target_img.top+20)
            except pyautogui.ImageNotFoundException:
                pyautogui.moveTo(UI_COORDS['star_slider_default'][0], UI_COORDS['star_slider_default'][1])
                pyautogui.drag(0,70, duration=2)
                continue
            break

    @staticmethod
    # TODO: Create coordinates system based on map segments + navigation by keyboard clicks
    def starBuffApply(buff_img):
        SettlerBot.starBuffSelect(buff_img)
        pyautogui.click(clicks=2, interval=0.75)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry=("400x240")
        self.title="SettlerBot"

        self.selector = customtkinter.CTkComboBox(self, values=BUFF_IDS)
        self.selector.grid(row=0,column=0,padx=20,pady=20)

        # ! Remove before pushing
        SettlerBot.cameraSetPos()
        SettlerBot.starWindowLocate()
        SettlerBot.starBuffSelect('irma_basket')
        # SettlerBot.Debug.getCursorPos(10)

        # # * Move one map frame (y)
        # for i in range(4):
        #     pyautogui.moveTo(UI_COORDS['movement_mouse_reset'][0],UI_COORDS['movement_mouse_reset'][1], duration=0.3)
        #     pyautogui.drag(0,300,duration=0.3)
        
        # # * Move one map frame (x)
        # for i in range(4):
        #     pyautogui.moveTo(UI_COORDS['movement_mouse_reset'][0],UI_COORDS['movement_mouse_reset'][1], duration=0.3)
        #     pyautogui.drag(-600,0, duration=0.3)

        



app = App()
customtkinter.set_appearance_mode('Dark')

if __name__ == '__main__':
    app.mainloop()

