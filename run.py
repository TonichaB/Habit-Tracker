import gspread
from google.oauth2.service_account import Credentials
import questionary

# List of APIs requiring access
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


def login():
    print("You have selected Log In")

    while True:
        username = questionary.text("Please confirm your username:").ask()
        password = questionary.password("Please confirm your password:").ask()

        username_column = credentials_worksheet.col_values(1)
        password_column = credentials_worksheet.col_values(2)

        if username in username_column:
            index = username_column.index(username)
            stored_password = password_column[index]
            if stored_password == password:
                print("Login successful!")
                break
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")

    return False


def register():
    print("You have selected Register")

    while True:
        new_user = questionary.text("Please choose your username:").ask()

        username_column = credentials_worksheet.col_values(1)

        if new_user in username_column:
            print("The username already exists. Please try again.")
        else:
            new_password = (
                questionary.password("Please choose your password:")
                .ask()
            )

            # Add the new user's credentials to the next available row.
            next_row = len(username_column) + 1
            credentials_worksheet.update_cell(next_row, 1, new_user)
            credentials_worksheet.update_cell(next_row, 2, new_password)

            print("Registration successful!")
            break


def startup():
    print("Habit Tracker")
    options = ["Login", "Register"]

    selected_option = (
        questionary.select("Please select an option:", choices=options)
        .ask()
    )

    if selected_option == "Login":
        if login():
            # Continue with other main menu options, since
            # the user is now logged in.
            pass  # Replace with main menu logic
    elif selected_option == "Register":
        register()


if __name__ == "__main__":
    startup()
