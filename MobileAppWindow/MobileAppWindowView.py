from tkinter import *


class MobileAppWindowView:
    def __init__(self, master, controller, bg_color):
        self.bg_color = bg_color
        # Loading icons and scaling them
        copy_icon = PhotoImage(file="Icons/copy.png")
        copy_icon = copy_icon.subsample(20, 20)
        email_icon = PhotoImage(file="Icons/email.png")
        email_icon = email_icon.subsample(20, 20)

        # Create TopLevel window
        mobile_app_root = Toplevel(master, bg=bg_color)
        mobile_app_root.geometry("400x200")
        mobile_app_root.title("Download our mobile app")
        mobile_app_root.resizable(False, False)

        # Labels
        Label(mobile_app_root, text="There is a link to our mobile app:", font=('Arial', 15), bg=self.bg_color) \
            .grid(row=0, column=0, pady=10)

        app_link = Label(mobile_app_root, text="Link", font=('Arial', 15), bg=self.bg_color)
        app_link.grid(row=1, column=0)
        Label(mobile_app_root, text="To download you have to click this link on your mobile device,\n"
                                         "so type it in google\n"
                                         "or copy and sent it to yourself then use on phone", borderwidth=2,
              relief="solid", bg=self.bg_color) \
            .grid(row=2, column=0, pady=10, padx=30)

        # Copy button
        copy_icon_widget = Button(mobile_app_root, image=copy_icon, bg="light gray",
                                  command=lambda: controller.copy_link(app_link.cget("text")))
        copy_icon_widget.image = copy_icon
        copy_icon_widget.grid(row=1, column=0, sticky=NE, padx=60)

        # Send email button
        send_mail_icon_widget = Button(mobile_app_root, image=email_icon, bg="light gray",
                                       command=lambda: controller.send_email_with_link(app_link.cget("text")))
        send_mail_icon_widget.image = email_icon
        send_mail_icon_widget.grid(row=1, column=0, sticky=NE, padx=10)

        # Close button
        Button(mobile_app_root, text="Close", font=('Arial', 15), command=mobile_app_root.destroy,
               bg="light gray") \
            .grid(row=3, column=0)

        # Focus on TopLevel window
        mobile_app_root.grab_set()
