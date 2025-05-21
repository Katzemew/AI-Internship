# Rule-Based Trivia Chatbot

Welcome to the **Rule-Based Trivia Chatbot**! This is a terminal-based Python chatbot that quizzes you with trivia questions from various domains such as general knowledge, science, history, and more. You can choose a domain, answer randomized multiple-choice questions, and track your score — with the freedom to exit at any point. The bot is built using simple Python logic, file handling, and user input handling, making it lightweight and beginner-friendly.

## How to Play

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the project.
4. Make sure your trivia questions are formatted correctly inside `trivia_questions.txt`.
5. Run the Python script:

   ```bash
   python trivia_bot.py
   ```
6. Select your desired category from the list.
7. Answer questions by typing `A`, `B`, `C`, or `D`.
8. Type `exit` anytime to quit early — your score will still be shown.
9. After finishing a quiz, choose whether you want to retry or exit.

## Features

* **Domain Selection**: Choose from different trivia categories before starting the game.
* **Randomized Questions**: Each game presents randomized questions within the selected domain.
* **Graceful Exit**: You can type `exit` at any time to quit and still see your score.
* **Replay Prompt**: After each round, the bot asks if you want to play again.
* **Clean Terminal Output**: Optimized for terminal or command line use (VS Code, cmd, PowerShell, etc.).

## Requirements

* Python 3.x

# Install Requirements

Run this in your terminal (if you don't already have Python 3 installed):

```bash
pip install -r requirements.txt
```

> **Note:** No external libraries are required — the chatbot uses only built-in Python modules.

## Trivia File Format

Your `trivia_questions.txt` file should contain questions in the following format (one per line):

```
Category|Question?|A. Option, B. Option, C. Option, D. Option|CorrectOptionLetter
```

**Example:**

```
Science|What is the chemical symbol for water?|A. H2O, B. CO2, C. O2, D. NaCl|A
History|Who was the first President of the United States?|A. Lincoln, B. Jefferson, C. Washington, D. Adams|C
```

## Implementation Details

* The chatbot uses Python's `random`, `time`, and file I/O to load and handle questions.
* Each question is parsed and validated during load to avoid errors.
* The score is calculated as a percentage, even if the user quits mid-game.

## Future Improvements

* GUI Version using Streamlit for a modern interface.
* Timer per question with bonus points for speed.
* Persistent high score tracking using file/database.
* Add difficulty levels or mixed-category rounds.

## Credits

* Inspired by classic rule-based chatbot techniques.
* Special thanks to the open-source and AI education community.