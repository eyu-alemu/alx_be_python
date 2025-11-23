# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []  # Check for implementation of a list

    while True:
        display_menu()  # Call to display_menu

        # Parse the user choice as an integer (not just string)
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added.")
            else:
                print("Empty item name, nothing added.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print(f"'{item}' is not in your shopping list.")

        elif choice == 3:
            if shopping_list:
                print("Current shopping list:")
                for idx, itm in enumerate(shopping_list, start=1):
                    print(f"{idx}. {itm}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
