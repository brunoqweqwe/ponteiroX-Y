import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}", end="\r")
except KeyboardInterrupt:
    print("\nPrograma encerrado.")
