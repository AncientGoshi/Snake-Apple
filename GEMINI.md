# Project Overview

This project is a classic Snake game implemented in Python using the `pygame` library. The player controls a snake that moves around the screen, eating apples to grow longer. The game ends if the snake hits the walls or its own tail. The high score is saved and displayed.

# Building and Running

To run the game, follow these steps:

1.  **Activate the virtual environment:**
    ```shell
    source ./.venv/bin/activate
    ```

2.  **Run the game:**
    ```shell
    python3 execute_functions.py
    ```

# Development Conventions

*   The code is written in Python.
*   The `pygame` library is used for graphics and event handling.
*   The high score is stored in a JSON file named `high-score.json`.
*   The main game logic is separated into `snake.py` and `execute_functions.py`.
*   The `json_helpers.py` file contains functions for reading and writing the high score to the JSON file.

# Key Files

*   `execute_functions.py`: The main entry point of the game. It initializes `pygame`, handles user input, and manages the game loop.
*   `snake.py`: Contains the `Snake` class, which defines the snake's behavior, including movement, growth, and collision detection.
*   `json_helpers.py`: Provides helper functions for reading and writing the high score to `high-score.json`.
*   `high-score.json`: Stores the player's high score.
*   `JetBrainsMono-Regular.ttf`: The font used for displaying the score and game-over message.
*   `README.md`: Contains basic instructions on how to run the game.
