import time

import pyautogui

"""
0: terminal
1: singleplayer
2: launch
3: respawn
4: save and exit
5: zombie screenshot
6: menu screenshot
7: loading screenshot
8: death screenshot
"""


def load_points(screen_file: str) -> list[list[int]]:
    coords = []
    with open(screen_file, "r") as f:
        for line in f:
            coords.append(list(map(int, line.strip().split(" "))))  # type: ignore

    return coords  # type: ignore


def get_color(x: int, y: int):
    pixel = pyautogui.pixel(x, y)
    return (pixel[0], pixel[1], pixel[2])


def check_mob(coords: list[list[int]]):
    color = get_color(coords[5][0], coords[5][1])
    red = color[0]
    green = color[1]
    blue = color[2]

    if red == 91 and green == 103 and blue == 182:
        return False
    return True


def check_menu(coords: list[list[int]]):
    color = get_color(coords[6][0], coords[6][1])
    red = color[0]
    green = color[1]
    blue = color[2]

    if red == 244 and green == 186 and blue == 0:
        return True
    return False


def check_loading(coords: list[list[int]]):
    color = get_color(coords[7][0], coords[7][1])
    red = color[0]
    green = color[1]
    blue = color[2]

    if red == 30 and green == 21 and blue == 15:
        return True
    return False


def check_death(coords: list[list[int]]):
    color = get_color(coords[8][0], coords[8][1])
    red = color[0]
    green = color[1]
    blue = color[2]

    if red > 100 and green < 90 and blue < 90:
        return True
    return False


def auto_restart(screen_file: str):
    coords = load_points(f"screens/{screen_file}")
    # load backup
    pyautogui.click(coords[0])
    pyautogui.click(coords[0])
    # pyautogui.typewrite("python3 reload.py starve_half_heart")
    pyautogui.press("UP")
    pyautogui.press("enter")
    # click singleplayer
    pyautogui.click(coords[1])
    pyautogui.click(coords[1])
    # click world
    pyautogui.click(coords[2])
    pyautogui.click(coords[2])
    # wait for load
    while not check_loading(coords):
        # print("waiting for loading")
        pass
    # wait for death
    # walk off edge
    # time.sleep(3.5)
    pyautogui.keyDown("s")
    while not check_death(coords):
        # print("waiting for death")
        pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    # click respawn
    time.sleep(1)
    pyautogui.click(coords[3])
    # check for zombiessss
    mob = False
    for _ in range(3):
        if check_mob(coords):
            mob = True
    # click escape
    pyautogui.press("esc")
    # if zombie, return and wait for user
    if mob:
        print("zombie found")
        return
    # else click save and quit
    pyautogui.click(coords[4])
    # restart
    auto_restart(screen_file)


# RUN BOTH TOGETHER
input("enter into your terminal: python3 reload.py { RELOAD_NAME }")
auto_restart("{ SCREEN_FILE }")
