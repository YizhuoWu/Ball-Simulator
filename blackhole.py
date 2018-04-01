# Black_Hole is derived from Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    
    radius = 10

    def __init__(self,x,y):
        Simulton.__init__(self,x,y,Black_Hole.radius*2,Black_Hole.radius*2)
    
    def update(self):
        
        eaten_set = model.find(lambda x:self.contains(x) and isinstance(x,Prey))
        for ball in eaten_set:
            model.remove(ball)
        return eaten_set

    
    def display(self,the_canvas):
        
        width = self.get_dimension()[0]
        height = self.get_dimension()[1]
        
        the_canvas.create_oval(self._x-width      , self._y-height,
                                self._x+width, self._y+height,
                                fill='black')

    def contains(self,ball):

        if type(ball) == tuple:
            if self.distance(ball) <= Black_Hole.radius:
                return True
            return False
        else:
            if self.distance(ball.get_location()) <= Black_Hole.radius:
                return True
            return False            