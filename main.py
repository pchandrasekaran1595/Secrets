import os
import sys
import string
import keyboard
from random import choices


def main():
    args = "--build"
    build = False

    if args in sys.argv: build = True

    if build:
        os.system("pyinstaller main.py --onefile --clean --log-level DEBUG --name secrets --console")
    else:
        print("SECRET : {}".format("".join(choices(string.ascii_letters + string.digits + ".", k=64))))

        while True:
            if keyboard.is_pressed("q"):
                break

if __name__ == "__main__":
    sys.exit(main() or 0)