import logging
import pyautogui
import time


def log_testing():
    # 此处进行Logging.basicConfig() 设置，后面设置无效
    # logging.basicConfig(filename='log.txt',
    #                     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
    #                     level=logging.INFO)
    logging.basicConfig(level=logging.INFO)
    time.sleep(2)
    # logging.info(pyautogui.pixel(405,1369) == (40, 64, 60))
    # return

    while True:
        if not pyautogui.getActiveWindowTitle().startswith("觅长生"):
            time.sleep(1)
            continue
            # return
        if pyautogui.pixel(405,1369) != (40, 64, 60):
            time.sleep(1)
            continue

        pyautogui.press('D')
        time.sleep(0.01)
        if try_cast(Spell.k3):
            continue
        if try_cast(Spell.kr):
            continue
        if try_cast(Spell.k2):
            continue
        if try_cast(Spell.kt):
            continue
        if try_cast(Spell.k1):
            continue
        if try_cast(Spell.k5):
            continue
        if try_cast(Spell.k4):
            continue
        if try_cast(Spell.kq):
            continue
        if try_cast(Spell.k3):
            continue
        pyautogui.press('D')
        time.sleep(0.01)
        pyautogui.press('Esc')
        wait_rival()


def try_cast(key):
    pixel = pyautogui.pixel(key.value["point"][0], key.value["point"][1])
    if pixel != key.value["color"]:
        return False
    pyautogui.press(key.value["key"])
    time.sleep(0.01)
    if pyautogui.pixelMatchesColor(1319, 1052, (199, 97, 36)):
        pyautogui.press('space')
        time.sleep(0.2)
        return True
    else:
        logging.info(pyautogui.pixel(1319, 1052))
        return False


def wait_rival():
    not_ready = True

    while not_ready:
        if pyautogui.pixelMatchesColor(1156, 1120, (77, 89, 66)):
            time.sleep(0.5)
        else:
            not_ready = False

from enum import Enum


class Spell(Enum):
    # 547,1210  91D7EB
    # 660,1206  9BE5F9
    # 769,1209  94DBEF
    # 881,1209  72A4BC
    # 993,1211  74A3B0

    # 545,1320  9AE5F9
    # 656,1322  9BE6FA
    # 763,1322  82BECF
    # 880,1326  89CBDB
    # 988,1321  9BE6FA




    k1 = {'key': '1', 'point': (547,1210), 'color': (235, 215, 145)}
    k2 = {'key': '2', 'point': (660,1207), 'color': (250, 230, 155)}
    k3 = {'key': '3', 'point': (769,1209), 'color': (239, 219, 148)}
    k4 = {'key': '4', 'point': (881,1209), 'color': (188, 164, 114)}
    k5 = {'key': '5', 'point': (993,1211), 'color': (176, 163, 116)}

    kq = {'key': 'q', 'point': (545,1320), 'color': (249, 229, 155)}
    kw = {'key': 'w', 'point': (656,1322), 'color': (250, 230, 155)}
    ke = {'key': 'e', 'point': (763,1322), 'color': (207, 190, 130)}
    kr = {'key': 'r', 'point': (880,1326), 'color': (219, 203, 137)}
    kt = {'key': 't', 'point': (988,1321), 'color': (250, 230, 155)}


log_testing()
