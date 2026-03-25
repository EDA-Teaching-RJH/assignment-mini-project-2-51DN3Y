import csv
import re

class Session:
    def __init__ (self, date, distance, time, notes):
        self.date = date
        self.distance = distance
        self.time = time
        self.notes = notes

class TrainingLog:
    def __init__(self):
        self.sessions = []
    
    def add_session(self, session):
        self.sessions.append(session)

    def get_all_sessions(self):
        return self.sessions
    
    def save_to_csv(self, training_results):
        with open(training_results, "w", newline='') as file:
            writer = csv.writer(file)

            for session in self.sessions:
                writer.writerow([session.date, session.distance, session.time, session.notes])
    
    def search_sessions(self, keyword):
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        results = []
        
        for session in self.sessions:
            if pattern.search(session.notes):
                results.append(session)

        return results
    
    def load_from_csv(self, training_results):
        try:
            with open(training_results, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 4:
                        session = Session(row[0], row[1], row[2], row[3])
                        self.add_session(session)
        
        except FileNotFoundError:
            print("No existing training log found.")