# daily_reminder.py

# Prompt for a single task
task = input("Enter the task: ")
priority = input("Enter the priority level (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Match Case statement to process task based on priority
match priority:
    case "high":
        reminder = f"The task '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"The task '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"The task '{task}' is a LOW priority task."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority level."

# Use if statement to modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Print the final customized reminder
print(reminder)
