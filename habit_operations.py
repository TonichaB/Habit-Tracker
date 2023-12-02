import questionary


class HabitOperations:
    def __init__(self, habit_tracker):
        self.habit_tracker = habit_tracker

    # Main Page Functions
    def main_options(self):

        print(
            f'Welcome {self.habit_tracker.logged_in_user} to your habit tracker!'
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
            self.new_habit()

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
                self.delete_account()
            else:
                print("You have confirmed no, returning to Main Menu")

    def delete_account(self):
        username_column = (
            self.habit_tracker.credentials_worksheet.col_values(1)
        )

        if self.habit_tracker.logged_in_user not in username_column:
            print(f"User {self.habit_tracker.logged_in_user} not found.")
            return

        # find the row index for the logged_in_user
        user_index = (
            username_column.index(self.habit_tracker.logged_in_user) + 1
        )

        # delte the row in the user_accounts worksheet
        self.habit_tracker.credentials_worksheet.delete_rows(user_index)

        # Delete all habits linked with the logged_in_user
        habit_options = self.habit_tracker.habits_worksheet.col_values(1)
        user_habits = [
            habit for habit in habit_options if habit.startswith(
                self.habit_tracker.logged_in_user
            )]

        for habit in user_habits:
            habit_index = habit_options.index(habit) + 1
            self.habit_tracker.habits_worksheet.delete_rows(habit_index)

        print(
            f"Account for {self.habit_tracker.logged_in_user} has been deleted."
            )
        self.habit_tracker.startup()

    def new_habit(self):
        while True:
            new_habit = questionary.text(
                '''
                    Please type in a habit to track:
                    Click Enter to submit your answer.
                    Press Enter without text to exit
                    back to the main menu!
                '''
            ).ask()

            habit_options = self.habit_tracker.habits_worksheet.col_values(1)
            habit_frequency = self.habit_tracker.habits_worksheet.col_values(2)

            if new_habit in habit_options:
                # Habit already included in the database to be tracked
                print("You are already tracking this habit!")
            elif not new_habit:
                # If the user selects enter with no text they
                # progress to the Main Menu
                print("No habit entered. Returning to Menu.")
                self.main_options()
            elif new_habit not in habit_options:

                # Add username to the habit saved
                formatted_habit = (
                    f"{self.habit_tracker.logged_in_user}_{new_habit}"
                )

                # New habit created and saved to database
                next_row = len(habit_options) + 1
                self.habit_tracker.habits_worksheet.update_cell(
                    next_row, 1, formatted_habit
                )

                frequency = questionary.select(
                    '''
                        How often would you like to track this habit?
                        Use Arrow Keys to select and Enter to submit.
                    ''',
                    choices=["Daily", "Weekly", "Monthly"]
                    ).ask()
                next_row_f = len(habit_frequency) + 1
                self.habit_tracker.habits_worksheet.update_cell(
                    next_row_f, 2, frequency
                )

                print("Habit Saved!")
