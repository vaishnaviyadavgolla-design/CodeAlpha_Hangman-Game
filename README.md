# 🎮 CodeAlpha Hangman Game

A simple **console-based Hangman game** built in Python as part of the **CodeAlpha Python Internship**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📝 Description

This is a classic text-based Hangman game where the player guesses letters to reveal a hidden word. The game features ASCII art that progressively draws a hangman figure with each incorrect guess. The player has **6 chances** to guess the word correctly before the game is over.

---

## 🎯 Features

- 🎲 **Random Word Selection** — Picks a random word from a predefined list of 5 words
- 🖼️ **ASCII Art Hangman** — Visual hangman figure that builds with each wrong guess
- ✅ **Input Validation** — Handles invalid inputs, duplicate guesses, and single-letter checks
- 📊 **Game State Tracking** — Displays guessed letters, remaining attempts, and word progress
- 🏆 **Win/Loss Detection** — Clear messages for both outcomes with the correct word revealed

---

## 📸 Screenshots

### Game Start
![Game Start](screenshots/start.png)

### Playing
![Playing](screenshots/playing.png)

### Game Won
![Game Won](screenshots/won.png)

---

## 📋 Requirements

- **Python 3.x** (Python 3.6 or higher recommended)
- No external libraries required — uses only Python's built-in `random` module

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/maddikuntarahul/CodeAlpha_ProjectName-.git
cd CodeAlpha_ProjectName-
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
> **Note:** No external dependencies are required. The `requirements.txt` file is included for project completeness.

---

## ▶️ Usage

Run the game with:
```bash
python main.py
```

### How to Play
1. The game randomly selects a word from the word list
2. You see the word displayed as underscores (`_ _ _ _ _`)
3. Enter one letter at a time to guess the word
4. **Correct guess** → The letter is revealed in its position(s)
5. **Incorrect guess** → A body part is added to the hangman (max 6)
6. **Win** → Guess all letters before running out of attempts
7. **Lose** → 6 incorrect guesses and the hangman is complete

---

## 🛠️ Tech Stack

| Technology | Purpose              |
|------------|----------------------|
| Python 3   | Core programming     |
| `random`   | Random word selection |

---

## 📂 Project Structure

```
CodeAlpha_Hangman_Game/
│
├── main.py             # Main game logic
├── README.md           # Project documentation
├── LICENSE             # MIT License
├── requirements.txt    # Dependencies (none required)
├── .gitignore          # Git ignore rules
└── screenshots/        # Game screenshots
    ├── start.png
    ├── playing.png
    └── won.png
```

---

## 🔑 Key Concepts Demonstrated

| Concept       | Usage                                          |
|---------------|------------------------------------------------|
| `random`      | `random.choice()` to pick a word from the list |
| `while` loop  | Game loop runs until win or loss               |
| `if-else`     | Guess validation, win/loss checks              |
| `strings`     | Building the word display with `_` and letters |
| `lists`       | Word list and tracking guessed letters         |
| `functions`   | Modular code organization                      |

---

## 👩‍💻 Author

**Rahul Maddikunta** — CodeAlpha Python Programming Intern

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
