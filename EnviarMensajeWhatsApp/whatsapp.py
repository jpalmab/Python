import pyautogui as pg
import time
import webbrowser
webbrowser.open('https://web.whatsapp.com/send?phone="+57NUMEROCEL+"&text=+TEXTO')

width,height = pg.size()    
pg.click(width/2,height/2)
time.sleep(2)
pg.press('enter')
pg.press('enter')
pg.press('enter')

time.sleep(4)
pg.hotkey('ctrl', 'w')
pg.press('enter')