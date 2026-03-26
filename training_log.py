import csv, re

class Session:
    def __init__ (self, date, distance, time, notes):
        self.date = date
        self.distance = float(distance)
        self.time = time
        self.notes = notes

    def get_pace(self):
        minutes, seconds = map(int, self.time.split(":"))
        total_minutes = minutes + seconds /60
        pace = total_minutes / self.distance
        return round(pace, 2)
    
    def to_list(self):
        return [self.date, self.distance, self.time, self.notes]
    
    def __str__(self):
        return f"Date: {self.date}, Distance: {self.distance} km, Time: {self.time}, Notes: {self.notes}, Pace: {self.get_pace()} min/km"

class TrainingLog:
    def __init__(self):
        self.sessions = []
    
    def add_session(self, session):
        self.sessions.append(session)

    def remove_session(self, index):
        if 0 <= index < len(self.sessions):
            self.sessions.pop(index)

    def get_all_sessions(self):
        return self.sessions
    
    def save_to_csv(self, training_results):
        with open(training_results, "a", newline="") as file:
            file.seek(0)
            empty = file.read(1) == ""
            writer = csv.writer(file)
            
            if empty:
                writer.writerow(["Date", "Distance", "Time", "Notes"])

            for session in self.sessions:
                writer.writerow(session.to_list())
    
    def search_sessions(self, keyword):
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        results = []
        
        for session in self.sessions:
            if pattern.search(session.notes or ""):
                results.append(session)
        return results
    
    def load_from_csv(self, training_results):
        try:
            self.sessions = []
            with open(training_results, "r") as file:
                reader = csv.reader(file)
                next(reader, None)
                
                if not self.sessions:
                    print("No existing sessions found.")

                for row in reader:
                    if len(row) == 4:
                        session = Session(row[0], row[1], row[2], row[3])
                        self.add_session(session)

        except FileNotFoundError:
            print("No existing training log found.")