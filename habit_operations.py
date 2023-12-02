import questionary
from operation_functions import Functions


class HabitOperations:
    def __init__(self, habit_tracker, operation_functions):
        self.habit_tracker = habit_tracker
        self.operation_functions = operation_functions

    # Main Page Functions
    def main_options(self):

        print(
            f'Welcome {self.habit_tracker.logged_in_user} '
            f'to your habit tracker!'
            )

        # User Options
        choice = questionary.select(
            '''
                Use your arrow keys to navigate the list.
                To select your answer press enter.
                What would you like to do?
            ''',
            choices=[
                "Update Password",
                "Add New Habit",
                "Delete Habit",
                "Change Habit Frequency",
                "Log Today's Habits",
                "View Habits",
                "Delete Account"]
            ).ask()

        # Update Password
        if choice == "Update Password":
            while True:
                # Asks user to enter current details
                user = questionary.text("Please confirm your username:").ask()
                old_password = (
                    questionary.password(
                        "Please confirm your current password:"
                    ).ask()
                )

                username_column = (
                    self.habit_tracker.credentials_worksheet.col_values(1)
                )
                password_column = (
                    self.habit_tracker.credentials_worksheet.col_values(2)
                )

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
                        self.habit_tracker.credentials_worksheet.update_cell(
                            row_index,
                            2,
                            new_password
                        )

                        print("Password Updated!")
                        self.main_options()
                        break
                    else:
                        print("Old Password Incorrect, Try Again")
                else:
                    print("Username not found or incorrect current password.")

        # Option to add new habit repeats registration method
        elif choice == "Add New Habit":
            self.operation_functions.new_habit()

        # Option to delete a stored habit
        elif choice == "Delete Habit":
            print("Don't need to track a habit anymore?")
            print("No worries! Lets take it out of the tracker!")

            while True:
                ex_habit = questionary.text(
                    "Please confirm the habit to be removed:"
                ).ask()

                habit_options = (
                    self.habit_tracker.habits_worksheet.col_values(1)
                )

                if ex_habit in habit_options:
                    print("Habit has been confirmed.")

                    # Before deleting user is asked whether they are sure
                    answer = questionary.confirm(
                        "Are you sure? Confirm Yes/No"
                    ).ask()

                    # If user types 'Y' the habit will be removed
                    if answer:
                        print("You have selected yes")
                        habit_index = (
                            self.habit_tracker.habit_options.index(
                                ex_habit
                            ) + 1
                        )
                        self.habit_tracker.habits_worksheet.delete_rows(
                            habit_index
                        )
                        print("Habit Removed Sucessfully!")
                        self.main_options()
                        break
                    # If user types 'N' the habit is not removed
                    else:
                        print("You have selected No")

                # If the user does not enter anything, return to Main Menu
                elif not habit_options:
                    print(
                        '''A habit has not been confirmed.
                        Returning to Main Menu'''
                    )
                    self.main_options()
                    break

                # If the habit has been typed incorrectly the user is
                # notified and will be asked to enter habit details again
                elif ex_habit not in habit_options:
                    print("Sorry we can't locate this habit, please try again")
                    print("Please note habits are case sensitive!")

        # Change the frequency applied to a saved habit
        elif choice == "Change Habit Frequency":
            print("Change how often you want to complete a habit.")

        # User logs which habits have been completed for the current date
        elif choice == "Log Today's Habits":
            print("What have you achieved today?")

        # Opens further options to the user to view habits previously logged
        elif choice == "View Habits":
            print("Please select from the following options:")

        # Log out from current user and return to start page
        elif choice == "Log Out":
            print("You are now logged out!")
            self.habit_tracker.startup()

        # User can choose to delete their account
        # and any saved data under their account
        elif choice == "Delete Account":
            print("We are sorry to see you go!")

            answer = questionary.confirm(
                '''Are you sure you want to delete your account?
                Confirm Y (Yes) or N (No)'''
            ).ask()

            if answer:
                self.operation_functions.delete_account()
            else:
                print("You have confirmed no, returning to Main Menu")
