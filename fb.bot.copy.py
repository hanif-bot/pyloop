import pyautogui
import time

def main():
    while True:
        command = input("Enter a command : ily, alabiu, imissyou : ")

        if command == 'ily':
            for i in range(10):
                pyautogui.typewrite("ily")
                pyautogui.typewrite("\n")
                time.sleep(0.1)
        elif command == 'alabiu':
            for i in range(10):
                pyautogui.typewrite("alabiu")
                pyautogui.typewrite("\n")
                time.sleep(0.1)
        elif command == 'imissyou':
            for i in range(10):
                pyautogui.typewrite("imissyou")
                pyautogui.typewrite("\n")
                time.sleep(0.1)

        else:
            print("Enter Correct Command. Stupid<33")

if __name__ == "__main__":
    main()