# Syntecxhub-python-internship
Internship tasks and weekly submissions for Python Programming at SYNTECXHUB.
# Week 1 – Task 1: Python Calculator

A simple and clean Python calculator built as part of my SyntecxHub Internship.  
This program takes two numbers, accepts an operator (+, -, *, /), performs the calculation, and returns the result with basic error handling.  
Designed to practice core Python concepts such as functions, user input, and conditional logic while maintaining readable and beginner-friendly code.
#  Number Guessing Game (Python)

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

##  Run the Program

Use the following command in your terminal:

```bash
python guess_game.py
