# Hunter is derived from Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator,Mobile_Simulton):
    
    valid_distance = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,self._width,self._height,0,5)
        self.randomize_angle()

    
    def update(self):
        self.counter+=1
        target_set = model.find(lambda x: isinstance(x,Prey))        

        alist = [(i,i.distance(self.get_location())) for i in target_set if i.distance(self.get_location()) < Hunter.valid_distance]
        alist = sorted(alist,key = lambda x: x[1])
        
        if alist == []:
            pass
        else:
            close_one = alist[0][0]
            
            y_differ = close_one.get_location()[1] - self.get_location()[1]
            x_differ = close_one.get_location()[0] - self.get_location()[0]
            
            new_angle = atan2(y_differ,x_differ)
            self.set_angle(new_angle)
        
        
        eaten_set = model.find(lambda x:self.contains(x) and isinstance(x,Prey))
        for ball in eaten_set:
            model.remove(ball)
            
        if len(eaten_set)!=0:
            self.change_dimension(len(eaten_set),len(eaten_set))
            self.counter = 0

        else:

            if self.counter == Pulsator.counter_constant:
                self.change_dimension(-1,-1)
                self.counter = 0
                
            if self.get_dimension() == (0,0):
                model.remove(self)
        
        
        self.move()
                
