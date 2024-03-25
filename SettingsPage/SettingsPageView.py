from tkinter import *


class SettingsPageView:
    def __init__(self, master, controller):
        self.controller = controller

        # Frame creation
        self.settings_page = Frame(master)
        self.settings_page.grid(row=0, column=0, sticky=NSEW)

        # Labels
        Label(self.settings_page, text="Settings", font=('Arial', 40), bg="light gray")\
            .grid(row=0, column=0, sticky=EW, padx=330, pady=30, ipadx=220, ipady=50)

        # Dark mode checkbutton
        Checkbutton(self.settings_page, text="Dark mode", font=('Arial', 20), bg="light gray", borderwidth=2,
                    relief="solid", command=lambda: controller.dark_mode())\
            .grid(row=3, column=0, pady=40)

        # Support and help button
        Button(self.settings_page, text="Support and Help", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.support_and_help())\
            .grid(row=1, column=0, sticky=W, padx=200, pady=40, ipady=5)

        # App version button
        Button(self.settings_page, text="App version", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.app_version())\
            .grid(row=1, column=0, sticky=E, padx=200, pady=40, ipady=5)

        # Credits button
        Button(self.settings_page, text="Credits", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.credits())\
            .grid(row=2, column=0, sticky=W, padx=200, pady=40, ipady=5)

        # About app button
        Button(self.settings_page, text="About app", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.about_app())\
            .grid(row=2, column=0, sticky=E, padx=200, pady=40, ipady=5)

        # Close button
        Button(self.settings_page, text="Close", font=('Arial', 15), bg="light gray", width=8,
               command=lambda: controller.back())\
            .grid(row=4, column=0, sticky=SE, padx=30, pady=10, ipady=5)

    # Destroying frame
    def destroy_setting_page_frame(self):
        self.settings_page.destroy()