import questionary
from operation_functions import Functions
import bcrypt


class HabitOperations:
    def __init__(self, habit_tracker):
        self.habit_tracker = habit_tracker
        self.operation_functions = Functions(self, habit_tracker)

    # defining the log in function
    def login(self):
        print("You have selected Log In")
        print(
            """
            Please remember your username must be:
            More than 4 Characters but less than 12
            Will be case sensitive
            Cannot include special characters other than !@#$%^&*()-+=
            """
        )
        print(
            """
            Please remember your password must:
            Contain at least 1 Uppercase character
            Contain at least 1 Lowercase character
            Contain at least 1 Special character (!@#$%^&*()-_+=)
            """
        )

        while True:
            username = questionary.text("Please confirm your username:").ask()
            password = questionary.password(
                "Please confirm your password:"
            ).ask()

            # Validate the username format
            if not self.operation_functions.validate_username(username):
                print("Invalid username format. Please try again")
                self.operation_functions.clear_with_delay()
                continue

            if not self.operation_functions.validate_password(password):
                print("Invalid password format. Please try again.")
                self.operation_functions.clear_with_delay()
                continue

            username_column = (
                self.habit_tracker.credentials_worksheet.col_values(1)
            )
            password_column = (
                self.habit_tracker.credentials_worksheet.col_values(2)
            )

            # Check username & password against database
            if username in username_column:
                index = username_column.index(username)
                stored_password_hash = password_column[index]
                # Use bcrypt to verify the password
                if (bcrypt.checkpw(
                        password.encode('utf-8'),
                        stored_password_hash.encode('utf-8'))):
                    print("Login successful!")
                    self.operation_functions.clear_with_delay()
                    self.habit_tracker.logged_in_user = username
                    # Proceed to Main Menu
                    self.main_options()
                    break
                else:
                    print("Incorrect password.")
                    self.operation_functions.clear_with_delay()
            else:
                print("Username not found.")
                self.operation_functions.clear_with_delay()

        return False

    # defining the register function
    def register(self):

        print("You have selected Register")
        print(
            """
            Please note your username must be:
            More than 4 Characters but less than 12
            Will be case sensitive
            Cannot include special characters other than !@#$%^&*()-+=
            """
        )
        print(
            """
            Please note your password must:
            Contain at least 1 Uppercase character
            Contain at least 1 Lowercase character
            Contain at least 1 Special character (!@#$%^&*()-_+=)
            """
        )
        while True:
            # User creates a new username
            new_user = questionary.text("Please choose your username:").ask()

            username_column = (
                self.habit_tracker.credentials_worksheet.col_values(1)
            )

            # Validate the username format
            if not self.operation_functions.validate_username(new_user):
                print("Invalid username format. Please try again")
                continue

            if new_user in username_column:
                # If the username exists the user will need
                # to try again
                print("The username already exists. Please try again.")
                self.operation_functions.clear_with_delay()
            else:
                # If the username is new, the User can then add a password
                new_password = (
                    questionary.password("Please choose your password:")
                    .ask()
                )

                # Validate the password format
                if not self.operation_functions.validate_password(
                    new_password
                ):
                    print("Invalid password format. Please try again")
                    self.operation_functions.clear_with_delay()
                    continue

                # Use the validated username and password
                if (
                    self.operation_functions.validate_username(new_user)
                    and
                    self.operation_functions.validate_password(new_password)
                ):

                    # Use bcrypt to hash the password
                    hashed_password = bcrypt.hashpw(
                        new_password.encode('utf-8'),
                        bcrypt.gensalt()
                    )

                    # Add the new user's credentials to the next available row.
                    next_row = len(username_column) + 1
                    self.habit_tracker.credentials_worksheet.update_cell(
                        next_row, 1, new_user
                    )
                    self.habit_tracker.credentials_worksheet.update_cell(
                        next_row, 2, hashed_password.decode('utf-8')
                    )

                    self.habit_tracker.logged_in_user = new_user

                    print("Registration successful!")
                    self.operation_functions.clear_with_delay()
                    # Once the credentials are confirmed the User
                    # can start to build their habits
                    self.operation_functions.new_habit()
                    break

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
                "Log Out",
                "Delete Account",
                "Quit"]
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
            self.operation_functions.clear_with_delay()
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
                self.main_options()

        # Use can exit the application completely
        elif choice == "Quit":
            print("Quiting the application...")
            self.operation_functions.clear_and_exit()
            return
