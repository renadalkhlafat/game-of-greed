from game_of_greed.game_logic import GameLogic
# from game_logic import GameLogic

from game_of_greed.banker import Banker
# from banker import Banker


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
        self.roller = None
        self.new_game = GameLogic()
        self.dices_left = 6
        self.end_flag = False

    def play(self,roller = GameLogic.roll_dice):
        """
        Description: Starts a new game with multiple options, such as enter, quit and bank which are depending on the user choice.

        Args:
            roller (Type: function): function to mock rolling of dice
        """
        self.roller = roller

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        wanna_play=input("> ").replace(" ","")
        self.round_num+=1
        if wanna_play=="n" or wanna_play=="no":
            print("OK. Maybe another time")

        else:
            print(f"Starting round {self.round_num}")
            self.play_again()


    def bank(self):
        """
        Description: This function is responsible for banking shefing the points and gives a summary of the recorded points and the end of each round

        Args:
            None
        """
        print(f"You banked {self.banker.shelved} points in round {self.round_num}")
        self.banker.bank()
        print(f"Total score is {self.banker.balance} points")
        self.dices_left = 6
        self.round_num+=1
        if self.round_num <= 20 or self.banker.balance >= 10000:
            print(f"Starting round {self.round_num}")
            self.play_again()
        else:
            print(f"Thanks for playing. You earned {self.banker.balance} points")
            quit()

    def end_round(self):
        """
        Description: This function is responible for checking the user input, if its not contain any recorded points it will end the round and starts a new one

        Args:
            None
        """
        print(f"You banked 0 points in round {self.round_num}")
        print(f"Total score is {self.banker.balance} points")
        self.banker.clear_shelf()
        self.round_num += 1
        self.dices_left = 6
        print(f"Starting round {self.round_num}")
        self.end_flag = True


    def play_again(self):
        """
        Description: This function is responible for ustomizing the user input by removing the useless spacess, aslo, its calling the calcualte function to calculate the actual recorded points

        Args:
            None
        """
        if self.round_num >= 20 or self.banker.balance >= 10000:
            print(f"Thanks for playing. You earned {self.banker.balance} points")
            quit()

        if self.end_flag == True or self.dices_left == 0:
            self.dices_left = 6
            self.end_flag = False

        print(f"Rolling {self.dices_left} dice...")
        a=self.roller(self.dices_left)
        b= str(a).replace(",","").replace("[","").replace("]","")

        earned_points=self.new_game.calculate_score(a)
        keep_q2 = ''
        flag = True
        while flag:
            print(f"*** {b} ***")
            if self.zlich(tuple(a)):
                flag = False
                self.end_round()
                self.play_again()
            print("Enter dice to keep, or (q)uit:")
            keep_q2=input("> ").replace(" ","")
            if keep_q2=="q" or keep_q2=="quit":
                print(f"Thanks for playing. You earned {self.banker.balance} points")
                quit()
            elif self.detect_type_or_cheater(keep_q2,a): # if true, print cheater else continue to the rest of code
                print("Cheater!!! Or possibly made a typo...")
            else:
                flag = False
                keep_points_tuple = [int(i) for i in keep_q2]
                earned_points=tuple(keep_points_tuple)

                self.dices_left=(self.dices_left)-len(earned_points)
                
                shelfed_points=self.banker.shelf(self.new_game.calculate_score(earned_points))
                print(f"You have {shelfed_points} unbanked points and {self.dices_left} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                
                while True:
                    roll_again = input("> ").replace(" ","")
                        
                    if roll_again=="q" or roll_again=="quit":
                        print(f"Thanks for playing. You earned {self.banker.balance} points")
                        break

                    elif roll_again=="b" or roll_again=="bank":
                        self.bank()
                        

                    if(roll_again == "r" or roll_again == "roll"):
                        self.play_again()


    @staticmethod
    def detect_type_or_cheater(input,rolled_dice):
        """
        Description: This function is responible for dedtcting if the user wanted to cheat or entered a  typo

        Args:
            Input: Tuple
            Rolled_dice:Tuple
        """

        _rolled_dice = list(rolled_dice)

        _input = [int(i) for i in input]

        if len(_input)>len(_rolled_dice):
            return True
        
        for i in _input:
            if i in _rolled_dice:
                _rolled_dice.remove(i)
            else:
                return True
        return False

    def zlich(self,dice):
        """
        Description: This function is responible for game over statment which ocuurs if the user did not have any recorded points

        Args:
            Dice: Tuple
        """
        score = GameLogic.calculate_score(dice)
        if score==0:
            zilch_string = """****************************************
**        Zilch!!! Round over         **
****************************************"""
            print(zilch_string)
            return True
        else:
            return False


            
# if __name__ == '__main__':
#     game = Game()
#     game.play()   
        
                


            

        
