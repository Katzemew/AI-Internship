# Tic Tac Toe AI Game (Unbeatable Mode)

Welcome to the **Tic Tac Toe AI Game** — a Python-powered, Pygame-based graphical game where you play against an intelligent AI opponent. The game is built with feature of Minimax decision-making algorithm and an interactive interface.

## How to Play

1. Clone or download this repository to your local machine.

2. Make sure you have Python 3.x installed.

3. Navigate to the project directory.

4. Run the game using the command:

   ```bash
   python ttt.py
   ```

5. Choose a grid cell with your mouse to place your symbol (`X`).

6. Watch the AI respond with its move.

7. First to align three symbols in a row (horizontally, vertically, or diagonally) wins.

8. A message appears if there's a win or a tie.

## Features

* **AI Opponent**: Implements the Minimax algorithm to create an unbeatable opponent.
* **Game Modes**: Optionally extendable for PvP or AI difficulty levels.
* **Win Detection**: Handles all winning conditions and tie games.
* **Graphical Interface**: Clean and user-friendly game board using Pygame.
* **Replay Logic**: Easily restart by re-running the program.
* **AI Evaluation Feedback**: Console prints show how AI selects its moves and why.

## Game Functions

The game supports keyboard shortcuts for toggling modes and changing difficulty:

**Key**   	**Function Description**

* **G**  --   Toggle Game Mode between Player vs Player (PvP) and Player vs AI
* **0**	 --   Set AI difficulty to Level 0 – AI plays random moves
* **1**	 --   Set AI difficulty to Level 1 – AI uses the Minimax algorithm
* **R**	 --   Reset the current game and start a new one

These shortcuts make it easy to test different AI strategies and enjoy competitive or casual gameplay.


## Requirements

* Python 3.x
* `pygame` module

### Install Requirements

Run this in your terminal:

```bash
pip install pygame
```

## Project Structure

```bash
├── ttt.py              # Main game file with AI logic
├── constants.py        # File for all visual and game constants
├── README.md           # This file
```

## Implementation Details

* Uses NumPy arrays to manage the board state.
* Minimax recursively evaluates all possible game outcomes.
* The AI is designed to always block the player or win if a path exists.
* Game board redrawing and event handling are done using Pygame.
* Added difficulty levels (Random, Minimax with depth limit, Perfect AI).

## Future Improvements

* Add score tracking across multiple rounds.
* Add background music or sound effects.
* GUI elements like reset button or difficulty selector.
* Celebration animations for win/tie.

## Credits

* Developed following [this tutorial](https://youtu.be/Bk9hlNZc6sE?si=22YPbqjNNZr_Aedv) by @Coding Spot.
* Built using Python and Pygame.
* Special thanks to the open-source game dev community.

