from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        days = int(input("Enter number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        print("Future Date after", days, "days:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if _name_ == "_main_":
    main()