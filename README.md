# Syntecxhub-python-internship
Internship tasks and weekly submissions for Python Programming at SYNTECXHUB.
# Week 1 – Task 1:
# Project 1: Python Calculator

A simple and clean Python calculator built as part of my SyntecxHub Internship.  
This program takes two numbers, accepts an operator (+, -, *, /), performs the calculation, and returns the result with basic error handling.

The project focuses on practicing core Python concepts such as user input, functions, conditionals, and clean code structure. It is designed to be beginner-friendly while demonstrating clear logic and proper handling of invalid inputs.

---

## Features

- Supports four basic arithmetic operations: addition, subtraction, multiplication, and division  
- Uses functions to organize and process calculations  
- Handles invalid operators and incorrect inputs  
- Returns clear, readable output for each operation  
- Simple structure suitable for beginners learning Python fundamentals

---

## How It Works

1. The program asks the user to input two numbers  
2. The user selects an operator: +, -, *, or /  
3. The calculator processes the operation and displays the result  
4. If the user enters an invalid operator or non-numeric input, the program handles the error gracefully

---

## Technologies Used

- Python 3
- Functions for modular code
- Conditional statements for operation control
- Input handling for user interaction

---


#  Project-2 : Number Guessing Game (Python)

A simple yet feature-rich **Python Number Guessing Game** that uses loops, conditionals, and the `random` module. The game challenges the user to guess a randomly generated number with hints, difficulty modes, attempt tracking, and a replay option.

---

##  Features

-  **Random Number Generation** using `random.randint()`
- **Difficulty Levels**
  - Easy (1–20)
  - Medium (1–50)
  - Hard (1–100)
-  **Higher / Lower Hints** after every guess
-  **Replay Support** — play unlimited rounds
- **Best Score Tracking** — records the lowest number of attempts
-  Input validation (avoids crashes)
-  Beginner-friendly logic using **loops and conditionals**

---

##  How It Works

1. The player selects a difficulty level.
2. The program generates a random number within the chosen range.
3. The player keeps guessing until they find the correct number.
4. After every guess, the game gives **Higher/Lower hints**.
5. The game tracks the number of attempts.
6. It compares attempts with the **best score** and updates it.
7. The user can **play again** or exit the game.

---

## 🛠 Technologies Used

- **Python 3**
- `random` module
- Loops (`while`)
- Conditionals (`if/elif/else`)
- User input handling

---
# Week 2 – Task 2:
# Project:3 Student Management System (CLI)

A simple and structured Student Management System built using Python.
This command-line application allows users to add, update, delete, and view student records while persisting data using file storage.

The project focuses on practicing Object-Oriented Programming (OOP) concepts, file handling, and basic input validation. It is designed to be beginner-friendly while demonstrating clean code structure and real-world logic.

---

## Features

- Add new student records with unique student IDs
- Update existing student details (name and grade)
- Delete student records by ID
- List all student records in a formatted table
- Persistent storage using a JSON file
- Prevents duplicate student IDs
- Clean and readable console output

---

## How It Works

1. The program displays a menu with available operations
2. The user selects an option (Add / Update / Delete / List / Exit)
3. Student details are entered via the command line
4. Records are saved automatically to a JSON file
5. Data is loaded from the file each time the program runs

---

## Technologies Used

- Python 3
- Object-Oriented Programming (Classes & Objects)
- JSON file handling for data persistence
- Conditional statements and loops
- Basic input validation
- CLI-based user interaction

# Week 3 – Task 2: CSV to Excel Converter (CLI)

The project focuses on practicing real-world data preparation techniques, building CLI automation, structured logging, and error-handling mechanisms. It is designed to be lightweight, user-friendly, and suitable for reporting or data-processing workflows.
---

## Features

- Read CSV files from local storage
- Clean and normalize column names
- Handle missing values safely
- Automatic parsing for date columns
- Simple column rename rules (ID normalization)
- Export processed data to Excel (`.xlsx`)
- CLI flags for input file and output path
- Logging and structured error messages for invalid files
- Fast execution suitable for automation pipelines

---

## How It Works

1. The user provides input CSV file using CLI flags
2. The program reads the file using pandas
3. Data is cleaned and normalized
4. Date columns are parsed automatically if present
5. Output is written to Excel format using openpyxl engine
6. Logs are generated for each step and errors are handled gracefully

---

## Installation

Ensure you have Python installed, then install required dependencies:

```sh
pip install pandas openpyxl
```

---

## Usage

Run the script from terminal:

```sh
python converter.py -i input.csv -o output.xlsx
```

### CLI Flags
| Flag | Description |
|------|-------------|
| `-i`, `--input`  | Path to input CSV file |
| `-o`, `--output` | Path to output Excel file (`.xlsx`) |

---

## Project Structure

```
CSV-Excel-Converter/
│── converter.py
│── README.md
│── sample.csv (optional test file)
```

---

## Error Handling

The program validates and handles:

- Missing or incorrect file paths
- Empty CSV files
- Corrupted or badly formatted CSV files
- Incorrect output file extension
- Unexpected runtime failures

All errors are logged and displayed without breaking execution flow.

---

## Future Scope

- Can be integrated into reporting automation
- Can be extended with advanced cleaning rules
- Can support multiple file conversions
- Can be packaged into executable CLI tools


---


##  Run the Program

Use the following command in your terminal:

```bash

python calculator.py
python guess_game.py
python main.py
