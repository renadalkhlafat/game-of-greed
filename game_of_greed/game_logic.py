import random
from collections import Counter
from typing import List
Scores={
    "Straight":1500,
    "Three Pairs" :	1500,

    (1,1):100,
    (1,2):200,
    (1,3):1000,
    (1,4):2000,
    (1,5):3000,
    (1,6):4000,

    (2,3):200,
    (2,4):400,
    (2,5):600,
    (2,6):800,

    (3,3):300,
    (3,4):600,
    (3,5):900,
    (3,6):1200,

    (4,3):400,
    (4,4):800,
    (4,5):1200,
    (4,6):1600,

    (5,1):50,
    (5,2):100,
    (5,3):500,
    (5,4):1000,
    (5,5):1500,
    (5,6):2000,

    (6,3):600,
    (6,4):1200,
    (6,5):1800,
    (6,6):2400

}
class GameLogic:
    """
    Name:
    GameLogic

    Description:
    A class used to handle the logic of the Game of Greed Game

    Methods:

    calculate_score(static method):
    Input:  tuple of integers that represent a dice roll
    Output: integer representing the roll’s score according to rules of the game 

    roll_dice(static method): 
    Input:  Integer ( between 1 and 6)
    Output: tuple with random values between 1 and 6
    """
    
    def __init__(self,dice_num=6):
        self.dice_num=dice_num
    @staticmethod
    def roll_dice(dice_num=6):
        return tuple(random.randint(1,6) for _ in range(0,dice_num))

    @staticmethod
    def calculate_score(dice):
        score = 0
        dices=Counter(dice)
        x = list(dices)
        x.sort()
        if x  == [1,2,3,4,5,6]:
            score +=Scores["Straight"]
        elif list(dices.values()) == [2, 2, 2]:
            score +=Scores["Three Pairs"]
        else:
            for i in dices.items():
                try:
                    score +=Scores[i]
                except:
                    score +=0
        return score 



print(GameLogic.calculate_score((4,3,2,2,5,6)))
print(GameLogic.calculate_score((3,3,2,2,6,6)))
print(GameLogic.calculate_score((4,3,2,1,5,6)))
print(GameLogic.calculate_score((4,4,4,1,1,1)))
print(GameLogic.calculate_score((1, 1, 1, 2, 2, 2)))


