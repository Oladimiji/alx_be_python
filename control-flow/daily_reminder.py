# daily_reminder.py

# Prompt for a single task
task = input("Enter your task description: ")
priority = input("Enter the priority of the task (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Start the customized reminder
print("\nReminder:")

# Use match-case to handle different priority levels
match priority:
    case "high":
        message = f"Task: {task} [HIGH PRIORITY]"
    case "medium":
        message = f"Task: {task} [MEDIUM PRIORITY]"
    case "low":
        message = f"Task: {task} [LOW PRIORITY]"
    case _:
        message = f"Task: {task} [UNSPECIFIED PRIORITY]"

# Add urgency if time-bound
if time_bound == "yes":
    message += " — This is a time-sensitive task that requires immediate attention today!"

# Print the final message
print(message)