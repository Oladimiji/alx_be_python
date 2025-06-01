def get_task_details():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    while priority not in ["high", "medium", "low"]:
        priority = input("Invalid input. Please enter high, medium, or low: ").lower()

    time_bound = input("Is it time-bound? (yes/no): ").lower()
    while time_bound not in ["yes", "no"]:
        time_bound = input("Invalid input. Please enter yes or no: ").lower()

    return task, priority, time_bound

def provide_reminder(task, priority, time_bound):
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"

    if time_bound == "yes":
        reminder_message = f"{base_message} that requires immediate attention today!"
    else:
        if priority == "low":
            reminder_message = f"{base_message}. Consider completing it when you have free time."
        else:
            reminder_message = f"{base_message}. Try to complete it as soon as possible."

    print(f"Reminder: {reminder_message}")
