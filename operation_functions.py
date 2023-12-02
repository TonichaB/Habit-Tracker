import questionary


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
