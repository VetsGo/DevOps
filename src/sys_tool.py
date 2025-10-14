import sys

def main():
    if '--help' in sys.argv:
        print("При використанні інструменту python src/sys_tool.py")
        print("Друкує 'командна строка' лише при запуску напряму.")
        return

    print("командна строка")

if __name__ == "__main__":
    main()