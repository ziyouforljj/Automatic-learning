import pyautogui
import time
import webbrowser

url = "https://js.cc-edu.cn/#/home-page"
webbrowser.open(url)

time.sleep(2)

pyautogui.click(832,124)

time.sleep(1)

pyautogui.click(924,413)

time.sleep(1)

pyautogui.click(486,718)

time.sleep(1)

pyautogui.click(1403,638)

time.sleep(1)

for i in range(21):
    pyautogui.click(1862,1008)

time.sleep(1)

pyautogui.click(508,211)

time.sleep(1)

pyautogui.click(1250,276)

import os
import time

# 定义一个变量来记录当前时间
start_time = time.time()

# 循环等待直到时间超过15秒
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    # 如果超过15秒，跳到下一个
    if elapsed_time > 15:
        pyautogui.click(1440,262)
        time.sleep(1)
        for i in range(21):
            pyautogui.click(1862, 1008)

        time.sleep(1)

        pyautogui.click(882,209)

        time.sleep(1)

        pyautogui.click(1250, 276)
        break  # 跳出循环

    # 稍作延迟，避免过度占用CPU
    time.sleep(0.1)