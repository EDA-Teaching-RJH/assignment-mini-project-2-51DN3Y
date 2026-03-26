import csv, re

class Session:
    '''
    Represents a general training session with date, distance, time, and notes.'''
    def __init__ (self, date, distance, time, notes):
        self.date = date
        self.distance = float(distance)
        self.time = time
        self.notes = notes

    def get_pace(self):
        '''
        Calculates the pace in minutes per kilometre. 
        Returnes None if distance is zero to avoid division by zero.'''
        minutes, seconds = map(int, self.time.split(":"))
        total_minutes = minutes + seconds /60
        if self.distance == 0:
            return None
        pace = total_minutes / self.distance
        return round(pace, 2)
    
    def to_list(self):
        '''
        Converts session data into a list format for CSV writing.'''
        return [self.date, self.distance, self.time, self.notes]
    
    def __str__(self):
        return f"Date: {self.date}, Distance: {self.distance} km, Time: {self.time}, Notes: {self.notes}, Pace: {self.get_pace()} min/km"

class RowingSession(Session):
    '''
    Extends Session to include rowing-specific data.
    In this case, stroke rate in strokes per minute (spm). 
    Assigns default stroke rate of 20 spm if one is not provided by the user.'''
    def __init__ (self, date, distance, time, notes, stroke_rate=20):  
        super().__init__(date, distance, time, notes)
        self.stroke_rate = stroke_rate
    
    def to_list(self):
        '''
        Converts rowing session data, including stroke rate, into a list format for CSV writing.'''
        return [self.date, self.distance, self.time, self.notes, self.stroke_rate]

    def __str__(self):
        return super().__str__() + f", Stroke Rate: {self.stroke_rate} spm"

class TrainingLog:
    '''
    Manages a collection of training sessions.
    Including adding, removing, saving, and loading sessions.'''
    def __init__(self):
        self.sessions = []
    
    def add_session(self, session):
        '''
        Add a new session to the training log.'''
        self.sessions.append(session)

    def remove_session(self, index):
        '''
        Remove a session by its index, if the index is valid.'''
        if 0 <= index < len(self.sessions):
            self.sessions.pop(index)

    def get_all_sessions(self):
        '''
        Returns a list of all stored sessions.'''
        return self.sessions
    
    def save_to_csv(self, training_results):
        '''
        Save all session(s) data to a CSV file.'''
        with open(training_results, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Distance", "Time", "Notes", "Stroke Rate"])
            for session in self.sessions:
                writer.writerow(session.to_list())
    
    def search_sessions(self, keyword):
        '''
        Search session notes for a keyword using case-insensitive regex.
        Returns a list of matching sessions.'''
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        results = []
        for session in self.sessions:
            if pattern.search(session.notes or ""):
                results.append(session)
        return results
    
    def load_from_csv(self, training_results):
        '''
        Load sessions from a CSV file and recreates session objects.
        Handles missing files and invalid data.'''
        try:
            self.sessions = []
            with open(training_results, "r") as file:
                reader = csv.reader(file)
                next(reader, None)

                for row in reader:
                    if len(row) >= 4:
                        try:
                            stroke_rate = int(row[4]) if len(row) > 4 else 20       # Optional stroke rate, default to 20 if not provided
                            session = RowingSession(row[0], row[1], row[2], row[3], stroke_rate)
                            self.add_session(session)
                        except ValueError:  # Ignore rows with invalid data and the initial header row
                            print(f"Skipping invalid session data in row: {row}")
                                
                if not self.sessions:
                    print("No existing sessions found.")

        except FileNotFoundError:
            print("No existing training log found.")