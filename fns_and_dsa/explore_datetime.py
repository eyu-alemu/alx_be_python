# explore_datetime.py

from datetime import datetime, timedelta


def display_current_datetime():

    # get current local date & time :contentReference[oaicite:0]{index=0}
    current_date = datetime.now()
    # format nicely :contentReference[oaicite:1]{index=1}
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date


def calculate_future_date(current_date, days_to_add):
    # use timedelta to add days :contentReference[oaicite:2]{index=2}
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date


def main():
    # Part 1 — display current
    now = display_current_datetime()

    # Part 2 — get user input and calculate future date
    try:
        days_input = int(
            input("Enter the number of days to add to the current date: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid integer number of days.")
        return

    calculate_future_date(now, days_input)


if __name__ == "__main__":
    main()
