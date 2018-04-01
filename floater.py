# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random
import math


class Floater(Prey):

    angle = 0
    speed = 5 
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,Floater.angle,Floater.speed)
        self._image = PhotoImage(file = 'ufo.gif')
        self.randomize_angle()

    def update(self):
        time = random.random()
        if time <= 0.3:
            new_speed = Floater.speed*(1+random.uniform(-0.5,0.5))
            new_angle = self._angle + random.uniform(-0.5,0.5)
            self.set_speed(new_speed)
            self.set_angle(new_angle)   
            self.move()
        else:
            self.move()
            
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image = self._image)
