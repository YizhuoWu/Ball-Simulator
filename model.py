import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special    import Special

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
balls = set()
object_name = ''


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, balls
    running = False
    cycle_count = 0
    balls = set()


#start running the simulation
def start ():
    
    global running
    running = True

#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    
    global cycle_count, running
    
    if running == True:

        update_all()
        display_all()
        stop() 
    
    if running == False:
        
        start()
        update_all()
        display_all()
        stop() 

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    
    global object_name
    object_name = kind

#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global object_name,balls
    
    if object_name == 'Remove':
        
        for ball in list(balls):

            if ball.contains((x,y)) == True:
                remove(ball)
    elif object_name == '':
        pass
    else:        
            
        new_object = eval(str(object_name+"({x},{y})".format(x=x,y=y)))

        add(new_object)
    

#add simulton s to the simulation
def add(s):
    global balls
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global balls
    balls.remove(s)

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    new_set = set()
    global balls
    for ball in balls:
        if p(ball) == True:
            new_set.add(ball)
    
    return new_set

#call update for every simulton in the simulation
def update_all():
    global balls,cycle_count
    if running == True:
        cycle_count += 1
        for ball in list(balls):
            ball.update()


#delete each simulton in the simulation from the canvas; then call display for each
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    global balls
    
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)    
    
    canvas = controller.the_canvas

    for ball in balls:
        ball.display(canvas)
        
    controller.the_progress.config(text=str(cycle_count)+" cycles/"+str(len(balls))+" simultons")
 
