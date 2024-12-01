import random
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
    
# Mapping of inputs to choices
userInputDict = {"r": 1, "p": 2, "s": 3, "l": 4, "k": 5}  # Rock, Paper, Scissors, Lizard, Spock
reverseDict = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}

# File for storing player data
USER_DATA_FILE = 'user_data.json'

# Game Settings (OOP Class-based structure)
class Game:
    def __init__(self, player_name, opponent_name=None):
        self.player_name = player_name
        self.opponent_name = opponent_name
        self.player_wins = 0
        self.opponent_wins = 0
        self.rounds_played = 0
        self.user_choices = []
        self.ai_choices = []
        self.history = []

    def record_choice(self, user_choice, ai_choice):
        """Store the choices in history for both player and AI."""
        self.user_choices.append(user_choice)
        self.ai_choices.append(ai_choice)
        self.history.append((user_choice, ai_choice))

    def display_stats(self):
        """Display basic statistics of the game."""
        print(f"\nGame Statistics for {self.player_name}:")
        print(f"Total Wins: {self.player_wins}, Total Losses: {self.opponent_wins}")
        print(f"Rounds Played: {self.rounds_played}")
        print(f"Player's Most Common Choice: {self.most_common_choice(self.user_choices)}")
        print(f"AI's Most Common Choice: {self.most_common_choice(self.ai_choices)}")
        self.plot_choices()

    def most_common_choice(self, choices):
        """Return the most common choice made by the player/AI."""
        return max(set(choices), key=choices.count) if choices else "None"

    def plot_choices(self):
        """Plot the most common choices of both player and AI."""
        labels = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        player_counts = [self.user_choices.count(i) for i in range(1, 6)]
        ai_counts = [self.ai_choices.count(i) for i in range(1, 6)]

        plt.figure(figsize=(10, 5))
        plt.bar(labels, player_counts, alpha=0.5, label="Player Choices", color='b')
        plt.bar(labels, ai_counts, alpha=0.5, label="AI Choices", color='r')
        plt.title("Player vs AI Choice Distribution")
        plt.xlabel("Choices")
        plt.ylabel("Count")
        plt.legend()
        plt.show()

    def save_game_results(self):
        """Save game results to an Excel file for analysis."""
        df = pd.DataFrame(self.history, columns=["Player Choice", "AI Choice"])
        df.to_excel(f"{self.player_name}_game_results.xlsx", index=False)
        print(f"\nGame results saved as {self.player_name}_game_results.xlsx")

    def play_game(self, mode="single-player", difficulty="easy"):
        """Main game loop."""
        while self.rounds_played < 5:
            self.rounds_played += 1
            print(f"\n--- Round {self.rounds_played} ---")
            user_choice = input(f"{self.player_name}, choose (r for Rock, p for Paper, s for Scissors, l for Lizard, k for Spock): ").lower()
            if user_choice not in userInputDict:
                print("Invalid input! Please choose 'r', 'p', 's', 'l', or 'k'.")
                continue
            user_choice_num = userInputDict[user_choice]
            self.user_choices.append(user_choice_num)

            # AI makes its choice based on difficulty
            ai_choice_num = self.choose_ai_move(difficulty)
            self.ai_choices.append(ai_choice_num)

            print(f"{self.player_name} chose {reverseDict[user_choice_num]}, AI chose {reverseDict[ai_choice_num]}")

            result = self.determine_winner(user_choice_num, ai_choice_num)
            if result == "player":
                print(f"{self.player_name} wins this round!")
                self.player_wins += 1
            elif result == "ai":
                print(f"AI wins this round!")
                self.opponent_wins += 1
            else:
                print("It's a draw!")

            # Check if a player has won 3 out of 5
            if self.player_wins >= 3:
                print(f"\n{self.player_name} wins the game!")
                break
            elif self.opponent_wins >= 3:
                print(f"\nAI wins the game!")
                break

        self.display_stats()
        self.save_game_results()

    def choose_ai_move(self, difficulty):
        """AI's move based on difficulty."""
        if difficulty == "easy":
            return random.choice([1, 2, 3, 4, 5])
        elif difficulty == "medium":
            return self.predict_user_move()
        elif difficulty == "hard":
            return self.predict_user_move_with_learning()
        return random.choice([1, 2, 3, 4, 5])

    def predict_user_move(self):
        """AI predicts the next move based on the user's history."""
        if len(self.user_choices) < 2:
            return random.choice([1, 2, 3, 4, 5])
        last_move = self.user_choices[-1]
        return (last_move % 5) + 1  # Basic prediction

    def predict_user_move_with_learning(self):
        """AI uses learning to predict the user's move based on patterns."""
        if len(self.user_choices) < 3:
            return random.choice([1, 2, 3, 4, 5])
        user_last_moves = self.user_choices[-3:]
        ai_last_moves = self.ai_choices[-3:]

        # Machine learning model could be added here (just statistical for simplicity)
        most_common_user_move = self.most_common_choice(user_last_moves)
        return (most_common_user_move % 5) + 1      
    def determine_winner(self, player_choice, ai_choice):
        """Determine the winner between player and AI."""
        rules = {
            (1, 3): "player", (3, 1): "ai",  # Rock > Scissors
            (3, 2): "player", (2, 3): "ai",  # Scissors > Paper
            (2, 1): "player", (1, 2): "ai",  # Paper > Rock
            (1, 4): "player", (4, 1): "ai",  # Rock > Lizard
            (4, 5): "player", (5, 4): "ai",  # Lizard > Spock
            (5, 3): "player", (3, 5): "ai",  # Spock > Scissors
            (3, 4): "player", (4, 3): "ai",  # Scissors > Lizard
            (4, 2): "player", (2, 4): "ai",  # Lizard > Paper
            (2, 5): "player", (5, 2): "ai",  # Paper > Spock
        }
        if player_choice == ai_choice:
            return "draw"
        return rules.get((player_choice, ai_choice), "ai")

# User Authentication Functions
def load_user_data():
    """Load user data from a JSON file."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_user_data(user_data):
    """Save user data to a JSON file."""
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file)

def login_or_register():
    """Allow the user to login or register."""
    user_data = load_user_data()

    username = input("Enter your username: ").lower()

    if username in user_data:
        print(f"Welcome back, {username}!")
    else:
        print(f"Hello, {username}! Let's get you registered.")
        user_data[username] = {
            "total_wins": 0,
            "total_losses": 0,
            "game_history": []
        }
        save_user_data(user_data)

    return username, user_data

def main():
    # Login or Register User
    username, user_data = login_or_register()

    # Choose mode and play the game
    mode = input("\nChoose mode (single-player or multiplayer): ").lower()
    difficulty = "easy"  # Default difficulty

    if mode == "single-player":
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        game = Game(username)
        game.play_game(mode="single-player", difficulty=difficulty)

    elif mode == "multiplayer":
        opponent_name = input("Enter opponent's name: ")
        game = Game(username, opponent_name)
        game.play_game(mode="multiplayer")

    else:
        print("Invalid mode! Please choose 'singleplayer' or 'multiplayer'.")

if __name__ == "__main__":
    main()


