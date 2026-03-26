'''
Command Line Interface for recording rowing training sessions. 
Handles user input, displays menu options, interaction of the classes from training_log.py, 
and read/writes training data to csv file.
Author: Sidney Beacher, sb2435'''

from training_log import TrainingLog, RowingSession
import re, sys

def display_menu():
    print("\n -- Rowing Training Log --")
    print("1. Add session")
    print("2. Remove session")
    print("3. View sessions")
    print("4. Search sessions")
    print("5. Save and Exit")

def validate_date(date):
    '''
    Checks if the date is in the format DD/MM/YYYY using regex.
    Does not check if the date is logically correct.'''
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", date))

def validate_time(time):
    '''
    Checks if the time is in the format mm:ss using regex.'''
    return bool(re.match(r"^\d{1,2}:\d{2}$", time))

def validate_distance(distance):
    '''
    Ensures distance input is a positive number, including decimals.
    Returns True if valid, False otherwise.'''
    try:
        distance = float(distance)
        return distance > 0
    except ValueError:
        return False

def main():
    '''
    Main program loop that displays menu and handles/validates user input.
    Performs actions such as adding, removing, viewing, and searching training sessions.
    On exit, saves the training log to a csv file.'''    
    filename = "training_results.csv"
    log = TrainingLog()
    if len(sys.argv) > 1:   #if arguments provided, attempt to load from specified file
        filename = sys.argv[1]
    log.load_from_csv(filename)

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
            session = RowingSession(date, distance, time, notes, stroke_rate) #create session object and add to log
            log.add_session(session)
            print("Session Added!\n")

        elif choice == "2":
            print("\n---Remove session---")
            sessions = log.get_all_sessions()
            if not sessions:    #if no sessions, skip removal process and return to menu
                print("No sessions to remove!")
                continue
            for i in range (len(sessions)): #display sessions with index for user to select which to remove
                print(f"{i}: {sessions[i]}")
    
            while True:
                index_input = input("Enter the index of the session to remove: ")
                if not index_input.isdigit():
                    print("Invalid input. Please enter a valid session index.")
                    continue
                index = int(index_input)
                if index < 0 or index >= len(sessions):
                    print("Invalid index. Please enter a valid session index.")
                    continue

                log.remove_session(index)
                print("Session removed!\n")
                break

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