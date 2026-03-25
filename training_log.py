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
