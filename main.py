from training_log import TrainingLog, Session, RowingSession
import re, sys

def display_menu():
    print("\n -- Rowing Training Log --")
    print("1. Add session")
    print("2. Remove session")
    print("3. View sessions")
    print("4. Search sessions")
    print("5. Save and Exit")

def validate_date(date):
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", date))

def validate_time(time):
    return bool(re.match(r"^\d{1,2}:\d{2}$", time))

def validate_distance(distance):
    try:
        distance = float(distance)
        return distance > 0
    except ValueError:
        return False

def main():    
    filename = "training_results.csv"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        log.load_from_csv(filename)
    log = TrainingLog()
    log.load_from_csv("training_results.csv")

    while True:
        display_menu()
        choice = input("Enter valid option (1-5): ")

        if choice == "1":
            print("\n---Add Session---")
            while True:
                date = input("Enter date (DD/MM/YYYY): ")
                if validate_date(date):
                    break
                else:
                    print("Invalid date format. Please enter in DD/MM/YYYY format.")
            
            while True:
                distance_input = input("Enter distance (km): ")
                if validate_distance(distance_input):
                    distance = float(distance_input)
                    break
                else:
                    print("Distance must be a positive number.")

            while True:
                time = input("Enter time (mm:ss): ")
                if validate_time(time):
                    break
                else:
                    print("Invalid time format. Please enter in mm:ss format.")
            
            while True:
                stroke_rate_input = input("Enter stroke rate (spm, optional press ENTER to default (20spm)): ")
                if stroke_rate_input == "":
                    stroke_rate = 20
                    break
                try:
                    stroke_rate = int(stroke_rate_input)
                    break
                except ValueError:
                    print("Invalid stroke rate.")

            notes = input("Enter notes from session: ")
            session = RowingSession(date, distance, time, notes, stroke_rate)
            log.add_session(session)
            print("Session Added!\n")

        elif choice == "2":
            print("\n---Remove session---")
            sessions = log.get_all_sessions()
            for i in range (len(sessions)):
                print(f"{i}: {sessions[i]}")
            try:
                index = int(input("Enter the index of the session to remove: "))
                log.remove_session(index)
                print("Session removed!\n")
            except (ValueError, IndexError):
                print("Invalid index. Please enter a valid session index.")

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
            print("Training log saved. Goodbye!\n")
            break
        
        else:
            print("Invalid option. Please enter a number between 1 and 5.")
            
main()