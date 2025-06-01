# daily_reminder.py

# Prompt for a single task
task = input("Enter a task: ")
priority = input("Enter the priority level (high/medium/low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Match Case statement to process task based on priority
match priority:
    case "high":
        reminder = f"The task '{task}' has HIGH priority."
    case "medium":
        reminder = f"The task '{task}' has MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' has LOW priority."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority."

# If time-sensitive, append extra message
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Print the final customized reminder
