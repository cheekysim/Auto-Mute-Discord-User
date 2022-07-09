import mouse
import keyboard
import time

mouse1x, mouse1y, mouse2x, mouse2y= 0, 0, 0, 0

def main():
    print("Setup: ")
    print("WARNING:\nDiscord has to stay open,\nideally on a second monitor due to how this works,\nif discord moves and the program clicks the wrong thing,\nI take no responsibility for anything that happens.")
    input("Press any key to start: ")
    print("Step 1, Hover your mouse over someones user.")
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    mouse1x, mouse1y = mouse.get_position()
    print("Step 2, Right click and hover over server mute.")
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    mouse2x, mouse2y = mouse.get_position()
    print("Setup Done!")
    print("Press control m to mute.\nPress control n to stop.")
    while True:
        if keyboard.is_pressed('control+m'):
            mouse.move(mouse1x, mouse1y, absolute=True, duration=0)
            mouse.click('right')
            mouse.move(mouse2x, mouse2y, absolute=True, duration=0)
            time.sleep(1/10)
            mouse.click('left')
        elif keyboard.is_pressed('control+n'):
            break

if __name__ == "__main__":
    main()