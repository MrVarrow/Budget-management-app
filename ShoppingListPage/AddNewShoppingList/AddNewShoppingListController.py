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

    def submit_item(self, item_name, item_quantity):
        if not self.add_new_shopping_list_model.check_product_name(item_name):
            messagebox.showinfo("Information", "Entered product name contains not allowed characters")
            return
        if not self.add_new_shopping_list_model.check_product_quantity(item_quantity):
            messagebox.showinfo("Information", "Entered product quantity is incorrect or contains not allowed "
                                               "characters please follow format: xx or xx.xxx")
            return
        self.items_df = self.add_new_shopping_list_model.add_items_to_df(item_name, item_quantity, self.items_df)
        self.add_new_shopping_list_view.delete_items_in_treeview()
        self.add_new_shopping_list_view.update_treeview(self.items_df)

    def edit_element(self, item_value):
        self.add_new_shopping_list_view.edit_element_window(item_value[0], item_value[1])

    def delete_item(self, item_name):
        try:
            result = messagebox.askquestion("Warning", "Do you want to delete selected item from your shopping list?")
            if result == "yes":
                self.items_df = self.add_new_shopping_list_model.delete_from_df(item_name, self.items_df)
                self.add_new_shopping_list_view.delete_items_in_treeview()
                self.add_new_shopping_list_view.update_treeview(self.items_df)
        except IndexError:
            messagebox.showinfo("Information", "Please select item to delete first, by clicking on it.")

    def clear_shopping_list(self):
        result = messagebox.askquestion("Warning", "Do you want to clear shopping list, "
                                                   "your progress with adding shopping list will be lost")
        if result == "yes":
            self.items_df = self.add_new_shopping_list_model.create_df()
            self.add_new_shopping_list_view.clear_treeview()

    def add_shopping_list(self, shopping_list_name):
        print(shopping_list_name)
        if not self.add_new_shopping_list_model.check_receipt_name(shopping_list_name):
            messagebox.showinfo("Information", "Entered shopping list name contains not allowed characters")
            return
        self.add_new_shopping_list_model.add_shopping_list_to_database(
            self.user_data, shopping_list_name,
            self.add_new_shopping_list_model.lenght_of_shopping_list(self.items_df),
            self.add_new_shopping_list_model.get_creation_time()
        )
        shopping_list_id = self.add_new_shopping_list_model.get_shopping_list_id(shopping_list_name)
        self.add_new_shopping_list_model.add_items_to_database(
            shopping_list_id,
            self.user_data,
            self.items_df,
        )
        self.add_new_shopping_list_view.reset_receipt()
        self.items_df = self.add_new_shopping_list_model.create_df()
        messagebox.showinfo("Information", "Shopping list has been added successfully!")

    def update_shopping_list(self):
        shopping_list_id = self.add_new_shopping_list_model.get_shopping_list_id(self.shopping_list_name)
        self.add_new_shopping_list_model.delete_items_from_database(shopping_list_id)
        self.add_new_shopping_list_model.add_items_to_database(
            shopping_list_id,
            self.user_data,
            self.items_df,
        )
        self.add_new_shopping_list_model.update_item_count(
            self.add_new_shopping_list_model.lenght_of_shopping_list(self.items_df),
            shopping_list_id
        )
        self.back_to_shopping_list_page()
        messagebox.showinfo("Information", "Shopping list has been updated successfully!")

    def back_to_shopping_list_page(self):
        from ShoppingListPage.ShoppingListController import ShoppingListController
        ShoppingListController(self.root, self.user_data, self.bg_color)

    '''
    EDIT ELEMENTS WINDOW METHODS
    '''

    def apply_edit(self, old_name, new_name, new_quantity):
        try:
            self.items_df = self.add_new_shopping_list_model.edit_element_in_df(self.items_df, old_name, new_name,
                                                                                float(new_quantity))
            self.add_new_shopping_list_view.edit_element_widnow_destroy()
            messagebox.showinfo("Information", "Shopping list element has been updated successfully!")
            self.add_new_shopping_list_view.clear_treeview()
            self.add_new_shopping_list_view.update_treeview(self.items_df)
        except IndexError:
            messagebox.showinfo("Information", "Please select item to edit it first, by clicking on it.")

    def discard_edit(self):
        self.add_new_shopping_list_view.edit_element_widnow_destroy()
