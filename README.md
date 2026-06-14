# 🐍 Python Projects — Manish Bhagane

A collection of Python programs built during my self-learning journey.
All projects were written from scratch, debugged independently, and progressively improved — several refactored into cleaner versions to demonstrate optimisation thinking.

---

## 📁 Projects

### 🔐 Access Control System (v1 & v2)
A password-protected access control program with a 3-attempt limit and numeric input validation.
- **v1** — Fully working version using nested loop structure
- **v2 (Optimised)** — Refactored into a cleaner, tighter single loop — same result, less code
- Concepts used: `while` loop, `try/except`, input validation, `break`/`continue`

---

### 🪖 Outpost Management System
A text-based military outpost management tool with a full interactive menu system.
- View and update food supplies (rice, dal, vegetables) in kg
- Add soldiers/trainees with unique IDs stored in a dictionary
- Calculate how many weeks current supplies will last based on active soldier count
- Concepts used: dictionaries, arithmetic logic, loops, menu-driven design

---

### 🚀 Space Freight Smuggler
A cargo management game set in space — load titanium, platinum, and alien artifacts onto your ship without exceeding the 5,000 kg weight limit.
- Multi-item inventory system with live weight and cost tracking
- Confirmation prompts before every load action
- Reduce/remove cargo menu with input validation
- Safety sensor check before liftoff with total profit calculation
- Concepts used: nested loops, `try/except`, conditionals, inventory logic, game flow

---

### 🎲 Guessing Game
Guess a randomly generated number between 1 and 10.
- Directional hints after each wrong guess (too high / too low)
- Nested loop handles invalid (non-numeric) input before checking the guess
- Concepts used: `random` module, nested loops, `try/except`, conditional logic

---

### ❤️ Love Calculator
Enter two names and get a randomised love compatibility percentage.
- Input validation loop ensures neither name field is left blank
- Concepts used: `random` module, `while` loop, input validation

---

### 🧮 Old Age Persistent Calculator
A basic calculator that carries the result of each operation forward into the next.
- Supports `+`, `-`, `*`, `/` with operator validation
- Prompts the user to continue or exit after each calculation
- Concepts used: `while` loop, operator validation, persistent state via variable reassignment

---

### 🔢 calculator_v2.py
A command-line calculator built using def functions.
Features:
- Basic arithmetic operations (+, -, *, /, //, **)
- Continuous calculation until user exits
- Input validation using try/except
  
---

### 📱 calculator_v3.py
An upgraded version of the calculator with additional features.
Features:
- All features of v2
- Error handling for invalid numbers
- Division by zero protection
- Invalid sign detection
- Calculation history (press h to view)

---

### ⏰ Good Morning / Good Night Greeter (x2 versions)
Greets the user based on the time of day — built in two versions:
- **Manual** — user inputs the hour themselves
- **Automated** — uses Python's `time` module to detect current time automatically
- Concepts used: `datetime`/`time` module, conditionals, modular thinking

---

### 🎯 Even & Odd Checker (x2 versions)
Built twice to demonstrate code optimisation:
- **Version 1** — Standard `for` loop, ~15 lines
- **Version 2** — Refactored using `range(start, stop, step)`, ~3 lines
- Concepts used: `range()` with step, loops, refactoring instinct

---

### 💻 Chip Calculator
Input your CPU clock speed and get a performance classification (budget / mid-range / high-end / legacy).
- Concepts used: conditionals, input handling, numeric comparison

---

### 🎮 Weird Ladder Game
A text-based take on the classic Snake and Ladder concept.
- Concepts used: `random` module, loops, game state logic

---

## 🛠️ Concepts & Techniques Used
- Error handling (`try/except`)
- Loop logic (`while`, `for`, `break`, `continue`)
- Data structures (dictionaries, variables)
- Code refactoring (v1 → v2 optimisation)
- Python standard libraries (`random`, `time`, `datetime`)
- Walrus operator (`:=`) for assignment expressions
- Modular thinking and progressive improvement

---

### 🎓 Student Database (student_db.py)
A class-based student record system with search by ID.
- Concepts used: OOP, `class`, `__init__`, `__str__`, lists, `for` loop

---

### 🎓 Student Database v2 (student_db_v2.py)
Full CRUD student management system with persistent file storage.
- Add, search, update, delete students
- Data saved to `.txt` file — persists between sessions
- Concepts used: OOP, file handling (`open`, `read`, `write`, `append`), CRUD logic

---

### 🌸 Flower Database (flower_db.py)
A class-based flower record system.
- Concepts used: OOP, `class`, `__init__`, `__str__`, lists

---

### 📞 Phonebook (phonebook.py)
A command-line phonebook with full CRUD functionality and file persistence.
- Add, search, delete contacts
- Input validation for phone numbers
- Concepts used: OOP, file handling, input validation, string methods

  ---

  ### 🎯 Brutal Guessing Game
Guess a random number between 1 and 100 — with only 3 attempts!
- Directional hints after each wrong guess (too high / too low)
- Reveals the answer if you run out of attempts
- Shows total attempts taken on a win
- Play again option after each round
- Concepts used: `random` module, nested loops, `try/except`, flag variable

  ---

## 📬 Contact
**Manesh Bhagane**
📧 manishbhagane127@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/manesh-bhagane)
📍 Mumbai, India
