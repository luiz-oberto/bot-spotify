import pyautogui
from time import sleep


### MEU EXERCÍCIO: vamos passar uma música no spotify a cada 10 segundos
# 1 - clicar em uma playlist
pyautogui.click(0,0, duration=2.0)
# 2 - clicar em uma música
pyautogui.click(0,0, duration=2.0)
for i in range(10):
    # 3 - esperar 10 segundos
    sleep(11)
    # 4 - passar para a próxima música
    pyautogui.click(0,0, duration=2.0)

# 5 - repetir os passos 3 e 4
