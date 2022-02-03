import pyautogui as pg
import time
import webbrowser

contador = 0
for i in range(100):
    webbrowser.open('https://www.youtube.com/watch?v=rLk3RccDq8s&ab_channel=YefersonCossio')


    time.sleep(3)
    for i in range(26):
        pg.press('tab')

    pg.hotkey('ctrl', 'v')
    pg.hotkey('ctrl', 'enter')
    contador = contador + 1
    print("Ejecución número " + str(contador))
    time.sleep(4)

    pg.hotkey('ctrl', 'w')