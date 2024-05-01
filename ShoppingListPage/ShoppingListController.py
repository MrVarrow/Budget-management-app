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

        self.shopping_list_view.shopping_lists_combobox_update(
            self.shopping_list_model.shopping_list_list_from_database(self.user_data[0]))

    def open_shopping_list(self, shopping_list_name):
        receipt_id = self.shopping_list_model.select_shopping_list(shopping_list_name)
        self.items_df = self.shopping_list_model.items_from_shopping_list(receipt_id)
        shopping_list_date = self.shopping_list_model.shopping_list_date(receipt_id)

        self.shopping_list_view.create_overview(shopping_list_name, self.items_df, shopping_list_date)
        # Overview loading here

    def delete_shopping_list(self, shopping_list_name):
        result = messagebox.askquestion(title='Warning', message="Do you want to delete selected shopping list?")
        if result == "yes":
            self.shopping_list_model.delete_shopping_list_from_database(shopping_list_name,
                                                                        self.shopping_list_model.select_shopping_list(shopping_list_name))
            self.shopping_list_view.shopping_lists_combobox_update(
                self.shopping_list_model.shopping_list_list_from_database(self.user_data[0]))
        elif result == "no":
            pass

    def edit_shopping_list(self, shopping_list_name):
        if self.shopping_list_model.check_chosen_shopping_list(shopping_list_name):
            from ShoppingListPage.AddNewShoppingList.AddNewShoppingListController import AddShoppingListController
            self.shopping_list_view.destroy_shopping_list_frame()
            AddShoppingListController(self.root, self.user_data, self.bg_color, self.items_df, state="UPDATE",
                                      shopping_list_name=shopping_list_name)
            return
        messagebox.showinfo(title="Information", message="You need to choose receipt for editing first")

    def add_new_shopping_list(self):
        self.shopping_list_view.destroy_shopping_list_frame()
        from ShoppingListPage.AddNewShoppingList.AddNewShoppingListController import AddShoppingListController
        AddShoppingListController(self.root, self.user_data, self.bg_color, self.items_df, state="ADD",
                                  shopping_list_name=None)

    def back_to_logged_usr_page(self):
        self.shopping_list_view.destroy_shopping_list_frame()
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        LoggedUserPageController(self.root, self.user_data, self.bg_color)


