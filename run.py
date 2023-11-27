import gspread
from google.oauth2.service_account import Credentials
import questionary
import questionary as qt

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
habits_worksheet = SHEET.worksheet('habits_list')


# Main Page Functions
def main_options():
    print("Welcome {username} to your habit tracker!")

    # User Options
    choice = qt.select(
        "What would you like to do?",
        choices=[
            "Update Password",
            "Add New Habit",
            "Delete Habit",
            "Update Habit Frequency",
            "Update Today's Habits",
            "Showlast weeks overview",
            "Show 1 weekoverview from set date",
            "Delete Account"
        ]).ask()

    # Update Password
    if choice == "Update Password":
        while True:
            # Asks user to enter current details
            user = questionary.text("Please confirm your username:").ask()
            old_password = (
                questionary.password("Please confirm your current password:")
                .ask()
            )

            username_column = credentials_worksheet.col_values(1)
            password_column = credentials_worksheet.col_values(2)

            # If details are correct, proceed to allow password change
            if user in username_column and old_password in password_column:
                index = username_column.index(user)
                stored_password = password_column[index]

                if stored_password == old_password:
                    print("Old Password Confirmed.")
                    new_password = (
                        questionary.password(
                            "Please choose your new password:"
                        ).ask()
                    )

                    # Update the password in the existing row
                    row_index = index + 1
                    credentials_worksheet.update_cell(
                        row_index,
                        2,
                        new_password
                    )

                    print("Password Updated!")
                    main_options()
                    break
                else:
                    print("Old Password Incorrect, Try Again")
            else:
                print("Username not found or incorrect current password.")

    # Option to add new habit repeats registration method
    elif choice == "Add New Habit":
        new_habits(user)

    # Option to delete a stored habit
    elif choice == "Delete Habit":
        print("Don't need to track a habit anymore?")
        print("No worries! Lets take it out of the tracker!")

        while True:
            ex_habit = questionary.text(
                "Please confirm the habit to be removed:"
            )

            habit_options = habits_worksheet.col_values(1)

            if ex_habit in habit_options:
                print("Habit has been confirmed.")

                answer = questionary.confirm(
                    "Are you sure? Confirm Yes/No"
                ).ask()

                if answer:
                    print("You have selected yes")
                    habit_index = habit_options.index(ex_habit) + 1
                    habits_worksheet.delete_row(habit_index)
                    print("Habit Removed Sucessfully!")
                    break
                else:
                    print("You have selected No")

            elif not habit_options:
                print(
                    "A habit has not been confirmed, returning to Main Menu"
                )
                main_options()
                break
            elif ex_habit not in habit_options:
                print("Sorry we can't locate this habit, please try again")
                print("Please note habits are case sensitive!")


# defining the log in function
def login():
    print("You have selected Log In")

    while True:
        username = questionary.text("Please confirm your username:").ask()
        password = questionary.password("Please confirm your password:").ask()

        username_column = credentials_worksheet.col_values(1)
        password_column = credentials_worksheet.col_values(2)

        # Check username & password against database
        if username in username_column:
            index = username_column.index(username)
            stored_password = password_column[index]
            if stored_password == password:
                print("Login successful!")
                # Proceed to Main Menu
                main_options()
                break
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")

    return False


# defining function to create user habits
def new_habits(username):
    print("Welcome, {username}! Let's set up your habits!")

    while True:
        # User enters a new habit to be tracked
        new_habit = questionary.text("Please type in a habit to track:").ask()

        habit_options = habits_worksheet.col_values(1)
        habit_frequency = habits_worksheet.col_values(2)

        if new_habit in habit_options:
            # Habit already included in the database to be tracked
            print("You are already tracking this habit!")
        elif not new_habit:
            # If the user selects enter with no text they
            # progress to the Main Menu
            print("No habit entered. Skipping Habit Setup.")
            main_options()
            break
        elif new_habit not in habit_options:
            # New habit created and saved to database
            next_row = len(habit_options) + 1
            habits_worksheet.update_cell(next_row, 1, new_habit)

            frequency = questionary.select(
                "How often would you like to track this habit?",
                choices=["Daily", "Weekly", "Monthly"]).ask()
            next_row_f = len(habit_frequency) + 1
            habits_worksheet.update_cell(next_row_f, 2, frequency)

            print("Habit Saved!")


# defining the register function
def register():
    print("You have selected Register")

    while True:
        # User creates a new username
        new_user = questionary.text("Please choose your username:").ask()

        username_column = credentials_worksheet.col_values(1)

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

            # Add the new user's credentials to the next available row.
            next_row = len(username_column) + 1
            credentials_worksheet.update_cell(next_row, 1, new_user)
            credentials_worksheet.update_cell(next_row, 2, new_password)

            print("Registration successful!")
            # Once the credentials are confirmed the User
            # can start to build their habits
            new_habits(new_user)
            break


# defining the start up function
def startup():
    print("*** WELCOME TO HABIT TRACKER ***")
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
