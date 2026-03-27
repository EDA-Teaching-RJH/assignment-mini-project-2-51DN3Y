# Developer Journal - Mini Project 2

## Overview

As part of my mini project 2, I designed and implemented a rowing training log system using python. This allows the user to record data from each session, so they can go back and review a session, or manipulate the data to create, for example, a pace graph. The aim was to apply object-oriented programming (OOP), file handling using a CSV file, input/data validation, and testing. I used my skills I developed through the previous mini project (1), the recent workshops 7-9, and my lecture notes.

--

## Object-Oriented Programming

One of the main concepts applied in this project was object-oriented programming (OOP).

I created three classes in 'training_log.py':

- 'Session', which represents a single rowing session
- 'TrainingLog', which manages multiple sessions
- 'RowingSession', which is a subclass of 'Session' which allows for rowing specific data to be recorded, in this case, stroke rate (spm)

For example, the 'Session' class stores attributes like date, distance, and time. It also includes a method to calculate pace, based on the users input for distance and time. This shows how behaviour can be attached to data, rather than handled externally. I used my knowledge from workshop 9 to create inheritance using a subclass 'RowingSession' with the main class 'Session'.

--

## Data Validation

Within my code I implemented input validation using regular expressions (regex). I did this based off of my knowlegde and understanding from workshop 8.

Examples include:

- Date format validation ('DD/MM/YYYY')
- Time format validation ('MM:SS')

Although the validation ensures the correct format is entered, a limitation is that it is not able to validate logical correctness e.g. checking that the month value isn't greater than 12. Due to time constraints, I chose not to extend the validation further, but it is noted as a potential improvement. An alternative could be to use the python library datetime, over regex in this specific case.

--

## File Handling (CSV)

This project uses CSV file handling to store and retreive session data recorded by the user.

This connects with course topics, specifically workshop 8, which includes:

- Reading to a CSV file
- Writing to a CSV file
- Consistent data storage

The 'TrainingLog' class handles saving and loading sessions.

--

## Testing (pytest)

I created a separate file called 'test_training_log', and used 'pytest' to test key functionality.

Examples include:

- Session creation
- Session deletion
- Pace calculation
- Rogue input for 'distance' value

Some pytest features (e.g. 'tmp_path') were initially unfamiliar, but I used them to safely test file operations without affecting real data. This testing helped improve reliability of the program.

--

## Program Design

The program follows a modular structure.

- The main user interface ('main.py')
- Data logic ('training_log.py')
- Testing ('test_training_log.py')

Having this structure helps with testing, code organisation, maintainability, and readability. For example, to improve readability, I included accurate comments and docstrings using my knowledge from previous lecture.

--

## Challenges and Decisions

One challenge I experienced was balancing functionality with time constraints.

For example:

- I implemented regex correctly, but did not extend it to allow for full logical date validation.
- I initially did not integrate all classes fully nor have the required inheritance. I later refractored this to improve structure, and meet the specification.

--

## Improvements

If I had more time, I would:

- Improve data validation (e.g. checking valid days/months)
- Add more robust error handling
- Expand arguments use
- Enhance the user interface by using clearer prompts or using a GUI
- Expand test coverage to improve maintainability
- Add more external libraries such as 'matplotlib' to display a distance time graph or a pace graph, so the user can track their progress more clearly.
- Add a feature so that the user can track their power, in watts, from each session.

--

## Conclusion

In conclusion, this project helped reinforce key programming concepts from the module particularly OOP, file handling, arguments, and testing. It also highlighted the importance of planning, structure, and iterative improvements logged through Git commits.
