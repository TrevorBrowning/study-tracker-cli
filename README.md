# Study Tracker CLI

A simple command-line tool for tracking and analyzing study sessions from a text file.


## What It Does

The program reads study session data from a text file and lets you interact with it through a menu-driven CLI.

You can:

- View all study sessions
- See total number of sessions and total minutes studied
- Filter sessions by subject
- Filter sessions by duration range
- Sort sessions by longest duration
- Exit cleanly from the menu


## Data Format

The program expects a file named `study_data.txt` in the same directory.

Each line should follow this format:


Example:

2025-01-08, Monday, Python, 45
2025-01-09, Tuesday, HTML, 30
2025-01-10, Wednesday, Python, 60


Blank lines or malformed entries are ignored.



## How to Run

Make sure you have Python 3 installed.

From the project directory:


python study_tracker.py



## Example Output:
### Study Session Analyzer

1. Show all sessions
2. Show total sessions and duration
3. Filter by subject
4. Filter by duration
5. Show longest sessions
6. Exit


## Why This Project Exists

### This project was built to:

- Practice reading and validating file data

- Reinforce working with lists and tuples

- Learn how to structure a small but complete Python program

- Design a usable command-line interface

- Practice refactoring and cleanup after functionality was complete


## Future Improvements

- Input validation

- Filter by date

- Export data to CSV

- Read data from multiple file types (CSV)