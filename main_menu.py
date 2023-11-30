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
        prefix='''
            Use your arrow keys to navigate the list.
            To select your answer press enter.
        ''',
        choices=[
            "Update Password",
            "Add New Habit",
            "Delete Habit",
            "Update Habit Frequency",
            "Update Today's Habits",
            "View Habits",
            "Delete Account"]
        ).ask()

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
        while True:
            new_habit = questionary.text(
                "Please type in a habit to track:",
                prefix='''
                Click Enter to submit your answer.
                Press Enter without text to exit
                back to the main menu!
                '''
            ).ask()

            habit_options = habits_worksheet.col_values(1)
            habit_frequency = habits_worksheet.col_values(2)

            if new_habit in habit_options:
                # Habit already included in the database to be tracked
                print("You are already tracking this habit!")
            elif not new_habit:
                # If the user selects enter with no text they
                # progress to the Main Menu
                print("No habit entered. Returning to Menu.")
                main_options()
            elif new_habit not in habit_options:
                # New habit created and saved to database
                next_row = len(habit_options) + 1
                habits_worksheet.update_cell(next_row, 1, new_habit)

                frequency = questionary.select(
                    "How often would you like to track this habit?",
                    prefix="Use Arrow Keys to select and Enter to submit.",
                    choices=["Daily", "Weekly", "Monthly"]
                    ).ask()
                next_row_f = len(habit_frequency) + 1
                habits_worksheet.update_cell(next_row_f, 2, frequency)

                print("Habit Saved!")

    # Option to delete a stored habit
    elif choice == "Delete Habit":
        print("Don't need to track a habit anymore?")
        print("No worries! Lets take it out of the tracker!")

        while True:
            ex_habit = questionary.text(
                "Please confirm the habit to be removed:"
            ).ask()

            habit_options = habits_worksheet.col_values(1)

            if ex_habit in habit_options:
                print("Habit has been confirmed.")

                # Before deleting user is asked whether they are sure
                answer = questionary.confirm(
                    "Are you sure? Confirm Yes/No"
                ).ask()

                # If user types 'Y' the habit will be removed
                if answer:
                    print("You have selected yes")
                    habit_index = habit_options.index(ex_habit) + 1
                    habits_worksheet.delete_rows(habit_index)
                    print("Habit Removed Sucessfully!")
                    main_options()
                    break
                # If user types 'N' the habit is not removed
                else:
                    print("You have selected No")

            # If the user does not enter anything, return to Main Menu
            elif not habit_options:
                print(
                    "A habit has not been confirmed, returning to Main Menu"
                )
                main_options()
                break

            # If the habit has been typed incorrectly the user is
            # notified and will be asked to enter habit details again
            elif ex_habit not in habit_options:
                print("Sorry we can't locate this habit, please try again")
                print("Please note habits are case sensitive!")
