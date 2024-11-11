import random
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

#Mapping Input To Choices    
userInputDict = {"r":1,"p":2,"s":3,"l":4,"k":5}
reverseDict = {1:"Rock", 2:"Paper", 3:"Scissor", 4:"lizard", 5:"Spock"}

#Game Settings 
class Game :
    def __init__(self, userName):
        self.userName = userName
        self.userWins = 0 
        self.opponentWins = 0
        self.roundsPlayed = 0
        self.userChoices = []
        self.aiChoices = []
        self.history = []

    #Store Choices of user
    def recordChoices(self, userChoices, aiChoices):
        self.userChoices.append(userChoices)
        self.aiChoices.append(aiChoices)
        self.history.append((userChoices,aiChoices))
        
    #Calculate Most Common Choices
    def mostCommonChoices(self,choices):
        return max(set(choices), key = choices.count) if choices else "None"
    
    #Display Basic Staistics of the Game
    def displayStats(self):
        print(f"\nGame Statistics for {self.userName}")
        print(f"Total wins: {self.userWins}")
        print(f"Rounds Played: {self.roundsPlayed}")
        print(f"Palyer's Most Common Choice : {self.mostCommonChoices(self.userChoices)}")
        print(f"AI Most Common Choice : {self.mostCommonChoices(self.aiChoices)}")
        
        