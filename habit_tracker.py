
import gspread
from google.oauth2.service_account import Credentials
import questionary
import questionary as qt
from habit_operations import HabitOperations
import bcrypt


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
        self.logged_in_user = ""
        self.habit_operations = None

    # defining the log in function
    def login(self):
        print("You have selected Log In")

        while True:
            username = questionary.text("Please confirm your username:").ask()
            password = questionary.password(
                "Please confirm your password:"
            ).ask()

            username_column = self.credentials_worksheet.col_values(1)
            password_column = self.credentials_worksheet.col_values(2)

            # Check username & password against database
            if username in username_column:
                index = username_column.index(username)
                stored_password_hash = password_column[index]
                # Use bcrypt to verify the password
                if (bcrypt.checkpw(
                        password.encode('utf-8'),
                        stored_password_hash.encode('utf-8'))):
                    print("Login successful!")

                    # Proceed to Main Menu
                    self.habit_operations.main_options()
                    break
                else:
                    print("Incorrect password.")
            else:
                print("Username not found.")

        return False

    # defining the register function
    def register(self):

        print("You have selected Register")

        while True:
            # User creates a new username
            new_user = questionary.text("Please choose your username:").ask()

            username_column = self.credentials_worksheet.col_values(1)

            if new_user in username_column:
                # If the username exists the user will need
                # to try again
                print("The username already exists. Please try again.")
            else:
                # If the username is new, the User can then add a password
                new_password = (
                    questionary.password("Please choose your password:")
                    .ask()
                )

                # Use bcrypt to hash the password
                hashed_password = bcrypt.hashpw(
                    new_password.encode('utf-8'),
                    bcrypt.gensalt()
                )

                # Add the new user's credentials to the next available row.
                next_row = len(username_column) + 1
                self.credentials_worksheet.update_cell(next_row, 1, new_user)
                self.credentials_worksheet.update_cell(
                    next_row, 2, hashed_password.decode('utf-8')
                )

                self.logged_in_user = new_user

                print("Registration successful!")
                # Once the credentials are confirmed the User
                # can start to build their habits
                self.habit_operations.operation_functions.new_habit()
                break

    # defining the start up function
    def startup(self):
        print("*** WELCOME TO HABIT TRACKER ***")
        options = ["Login", "Register"]

        selected_option = (
            questionary.select("Please select an option:", choices=options)
            .ask()
        )

        if selected_option == "Login":
            if self.login():
                self.habit_operations.main_options()
        elif selected_option == "Register":
            self.register()
