import gspread
from google.oauth2.service_account import Credentials
import questionary
import questionary as qt
from habit_operations import HabitOperations
import shutup
shutup.please()


class HabitTracker:
    def __init__(self):
        # List of APIs requiring access
        self.SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        # Constant variables
        self.CREDS = Credentials.from_service_account_file('creds.json')
        self.SCOPED_CREDS = self.CREDS.with_scopes(self.SCOPE)
        self.GSPREAD_CLIENT = gspread.authorize(self.SCOPED_CREDS)

        self.SHEET = self.GSPREAD_CLIENT.open('habit_tracker')
        self.credentials_worksheet = self.SHEET.worksheet('user_accounts')
        self.habits_worksheet = self.SHEET.worksheet('habits_list')
        self.habit_log_worksheet = self.SHEET.worksheet('habit_log')
        self.logged_in_user = ""
        self.habit_operations = HabitOperations(self)

    # defining the start up function
    def startup(self):
        print("*** WELCOME TO HABIT TRACKER ***")
        options = ["Login", "Register"]

        selected_option = (
            questionary.select("Please select an option:", choices=options)
            .ask()
        )

        if selected_option == "Login":
            self.habit_operations.login()
        elif selected_option == "Register":
            self.habit_operations.register()
