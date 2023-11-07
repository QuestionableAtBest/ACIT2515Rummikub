colors = ["red","blue","yellow","black","joker"]
numbers = ["1","2","3","4","5","6","7","8","9","10","11","12","13","*"]

class Tile:
    def __init__(self, color, number):
        if color not in colors or number not in numbers:
            raise ValueError("Invalid color")
        else:
            self.color = color
            self.number = number
    
    def __str__(self):
        return f"{self.color} {self.number}"
    
    def sameNumber(self,other):
        return self.number == other.number

    def sameColor(self,other):
        return self.color == other.color
    
    