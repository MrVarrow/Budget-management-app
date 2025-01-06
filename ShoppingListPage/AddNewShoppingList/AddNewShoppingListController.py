from tkinter import messagebox
from ShoppingListPage.AddNewShoppingList.AddNewShoppingListModel import AddShoppingListModel
from ShoppingListPage.AddNewShoppingList.AddNewShoppingListView import AddNewShoppingListView
from Validations.Validations import digits_in_string, special_character_in_string, valid_quantity_string,\
    two_strings_are_the_same, tuple_is_empty


# Used for add new shopping list and update shopping list based on given state
class AddShoppingListController:
    def __init__(self, root, user_data, bg_color, items_df, state, shopping_list_name):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.shopping_list_name = shopping_list_name

        self.add_new_shopping_list_model = AddShoppingListModel()
        self.add_new_shopping_list_view = AddNewShoppingListView(self.root, self, self.bg_color,
                                                                 self.shopping_list_name, state)

        # If creating new list create new dataframe to create treeview, if updating use given dataframe in argument
        if items_df is None:
            self.items_df = self.add_new_shopping_list_model.create_df()
            self.add_new_shopping_list_view.create_treeview(self.items_df)
        else:
            self.items_df = items_df
            self.add_new_shopping_list_view.create_treeview(self.items_df)
            self.add_new_shopping_list_view.update_treeview(self.items_df)

    # Adds item to items_df and updates a treeview
    def submit_item(self, item_name: str, item_quantity: str):
        if special_character_in_string(item_name) or digits_in_string(item_name):
            messagebox.showinfo("Information", "Entered product name contains not allowed characters")
            return
        if not valid_quantity_string(item_quantity):
            messagebox.showinfo("Information", "Entered product quantity is incorrect or contains not allowed "
                                               "characters please follow format: xx or xx.xxx")
            return
        for name in self.add_new_shopping_list_model.get_names_from_items_df(self.items_df):
            if two_strings_are_the_same(name, item_name):
                messagebox.showinfo("Information", "This item already exits in your shopping list.")
                return

        self.items_df = self.add_new_shopping_list_model.add_items_to_df(item_name, item_quantity, self.items_df)
        self.add_new_shopping_list_view.delete_items_in_treeview()
        self.add_new_shopping_list_view.update_treeview(self.items_df)

    # Opens edit_element_window
    def edit_element(self, table):
        if tuple_is_empty(table.selection()):
            messagebox.showinfo("Information", "Select item first")
            return
        item_value = table.item(table.selection()[0], 'values')

        self.add_new_shopping_list_view.edit_element_window(item_value[0], item_value[1])

    # Delete selected item from items_df and updates treeview
    def delete_item(self, table):
        result = messagebox.askquestion("Warning", "Do you want to delete selected item from your shopping list?")
        if result == "yes":
            if tuple_is_empty(table.selection()):
                messagebox.showinfo("Information", "Select item first")
                return
            item_value = table.item(table.selection()[0], 'values')
            self.items_df = self.add_new_shopping_list_model.delete_from_df(item_value[0], self.items_df)

            self.add_new_shopping_list_view.delete_items_in_treeview()
            self.add_new_shopping_list_view.update_treeview(self.items_df)

    # Clear items_df and treeview
    def clear_shopping_list(self):
        result = messagebox.askquestion("Warning", "Do you want to clear shopping list, "
                                                   "your progress with adding shopping list will be lost")
        if result == "yes":
            self.items_df = self.add_new_shopping_list_model.create_df()
            self.add_new_shopping_list_view.clear_treeview()

    # Adds shopping list to database, clear items_df and all view to default
    def add_shopping_list(self, shopping_list_name: str):
        if special_character_in_string(shopping_list_name):
            messagebox.showinfo("Information", "Entered shopping list name contains not allowed characters")
            return
        self.add_new_shopping_list_model.add_shopping_list_to_database(
            self.user_data, shopping_list_name,
            self.add_new_shopping_list_model.length_of_dataframe(self.items_df),
            self.add_new_shopping_list_model.get_creation_time()
        )
        shopping_list_id = self.add_new_shopping_list_model.get_shopping_list_id(shopping_list_name)
        self.add_new_shopping_list_model.add_items_to_database(
            shopping_list_id,
            self.user_data,
            self.items_df,
        )
        self.add_new_shopping_list_view.reset_shopping_list()
        self.items_df = self.add_new_shopping_list_model.create_df()
        messagebox.showinfo("Information", "Shopping list has been added successfully!")

    # Updates shopping list in database and closing Add New Shopping List Page
    def update_shopping_list(self):
        shopping_list_id = self.add_new_shopping_list_model.get_shopping_list_id(self.shopping_list_name)
        self.add_new_shopping_list_model.delete_items_from_database(shopping_list_id)
        self.add_new_shopping_list_model.add_items_to_database(
            shopping_list_id,
            self.user_data,
            self.items_df,
        )
        self.add_new_shopping_list_model.update_item_count(
            self.add_new_shopping_list_model.length_of_dataframe(self.items_df),
            shopping_list_id
        )
        self.back_to_shopping_list_page()
        messagebox.showinfo("Information", "Shopping list has been updated successfully!")

    # Goes back to Shopping list page
    def back_to_shopping_list_page(self):
        from ShoppingListPage.ShoppingListController import ShoppingListController
        ShoppingListController(self.root, self.user_data, self.bg_color)

    '''
    EDIT ELEMENTS WINDOW METHODS
    '''

    # Edits an element in dataframe and also in treeview
    def apply_edit(self, old_name: str, new_name: str, new_quantity: str):
        try:
            self.items_df = self.add_new_shopping_list_model.edit_element_in_df(self.items_df, old_name, new_name,
                                                                                float(new_quantity))
            self.add_new_shopping_list_view.edit_element_window_destroy()
            messagebox.showinfo("Information", "Shopping list element has been updated successfully!")
            self.add_new_shopping_list_view.clear_treeview()
            self.add_new_shopping_list_view.update_treeview(self.items_df)
        except IndexError:
            messagebox.showinfo("Information", "Please select item to edit it first, by clicking on it.")

    # Close the edit element window
    def discard_edit(self):
        self.add_new_shopping_list_view.edit_element_window_destroy()
