from tkinter import messagebox
from ShoppingListPage.ShoppingListView import ShoppingListView
from ShoppingListPage.ShoppingListModel import ShoppingListModel
from Validations.Validations import empty_string_inside_widget, false_in_bool_list


class ShoppingListController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        # Define variables
        self.items_df = None
        self.checkbutton_list = []

        self.shopping_list_model = ShoppingListModel()
        self.shopping_list_view = ShoppingListView(self.root, self, self.bg_color)

        self.shopping_list_view.shopping_lists_combobox_update(
            self.shopping_list_model.shopping_list_list_from_database(self.user_data))

    # Open shopping list button
    def open_shopping_list(self, shopping_list_name: str):
        if empty_string_inside_widget(shopping_list_name):
            messagebox.showinfo(title="Information", message="You need to choose shopping list first.")
            return
        shopping_list_id = self.shopping_list_model.select_shopping_list(shopping_list_name)
        self.items_df = self.shopping_list_model.items_from_shopping_list(shopping_list_id)
        shopping_list_date = self.shopping_list_model.shopping_list_date(shopping_list_id)

        self.shopping_list_view.create_overview(shopping_list_name, self.items_df, shopping_list_date)

    # Delete shopping list button
    def delete_shopping_list(self, shopping_list_name: str, msg="Do you want to delete selected shopping list?"):
        if empty_string_inside_widget(shopping_list_name):
            messagebox.showinfo(title="Information", message="You need to choose shopping list first.")
            return
        result = messagebox.askquestion(title='Warning', message=msg)
        if result == "yes":
            self.shopping_list_model.delete_shopping_list_from_database(
                shopping_list_name,
                self.shopping_list_model.select_shopping_list(shopping_list_name)
            )
            self.shopping_list_view.shopping_lists_combobox_update(
                self.shopping_list_model.shopping_list_list_from_database(self.user_data[0]))
        elif result == "no":
            pass

    # Go to editing shopping list if user had chosen a list (button)
    def edit_shopping_list(self, shopping_list_name: str):
        if empty_string_inside_widget(shopping_list_name):
            messagebox.showinfo(title="Information", message="You need to choose shopping list for editing first")
            return

        from ShoppingListPage.AddNewShoppingList.AddNewShoppingListController import AddShoppingListController
        self.shopping_list_view.destroy_shopping_list_frame()
        AddShoppingListController(self.root, self.user_data, self.bg_color, self.items_df, state="UPDATE",
                                  shopping_list_name=shopping_list_name)

    # Go to add new shopping list page (button)
    def add_new_shopping_list(self):
        self.shopping_list_view.destroy_shopping_list_frame()
        from ShoppingListPage.AddNewShoppingList.AddNewShoppingListController import AddShoppingListController
        AddShoppingListController(self.root, self.user_data, self.bg_color, self.items_df, state="ADD",
                                  shopping_list_name=None)

    # Back to main page
    def back_to_logged_usr_page(self):
        self.shopping_list_view.destroy_shopping_list_frame()
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        LoggedUserPageController(self.root, self.user_data, self.bg_color)

    '''
    Overview methods
    '''

    # Check if user checked all the boxes
    def check_list(self, shopping_list_name: str):
        if false_in_bool_list(self.checkbutton_list):
            messagebox.showinfo(title="Information", message="You didn't check all of the items.")
            return
        self.delete_shopping_list(shopping_list_name, "List is complete, do you want to delete this shopping list?")

    # Tracks state of every checkbox state and update its value in list
    def check_box(self, index: int, check_vars: list):
        self.checkbutton_list = self.shopping_list_model.toggle_checkbutton(index, check_vars)
