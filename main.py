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
    log = TrainingLog()
    log.load_from_csv("training_results.csv")

    while True:
        display_menu()
        choice = input("Enter valid option (1-5): ")

        if choice == "1":
            print("---Add Session---")
            date = input("Enter date (DD/MM/YYYY): ")
            distance = float(input("Enter distance (km): "))
            time = input("Enter time (mm:ss): ")
            notes = input("Enter notes from session: ")

            session = Session(date, distance, time, notes)
            log.add_session(session)
            print("Session Added!\n")

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