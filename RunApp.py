from tkinter import Tk
from UserLoginPage.UserLoginController import UserLoginController


def main():
    root = Tk()
    root.configure(bg="light gray")
    root.geometry("1280x720")
    root.resizable(False, False)
    root.title("Budget")
    app = UserLoginController(root)
    root.mainloop()


if __name__ == '__main__':
    main()