# Rock, Paper, Scissors, Lizard, Spock Game

Welcome to the **Rock, Paper, Scissors, Lizard, Spock** game! This game allows you to play against an AI or with a friend in multiplayer mode. Choose from five moves: Rock, Paper, Scissors, Lizard, and Spock. The game also includes features like tracking stats, analyzing game history, and visualizing data!

## Features

- **Single-Player Mode**: Play against AI with three difficulty levels: Easy, Medium, and Hard.
- **Multiplayer Mode**: Play against a friend.
- **User Data Storage**: Track your wins, losses, and game history.
- **Game Analytics**: View statistics and plot choice distributions using **matplotlib**.
- **AI Difficulty**: AI can predict your moves based on history and learning.
- **Save Results**: Save your game results to an Excel file for later analysis.

## Requirements

To run this game, you'll need the following Python libraries:
- `random`
- `json`
- `os`
- `pandas`
- `matplotlib`

You can install the required libraries using pip:

`pip install pandas matplotlib`
## How to Play
**Login/Register**: Enter your username to either log in or register. The system will store your game data for later.

Choose Mode:
**Single-Player**: Play against the AI. Choose a difficulty level (easy, medium, or hard).
**Multiplayer**: Play against a friend by entering their username.

**Choose Your Move**: Enter your choice using the following keys:
r for Rock
p for Paper
s for Scissors
l for Lizard
k for Spock

**Game Flow**: The game will proceed in rounds. The first player to win 3 rounds wins the game.

# Features Explained
**Login/Register**: When you run the game, you will be asked to log in or register with your username. The system keeps track of your total wins, losses, and game history.

**Game Modes**
Single-Player: Choose from three difficulty levels:
Easy: The AI picks a random move.
Medium: The AI predicts your next move based on your previous choice.
Hard: The AI uses learning algorithms to predict your moves more accurately.
Multiplayer: Challenge a friend to play by entering their name, and take turns making your moves.

**Game Analytics**
Player vs AI Stats: After the game ends, the system will display:
Total wins and losses.
Player's most common choice.
AI's most common choice.
Plot Choices: A bar chart will be generated showing the distribution of moves for both the player and the AI.
Saving Game Results
Your game results will be saved to an Excel file (<player_name>_game_results.xlsx) for analysis and future reference.

## Sample Game Flow
```bash
Enter your username: player1
Hello, player1! Lets get you registered.

Choose mode (single-player or multiplayer): single-player
Choose difficulty (easy, medium, hard): easy

--- Round 1 ---
player1, choose (r for Rock, p for Paper, s for Scissors, l for Lizard, k for Spock): r
player1 chose Rock, AI chose Paper
AI wins this round!

--- Round 2 ---
player1, choose (r for Rock, p for Paper, s for Scissors, l for Lizard, k for Spock): s
player1 chose Scissors, AI chose Scissors
Its a draw!

--- Round 3 ---
player1, choose (r for Rock, p for Paper, s for Scissors, l for Lizard, k for Spock): p
player1 chose Paper, AI chose Rock
player1 wins this round!

Game Statistics for player1:
Total Wins: 1, Total Losses: 1
Rounds Played: 3
Players Most Common Choice: Scissors
AIs Most Common Choice: Paper

Game results saved as player1_game_results.xlsx
```
## **Contributing**
Feel free to fork the repository and create a pull request if you have any improvements or features you'd like to add!

License
This project is licensed under the MIT License - see the LICENSE file for details.

---
