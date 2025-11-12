# GRIT - Reminder & Motivation App

A simple desktop application built with Python and Tkinter to help you stay consistent and motivated by scheduling reminders for your daily tasks.

## Features
- Add tasks with a specific time (supports flexible time formats)
- Get motivational quotes with each reminder
- User-friendly GUI for task management
- Automatic daily rollover for missed tasks

## How to Run
1. **Requirements:**
   - Python 3.x (recommended 3.7+)
   - Tkinter (usually included with Python)

2. **Run the App:**
   - Open a terminal in the project directory.
   - Run:
     ```powershell
     python GRIT.py
     ```
   - On first launch, enter your name when prompted.
   - Add tasks and set reminder times in the format `HH:MM` (24-hour) or common variants (e.g., `9:30`, `930`, `9am`).

## File Structure
- `GRIT.py` - Main application code
- Other files (e.g., `function.html`, `json.html`, etc.) are not required for this app

## Usage Notes
- The app will notify you with a motivational quote when it's time for a scheduled task.
- If the scheduled time has already passed today, the reminder will be set for the next day.

## License
This project is provided for educational and personal use.
