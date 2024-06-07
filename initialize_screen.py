import pyautogui


def define_points():
    screen_file = input("enter screen file name: ")
    input("move to zombie screenshot")
    zombie_screenshot = pyautogui.position()
    input("move to menu screenshot")
    menu_screenshot = pyautogui.position()
    input("move to loading screenshot")
    loading_screenshot = pyautogui.position()
    input("move to death screenshot")
    death_screenshot = pyautogui.position()
    input("move to terminal")
    terminal = pyautogui.position()
    input("move to singleplayer")
    singleplayer = pyautogui.position()
    input("move to launch")
    launch = pyautogui.position()
    input("move to respawn")
    respawn = pyautogui.position()
    input("move to save and exit")
    save_and_exit = pyautogui.position()
    coords = f"{terminal.x} {terminal.y}\n{singleplayer.x} {singleplayer.y}\n{launch.x} {launch.y}\n{respawn.x} {respawn.y}\n{save_and_exit.x} {save_and_exit.y}\n{zombie_screenshot.x} {zombie_screenshot.y}\n{menu_screenshot.x} {menu_screenshot.y}\n{loading_screenshot.x} {loading_screenshot.y}\n{death_screenshot.x} {death_screenshot.y}"
    with open(f"screens/{screen_file}", "w") as f:
        f.write(str(coords))


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

if __name__ == "__main__":
    define_points()
