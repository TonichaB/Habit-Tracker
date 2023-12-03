from habit_tracker import HabitTracker
from habit_operations import HabitOperations
from operation_functions import Functions

if __name__ == "__main__":
    habit_tracker = HabitTracker()
    habit_operations = HabitOperations(habit_tracker)
    habit_tracker.habit_operations = habit_operations
    habit_tracker.startup()
