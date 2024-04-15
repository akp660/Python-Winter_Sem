
from abc import ABC, abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def noofsides(self):
        pass

class Square(Polygon):
    def noofsides(self):
        print("I am a square, I have 4 equal sides.")

s = Square()
s.noofsides()
