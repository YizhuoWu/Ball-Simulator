#The special class is a greedy Hunter, and I used a pig.png to represent it.
#It moves like a Hunter, but without changing its size and 
#it is kind of 'blind' since the distance they could detect is much closer than a Hunter.
#When Spcial finds a target(Prey), and the distance is valid(distance < 90), it will accelerate
#and eat the closest target. After eating that target, if there is no more target, the speed backs 
#to its normal speed.

from PIL.ImageTk import PhotoImage
from prey import Prey
from blackhole import Black_Hole        
from pulsator import Pulsator
from hunter import Hunter
from mobilesimulton import Mobile_Simulton
from math import atan2
import model

class Special(Hunter):
    
    valid_distance = 90
    
    def __init__(self,x,y):
        
        Hunter.__init__(self,x,y)
        self._image = PhotoImage(file = 'pig.png')
    
    def update(self):
        
        target_set = model.find(lambda x: isinstance(x,Prey))
        
        
        eaten_set = model.find(lambda x:self.contains(x) and isinstance(x,Prey))
        for ball in eaten_set:
            model.remove(ball)

        alist = [(i,i.distance(self.get_location())) for i in target_set if i.distance(self.get_location()) < Special.valid_distance]
        alist = sorted(alist,key = lambda x: x[1])
        
        if alist == []:
            self.set_speed(5)
            pass
        
        else:
            close_one = alist[0][0]
            
            y_differ = close_one.get_location()[1] - self.get_location()[1]
            x_differ = close_one.get_location()[0] - self.get_location()[0]
            
            new_angle = atan2(y_differ,x_differ)
            self.set_angle(new_angle)
            self.set_speed(40)
        
        self.move()    
    
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image = self._image)
