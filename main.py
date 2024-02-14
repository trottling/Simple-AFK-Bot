import random
import time
import threading

import pyautogui
import colorama
import keyboard

move_buttons = ["w", "a", "s", "d"]
cam_buttons = ["space", "ctrl", "shift"]
time_range_ms = [500, 2500]
move_range = [100, 1000]
sleep_time = 5
Is_bot_work = False
bot_thread = threading.Thread()


def change_bot_status():
    global Is_bot_work

    Is_bot_work = not Is_bot_work

    if Is_bot_work:
        print(f"{colorama.Fore.GREEN}Запуск бота")
        bot_thread.run()
    else:
        print(f"{colorama.Fore.YELLOW}Остановка бота")


def Afk_bot():
    while True:
        if not Is_bot_work:
            break

        mv_btn = random.choice(move_buttons)
        cm_bnt = random.choice(cam_buttons)

        pyautogui.keyDown(cm_bnt)
        pyautogui.keyDown(mv_btn)

        if not Is_bot_work:
            pyautogui.keyUp(cm_bnt)
            pyautogui.keyUp(mv_btn)
            break

        pyautogui.move(random.randint(move_range[0], move_range[1]), random.randint(move_range[0], move_range[1]), duration=random.randint(time_range_ms[0], time_range_ms[1]) / 1000, tween=pyautogui.easeInOutQuad)

        pyautogui.keyUp(cm_bnt)
        pyautogui.keyUp(mv_btn)

        if not Is_bot_work:
            break

        time.sleep(sleep_time)


if __name__ == "__main__":
    print("Запуск АФК бота...\n")

    colorama.init(autoreset=True)
    pyautogui.FAILSAFE = False
    bot_thread = threading.Thread(target=Afk_bot)
    keyboard.add_hotkey("alt+f12", change_bot_status)

    print(f"Нажмите {colorama.Fore.BLUE}Alt + F12{colorama.Style.RESET_ALL} для запуска или остановки\n")

    while True:
        keyboard.wait("alt+f12")
