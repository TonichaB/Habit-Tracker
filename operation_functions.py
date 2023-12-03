import questionary
from datetime import datetime, timedelta
import bcrypt


class Functions:
    def __init__(self, habit_operations, habit_tracker):
        self.habit_operations = habit_operations
        self.habit_tracker = habit_tracker

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

            habit_name = f"{self.habit_tracker.logged_in_user}_{ex_habit}"
            if habit_name in habit_options:
                print("Habit has been confirmed.")

                # Before deleting user is asked whether they are sure
                answer = questionary.confirm(
                    "Are you sure? Confirm Yes/No"
                ).ask()

                # If user types 'Y' the habit will be removed
                if answer:
                    print("You have selected yes")
                    habit_index = (
                        habit_options.index(
                            habit_name
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
            elif habit_name not in habit_options:
                print("Sorry we can't locate this habit, please try again")
                print("Please note habits are case sensitive!")

    def update_password(self):
        while True:
            # Asks user to enter current details
            user = self.habit_tracker.logged_in_user
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
            if user in username_column:
                index = username_column.index(user)
                stored_password_hash = password_column[index]

                if bcrypt.checkpw(
                    old_password.encode('utf-8'),
                    stored_password_hash.encode('utf-8')
                ):
                    print("Old Password Confirmed.")
                    new_password = (
                        questionary.password(
                            "Please choose your new password:"
                        ).ask()
                    )

                    # Use bcrypt to hash the new password
                    new_password_hash = bcrypt.hashpw(
                        new_password.encode('utf-8'),
                        bcrypt.gensalt()
                    )

                    # Update the password in the existing row
                    row_index = index + 1
                    self.habit_tracker.credentials_worksheet.update_cell(
                        row_index,
                        2,
                        new_password_hash.decode('utf-8')
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
            habit.split('_', 1)[1]
            for habit in habit_options
            if habit.startswith(
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
            habit_index = habit_options.index(
                f"{self.habit_tracker.logged_in_user}_{habit_to_change}"
            )

            # Extract the habit name without username prefix
            habit_name = habit_to_change

            # User chooses a new frequency
            new_frequency = questionary.select(
                "Choose a new frequency:",
                choices=["Daily", "Weekly", "Monthly"]
            ).ask()

            print(
                f'''You have selected to change:
                {habit_name} to {new_frequency}'''
            )
            answer = questionary.confirm("Is this correct?").ask()

            if answer:
                # Update habit frequency in spreadsheet
                self.habit_tracker.habits_worksheet.update_cell(
                    habit_index + 1, 2, new_frequency
                )
                print(f"{habit_name} has been updated to {new_frequency}")

            else:
                print("Habit frequency has not been updated")
            self.habit_operations.main_options()

    def log_habits(self):
        print("What have you achieved today?")
        # Display saved habits
        habit_options = self.habit_tracker.habits_worksheet.col_values(1)
        user_habits = [
            habit.split('_', 1)[1]
            for habit in habit_options
            if habit.startswith(
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

            # Update the log worksheet with new entries
            log_worksheet = self.habit_tracker.SHEET.worksheet('habit_log')

            # Update the spreadsheet with logged habits
            for habit in habits_completed:
                # This will extract habit name without username present
                log_worksheet.append_row([
                    self.habit_tracker.logged_in_user,
                    habit,
                    current_date
                ])
                print(f"{habits_completed} logged succesfully for today!")
                self.habit_operations.main_options()

    def view_habits(self):
        view_options = questionary.select(
            "Please select from the following options:",
            choices=[
                "View Today's Habits",
                "View Habits for a Selected Period",
                "Return to Main Menu"]
        ).ask()

        if view_options == "View Today's Habits":
            self.view_current_date_habits()
        elif view_options == "View Habits for a Selected Period":
            self.view_habits_in_period()
        elif view_options == "Return to Main Menu":
            self.habit_operations.main_options()

    def view_current_date_habits(self):
        # Get the current date
        current_date = datetime.now().strftime('%Y-%m-%d')

        # Get the username to filter saved habits
        username = self.habit_tracker.logged_in_user

        # Get the log worksheet
        log_worksheet = self.habit_tracker.SHEET.worksheet('habit_log')

        # Get the entries for the current user and current date
        all_entries = log_worksheet.get_all_values()

        # FIlter the entries based on user and date
        filtered_entries = [
            entry for entry in all_entries
            if len(entry) >= 3 and
            entry[0] == username and
            entry[2] == current_date
        ]

        if filtered_entries:
            print(
                "Habits logged for the current date ({}):".format(current_date)
            )
            for entry in filtered_entries:
                print(f"Habit: {entry[1]}")
        else:
            print("No habits have been logged for the current date.")
        self.habit_operations.main_options()

    def view_habits_in_period(self):
        # Initialise start and end date variables
        start_date = None
        end_date = None

        while True:
            # Get the start and end date from the user
            start_date_str = questionary.text(
                "Plese enter a start date (YYYY-MM-DD)"
            ).ask()
            end_date_str = questionary.text(
                "Please enter an end date (YYYY-MM-DD"
            ).ask()

            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        # Get the username to filter the habits
        username = self.habit_tracker.logged_in_user

        # Get the log worksheet
        log_worksheet = self.habit_tracker.SHEET.worksheet('habit_log')

        # Get the user entries within the specified date range
        date_filter = (
            f'{start_date.strftime("%Y-%m-%d")}:'
            f'{end_date.strftime("%Y-%m-%d")}'
        )
        user_entries = log_worksheet.get_all_values()

        # Filter entries for user and date range
        filtered_entries = [
            entry for entry in user_entries
            if entry[0] == username and date_filter.startswith(entry[2])
        ]

        # Display the filtered entries
        if filtered_entries:
            print(
                "Habits logged between {} and {}:".format(
                    start_date_str, end_date_str)
            )
            for entry in filtered_entries:
                print(f"Date: {entry[2]}, Habit: {entry[1]}")
        else:
            print("There are no habits logged within this time period.")
        self.habit_operations.main_options()
