from tkinter import Tk
from UserLoginPage.UserLoginController import UserLoginController


def main():
    # Create root
    root = Tk()
    bg_color = "#f0f0f0"
    root.geometry("1280x720")
    root.resizable(False, False)
    root.title("Budget App")
    # Launch App
    UserLoginController(root, bg_color)
    root.mainloop()


if __name__ == '__main__':
    main()
