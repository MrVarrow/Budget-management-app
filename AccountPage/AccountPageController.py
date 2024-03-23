from AccountPage.AccountPageModel import AccountPageModel
from AccountPage.AccountPageView import AccountPageView


class AccountPageController:
    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data
        self.account_page_view = AccountPageView(self.root, self)
        self.account_page_model = AccountPageModel()
