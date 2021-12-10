import pyautogui
import pathlib

classification = input("Classification: ")

pyautogui.hotkey("alt", "tab")
pyautogui.moveTo(100, 100, 1)
img = pyautogui.screenshot()
img = img.crop(
    (
        (pyautogui.size()[0] // 2) - (554 // 2),
        (pyautogui.size()[1] // 2) - (732 // 2),
        (pyautogui.size()[0] // 2) + (554 // 2),
        (pyautogui.size()[1] // 2) + (732 // 2),
    )
)

if classification == "blocked":
    numbers = list(
        map(
            lambda fpath: int(fpath.parts[-1].split(".")[0][1:]),
            pathlib.Path("data/blocked").glob("*.JPG"),
        )
    )
    numbers.sort()
    img.save(f"data/blocked/B{numbers[-1] + 1}.JPG")
elif classification == "clear":
    numbers = list(
        map(
            lambda fpath: int(fpath.parts[-1].split(".")[0][1:]),
            pathlib.Path("data/clear").glob("*.JPG"),
        )
    )
    numbers.sort()
    img.save(f"data/clear/C{numbers[-1] + 1}.JPG")
elif classification == "partial":
    numbers = list(
        map(
            lambda fpath: int(fpath.parts[-1].split(".")[0][1:]),
            pathlib.Path("data/partial").glob("*.JPG"),
        )
    )
    numbers.sort()
    img.save(f"data/partial/P{numbers[-1] + 1}.JPG")
else:
    print("Invalid classification")
    exit(1)

pyautogui.hotkey("alt", "tab")
