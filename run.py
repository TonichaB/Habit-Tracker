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

# Start Screen
print("Habit Tracker")
print("Please press enter to start...")


def login():
    # log in function will go here
    print("You have selected Log In")


def register():
    # register function will go here
    print("You have selected Register")


def startup():
    # the following code has been created with the assistance of open.ai
    # this code lets the user select login/register using arrow keys
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
                login()
            elif options[selected_option_index] == "Register":
                register()


if __name__ == "__main__":
    startup()
