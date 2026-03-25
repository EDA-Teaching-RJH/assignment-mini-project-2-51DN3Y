import csv
import re
from turtle import write

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
        file = open(training_results, "w")
        writer = csv.writer(file)

        for session in self.sessions:
            writer.writerow([session.date, session.distance, session.time, session.notes])

        file.close()
    
    def search_sessions(self, keyword):
        results = []
        
        for session in self.sessions:
            if keyword.lower() in session.notes.lower():
                results.append(session)

        return results