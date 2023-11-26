import gspread
from google.oauth2.service_account import Credentials
import curses

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

# Start Screen
print("Habit Tracker")
print("Please press enter to start...")


def login(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "You have selected Log In")
    stdscr.refresh()

    username = ""
    password = ""

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == 10:  # Enter key
            break
        elif key == curses.KEY_BACKSPACE:
            username = username[:-1]
        else:
            username += chr(key)

        stdscr.addstr(1, 0, f"Please confirm your username: {username}")
        stdscr.refresh()

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == 10:  # Enter key
            break
        elif key == curses.KEY_BACKSPACE:
            password = password[:-1]
        else:
            password += chr(key)

        stdscr.addstr(1, 0, f"Please confirm your password: {password}")
        stdscr.refresh()

    username_column = credentials_worksheet.col_values(1)
    password_column = credentials_worksheet.col_values(2)

    if username in username_column:
        index = username_column.index(username)
        stored_password = password_column[index]
        if stored_password == password:
            stdscr.addstr(2, 0, "Login successful!")
            stdscr.refresh()
            stdscr.getch()
            return True
        else:
            stdscr.addstr(2, 0, "Incorrect password.")
    else:
        stdscr.addstr(2, 0, "Username not found.")

    stdscr.refresh()
    stdscr.getch()
    return False


def register(stdscr):

    stdscr.clear()
    stdscr.addstr(0, 0, "You have selected Register")
    stdscr.refresh()

    new_user = ""
    new_password = ""

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == 10:  # Enter key
            break
        elif key == curses.KEY_BACKSPACE:
            new_user = new_user[:-1]
        else:
            new_user += chr(key)

        stdscr.addstr(1, 0, f"Please choose your username: {new_user}")
        stdscr.refresh()

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == 10:  # Enter key
            break
        elif key == curses.KEY_BACKSPACE:
            new_password = new_password[:-1]
        else:
            new_password += chr(key)

        stdscr.addstr(1, 0, f"Please choose your password: {new_password}")
        stdscr.refresh()

    username_column = credentials_worksheet.col_values(1)

    if new_user in username_column:
        stdscr.addstr(2, 0, "The username already exists. Please try again.")
    else:

        # Add the new user's credentials to the next available row.
        next_row = len(username_column) + 1
        credentials_worksheet.update_cell(next_row, 1, new_user)
        credentials_worksheet.update_cell(next_row, 2, new_password)

        stdscr.addstr(2, 0, "Registration successful!")

    stdscr.refresh()
    stdscr.getch()


def startup(stdscr):
    options = ["Login", "Register"]
    selected_option_index = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "\nPlease select an option:")

        for i, option in enumerate(options):
            stdscr.addstr(
                i + 1,
                0,
                f"{'>> ' if i == selected_option_index else '   '}{option}"
            )

        key = stdscr.getch()

        if key == curses.KEY_DOWN and selected_option_index < len(options) - 1:
            selected_option_index += 1
        elif key == curses.KEY_UP and selected_option_index > 0:
            selected_option_index -= 1
        elif key == 10:  # Enter key
            if options[selected_option_index] == "Login":
                if login(stdscr):
                    # Continue with other main menu options, since
                    # the user is now logged in.
                    pass  # Replace with main menu logic
            elif options[selected_option_index] == "Register":
                register(stdscr)


if __name__ == "__main__":
    curses.wrapper(startup)
