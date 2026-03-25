import csv
import re

class Session:
    def __init__ (self, date, distance, time, notes):
        self.date = date
        self.distance = distance
        self.time = time
        self.notes = notes
