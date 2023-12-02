import questionary
from datetime import datetime


class Functions:
    def __init__(self, habit_tracker, habit_operations):
        self.habit_tracker = habit_tracker
        self.habit_operations = habit_operations

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
            f'Account for {self.habit_tracker.logged_in_user} '
            f'has been deleted.'
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
                self.habit_operations.main_options()
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

    def delete_habit(self):
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
                    self.habit_operations.main_options()
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
                self.habit_operations.main_options()
                break

            # If the habit has been typed incorrectly the user is
            # notified and will be asked to enter habit details again
            elif ex_habit not in habit_options:
                print("Sorry we can't locate this habit, please try again")
                print("Please note habits are case sensitive!")

    def update_password(self):
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
                    self.habit_operations.main_options()
                    break
                else:
                    print("Old Password Incorrect, Try Again")
            else:
                print("Username not found or incorrect current password.")

    def update_frequency(self):
        print("Change how often you want to complete a habit.")
        # Display the list of saved habits
        habit_options = self.habit_tracker.habits_worksheet.col_values(1)
        user_habits = [
            habit for habit in habit_options if habit.startswith(
                self.habit_tracker.logged_in_user
            )
        ]

        if not user_habits:
            print("You have not saved any habits yet!")
            return

        # Allow user to select a habit
        else:
            habit_to_change = questionary.select(
                "Please choose a habit to change the frequency:",
                choices=user_habits).ask()

            # Find the index of habit within the list
            habit_index = user_habits.index(habit_to_change)

            # User chooses a new frequency
            new_frequency = questionary.select(
                "Choose a new frequency:",
                choices=["Daily", "Weekly", "Monthly"]
            ).ask()

            print(
                f'''You have selected to change:
                {habit_to_change} to {new_frequency}'''
            )
            answer = questionary.confirm("Is this correct?").ask()

            if answer:
                # Update habit frequency in spreadsheet
                self.habit_tracker.habits_worksheet.update_cell(
                    habit_index + 1, 2, new_frequency
                )
                print(f"{habit_to_change} has been updated to {new_frequency}")
            else:
                print("Habit frequency has not been updated")

    def log_habits(self):
        print("What have you achieved today?")
        # Display saved habits
        habit_options = self.habit_tracker.habits_worksheet.col_values(1)
        user_habits = [
            habit for habit in habit_options if habit.startswith(
                self.habit_tracker.logged_in_user
            )
        ]

        if not user_habits:
            print("You have no habits to log for today!")
            return
        else:
            # User can select habits completed
            habits_completed = questionary.checkbox(
                "Select the habits you have completed today:",
                choices=user_habits
            ).ask()

            # Get the current date
            current_date = datetime.now().strftime("%Y-%m-%d")

            # Update the spreadsheet with logged habits
            for habit in habits_completed:
                habit_index = habit_options.index(habit)
                self.habit_tracker.habits_worksheet.update_cell(
                    habit_index + 1, 3, current_date
                )
                print("Habits logged succesfully for today!")

    def view_habits(self):
        print("Please select from the following options:")
