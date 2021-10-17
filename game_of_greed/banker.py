class Banker :
    """
    
    """
    def __init__(self) :
        self.shelved =0
        self.balance=0

    def shelf(self ,points:int):
        self.shelved += points


    def clear_shelf(self):
        self.shelved =0

    def bank(self):
        self.balance += self.shelved 
        self.clear_shelf()

        return self.balance

    