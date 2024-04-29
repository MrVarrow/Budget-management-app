from tkinter import messagebox
from ShoppingListPage.ShoppingListView import ShoppingListView
from ShoppingListPage.ShoppingListModel import ShoppingListModel


class ShoppingListController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.items_df = None

        self.shopping_list_model = ShoppingListModel()
        self.shopping_list_view = ShoppingListView(self.root, self, self.bg_color)

    def open_shopping_list(self):
        ...

    def delete_shopping_list(self):
        ...

    def edit_shopping_list(self):
        ...

    def add_new_shopping_list(self):
        self.shopping_list_view.destroy_shopping_list_frame()
        from ShoppingListPage.AddNewShoppingList.AddNewShoppingListController import ShoppingListController
        ShoppingListController(self.root, self.user_data, self.bg_color, self.items_df, state="ADD", shopping_list_name=None)

    def back_to_logged_usr_page(self):
        self.shopping_list_view.destroy_shopping_list_frame()
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        LoggedUserPageController(self.root, self.user_data, self.bg_color)


