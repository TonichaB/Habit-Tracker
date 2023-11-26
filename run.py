import gspread
from google.oauth2.service_account import Credentials
import keyboard

# List of API's requiring access
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Constant variables
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('habit_tracker')
credentials_worksheet = SHEET.worksheet('user_accounts')

# Start Screen
print("Habit Tracker")
print("Please press enter to start...")


def login():

    print("You have selected Log In")
    username = input("Please confirm your username: ")
    password = input("Please confirm your password: ")

    username_column = credentials_worksheet.col_values(1)
    password_column = credentials_worksheet.col_values(2)

    if username in username_column:
        index = username_column.index(username)
        stored_password = password_column[index]
        if stored_password == password:
            print("Login successful!")
            return True
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")
    return False


def register():

    print("You have selected Register")
    new_user = input("Please choose your username: ")

    username_column = credentials_worksheet.col_values(1)

    if new_user in username_column:
        print("The username already exists. Please choose a different one.")
    else:
        new_password = input("Please choose your password: ")

        # Add the new user's credentials to the next available row.
        next_row = len(username_column) + 1
        credentials_worksheet.update_cell(next_row, 1, new_user)
        credentials_worksheet.update_cell(next_row, 2, new_password)

        print("Registration successful!")


def startup():

    options = ["Login", "Register"]
    selected_option_index = 0

    while True:
        print("\nPlease select an option:")
        for i, option in enumerate(options):
            print(f"{'>> ' if i == selected_option_index else '   '}{option}")

        key = keyboard.read_event(suppress=True).name

        if key == "down" and selected_option_index < len(options) - 1:
            selected_option_index += 1
        elif key == "up" and selected_option_index > 0:
            selected_option_index -= 1
        elif key == "enter":
            if options[selected_option_index] == "Login":
                if login():
                    # Continue with other main menu options, since
                    # the user is now logged in.
                    pass  # Replace with main menu logic
            elif options[selected_option_index] == "Register":
                register()


if __name__ == "__main__":

    startup()
