from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
class Game:

    """
    Description:
    This class repreasent the core of Game Of Greed which
    

    Methods: 
    - play: Starts a new game with multiple options, such as enter, quit and bank which are depending on the user choice.
    
    """

    def __init__(self,round_num=0):
        self.round_num=round_num
        self.banker=Banker()

    def play(self,roller):
        """
        Description: Starts a new game with multiple options, such as enter, quit and bank which are depending on the user choice.

        Args:
            roller (Type: function): function to mock rolling of dice
        """
        new_game=GameLogic()
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        wanna_play=input("> ").lower()
        self.round_num+=1
        if wanna_play=="n" or wanna_play=="no":
            print("OK. Maybe another time")

        else:
            print(f"Starting round {self.round_num}")
            print(f"Rolling {new_game.dice_num} dice...")

            a=roller(new_game.dice_num)
            b= str(a).replace(",","").replace("[","").replace("]","")

            earned_points=new_game.calculate_score(a)
        
            print(f"*** {b} ***")
            print("Enter dice to keep, or (q)uit:")
            keep_q=input("> ").lower()

            if keep_q=="q" or keep_q=="quit":
                print(f"Thanks for playing. You earned {self.banker.balance} points")

            else:
                keep_points_tuple = [int(i) for i in keep_q]
                earned_points=tuple(keep_points_tuple)
                dices_left=(new_game.dice_num)-len(earned_points)
                shelfed_points=self.banker.shelf(new_game.calculate_score(earned_points))
                print(f"You have {shelfed_points} unbanked points and {dices_left} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
            while True:
                roll_again=input("> ").lower()
                    
                if roll_again=="q" or roll_again=="quit":
                    print(f"Thanks for playing. You earned {self.banker.balance} points")
                    break

                elif roll_again=="b" or roll_again=="bank":
                    
                    print(f"You banked {self.banker.shelved} points in round {self.round_num}")
                    self.banker.bank()
                    print(f"Total score is {self.banker.balance} points")
                    self.round_num+=1
                print(f"Starting round {self.round_num}")
                print(f"Rolling {new_game.dice_num} dice...")
                a=roller(new_game.dice_num)
                b= str(a).replace(",","").replace("[","").replace("]","")

                earned_points=new_game.calculate_score(a)
        
                print(f"*** {b} ***")
                print("Enter dice to keep, or (q)uit:")
                keep_q=input("> ").lower()
                if keep_q=="q" or keep_q=="quit":
                    print(f"Thanks for playing. You earned {self.banker.balance} points")

                else:
                    keep_points_tuple = [int(i) for i in keep_q]
                    earned_points=tuple(keep_points_tuple)
                    dices_left=(new_game.dice_num)-len(earned_points)
                    shelfed_points=self.banker.shelf(new_game.calculate_score(earned_points))
                    print(f"You have {shelfed_points} unbanked points and {dices_left} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                   
                
            
            
            
            
        
                


            

        
