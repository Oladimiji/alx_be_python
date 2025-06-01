# daily_reminder.py

# Prompt for a single task
task = input("Enter your task description: ")
priority = input("Enter the priority of the task (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Match Case statement to process task based on priority
match priority:
    case "high":
        level = "HIGH"
    case "medium":
        level = "MEDIUM"
    case "low":
        level = "LOW"
    case _:
        level = "UNKNOWN"

# Base reminder message
reminder = f"The task '{task}' is a {level} priority task."

# Modify the reminder if time-bound
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Final customized output
print(reminder)
