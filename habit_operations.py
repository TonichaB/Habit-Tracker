import questionary
from operation_functions import Functions


class HabitOperations:
    def __init__(self, habit_tracker):
        self.habit_tracker = habit_tracker
        self.operation_functions = Functions(self, habit_tracker)

    def set_functions(self, operation_functions):
        self.operation_functions = operation_functions

    # Main Page Functions
    def main_options(self):
        from habit_tracker import HabitTracker
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

        # Update password option
        if choice == "Update Password":
            self.operation_functions.update_password()

        # Option to add new habit repeats registration method
        elif choice == "Add New Habit":
            self.operation_functions.new_habit()

        # Option to delete a stored habit
        elif choice == "Delete Habit":
            self.operation_functions.delete_habit()

        # Change the frequency applied to a saved habit
        elif choice == "Change Habit Frequency":
            self.operation_functions.update_frequency()

        # User logs which habits have been completed for the current date
        elif choice == "Log Today's Habits":
            self.operation_functions.log_habits()

        # Opens further options to the user to view habits previously logged
        elif choice == "View Habits":
            self.operation_functions.view_habits()

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
