import time
import pyautogui

def simulate_mouse_clicks():
    for _ in range(3):
        pyautogui.click(button='left')


def main():
    while True:
        simulate_mouse_clicks()
        time.sleep(10)  

if __name__ == "__main__":
    main()