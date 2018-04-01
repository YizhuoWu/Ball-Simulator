# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5
    width = 5
    height = 5
    angle = 0
    speed = 5
    color = 'blue'
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,Ball.angle,Ball.speed)
        self.color = Ball.color
        self.randomize_angle()

    def update(self):
        self.move()

    def display(self,the_canvas):
        
        the_canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill=self.color)