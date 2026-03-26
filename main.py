from training_log import TrainingLog, Session
import csv

def display_menu():
    print("\n -- Rowing Training Log --")
    print("1. Add session")
    print("2. Remove session")
    print("3. View sessions")
    print("4. Search sessions")
    print("5. Save and Exit")


def main():
    

    while True:
        display_menu()
        choice = input("Enter valid option (1-5): ")

        if choice == "1":
            print("Adding session...")
        elif choice == "2":
            print("Removing session...")
        elif choice == "3":
            print("Viewing sessions...")
        elif choice == "4":
            print("Searching sessions...")
        elif choice == "5":
            print("Saving and exiting...")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")
            
main()