# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions

from prey import Prey
from blackhole import Black_Hole
import model

class Pulsator(Black_Hole):
    
    counter_constant = 30
    
    def __init__(self,x,y):
        
        Black_Hole.__init__(self,x,y)
        
        self.counter = 0
    
    def update(self):
        
        self.counter+=1
        
        eaten_set = Black_Hole.update(self)
        
        if len(eaten_set)!=0:
            self.change_dimension(len(eaten_set),len(eaten_set))
            self.counter = 0

        else:

            if self.counter == Pulsator.counter_constant:
                self.change_dimension(-1,-1)
                self.counter = 0
                
            if self.get_dimension() == (0,0):
                model.remove(self)
        
            
        return eaten_set
        
    