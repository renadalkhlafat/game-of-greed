class Banker :
    """
    Name:
    Banker

    Description:
    A class used to handle the points in the Game of Greed Game

    Methods:

    shelf (instance method):
    Input to shelf is the amount of points (integer) to add to shelf.



    bank(instance method): 
    Add any points on the shelf to total and reset shelf to 0


    clear_shelf(instance method):
    Reset shelf to 0
    """
    def __init__(self) :
        self.shelved =0
        self.balance=0

    def shelf(self ,points:int):
        self.shelved += points
        return self.shelved


    def clear_shelf(self):
        self.shelved =0

    def bank(self):
        self.balance += self.shelved 
        self.clear_shelf()

        return self.balance

    