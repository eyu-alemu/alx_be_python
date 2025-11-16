while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    else:
        print("Please enter a valid task.")
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
print()
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority level."
if time_bound == "yes":
    reminder += "It requires immediate attention today!"
else:
    reminder += "Consider completing it when you have free time."
print("Reminder:", reminder)
