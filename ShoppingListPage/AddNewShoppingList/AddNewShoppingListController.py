from tkinter import messagebox
from ShoppingListPage.AddNewShoppingList.AddNewShoppingListModel import AddShoppingListModel
from ShoppingListPage.AddNewShoppingList.AddNewShoppingListView import AddNewShoppingListView


class ShoppingListController:
    def __init__(self, root, user_data, bg_color, items_df, state, shopping_list_name):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.shopping_list_name = shopping_list_name

        self.add_new_shopping_list_model = AddShoppingListModel()
        self.add_new_shopping_list_view = AddNewShoppingListView(self.root, self, self.bg_color, self.shopping_list_name, state)

        if items_df is None:
            self.items_df = self.add_new_shopping_list_model.create_df()
            self.add_new_shopping_list_view.create_treeview(self.items_df)
        else:
            self.items_df = items_df
            self.add_new_shopping_list_view.create_treeview(self.items_df)
            self.add_new_shopping_list_view.update_treeview(self.items_df)

    def submit_item(self):
        ...

    def edit_item(self):
        ...

    def delete_item(self):
        ...

    def clear_list(self):
        ...

    def add_shopping_list(self):
        ...

    def back_to_shopping_list_page(self):
        ...
