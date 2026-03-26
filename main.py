from training_log import TrainingLog, Session
import re

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
            print("\n---Add Session---")
            
            while True:
                date = input("Enter date (DD/MM/YYYY): ")
                if re.match(r"^\d{2}/\d{2}/\d{4}$", date):
                    break
                else:
                    print("Invalid date format. Please enter in DD/MM/YYYY format.")
            
            while True:
                try:
                    distance = float(input("Enter distance (km): "))
                    if distance <= 0:
                        print("Distance cannot be zero or negative. Please enter a valid distance.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number for distance.")

            while True:
                time = input("Enter time (mm:ss): ")
                if re.match(r"^\d{1,2}:\d{2}$", time):
                    break
                else:
                    print("Invalid time format. Please enter in mm:ss format.")

            notes = input("Enter notes from session: ")

            session = Session(date, distance, time, notes)
            log.add_session(session)
            print("Session Added!\n")

        elif choice == "2":
            print("\n---Remove session---")
            sessions = log.get_all_sessions()

            for i in range (len(sessions)):
                print(f"{i}:{sessions[i]}")
            
            index = int(input("Enter the index of the session to remove: "))
            log.remove_session(index)
            print("Session removed!\n")

        elif choice == "3":
            print("\n---View sessions---")
            sessions = log.get_all_sessions()
            
            if not sessions:
                print("No sessions found!")
            else:
                for session in sessions:
                    print(session)

        elif choice == "4":
            print("\n---Search sessions---")
            keyword = input("Enter keyword to search: ")
            results = log.search_sessions(keyword)

            if not results:
                print("No matching sessions found!")
            else:
                for session in results:
                    print(session)

        elif choice == "5":
            print("\n---Saving and exiting---")
            log.save_to_csv("training_results.csv")
            print("Training log saved. Goodbye!")
            break
        
        else:
            print("Invalid option. Please enter a number between 1 and 5.")
            
main()