import tkinter as tk
import threading
import time
import math

buttons_state=[False,]*4
led_state=[False,True,False,False]
pot_state=0

close_root=False
root_closed=False

disc_position=0

class Disc:
    def __init__(self,root,x,y,diametry):
        self.r=diametry/2
        self.canvas = tk.Canvas(root,width=diametry, height=diametry)
        self.canvas.place(x=x-self.r,y=y-self.r)
        self.ring=self.canvas.create_oval(2,2,self.r*2, self.r*2,fill="black") 
        self.line=self.canvas.create_line(0, 0, 1, 1, fill='white',width=3)
        
    def draw(self,marker_position):  
        r=self.r           
        angle=(2*math.pi/48)*marker_position
        x=math.cos(angle)*r+r
        y=math.sin(angle)*r+r
        self.canvas.coords(self.line,r,r,x,y)  
        
class Detector:
    def __init__(self,root,x,y,diametry):
        r=diametry/2
        self.canvas = tk.Canvas(root,width=diametry, height=diametry)
        self.canvas.place(x=x-r+1,y=y-r+1)
        self.ring=self.canvas.create_oval(2,2,r*2, r*2) 

    def draw(self,state):      
        color = 'cyan' if state else 'gray'
        self.canvas.itemconfig(self.ring,fill=color)    
        
class Leds:
    def __init__(self,root,x,y,diametry):
        self.ldes=[Detector(root,x=x,y=y+i*40,diametry=diametry) for i in range(4)]

    def draw(self,state):  
        for l,s in zip(self.ldes,reversed(state)):
            l.draw(s)
        

def thread():
    global disc_position,buttons_state,pot_state,root_closed
    
    root = tk.Tk()
    root.title("Servo Simulator for MTM")
    root.geometry('360x250')
    root.attributes("-topmost", True)

    #controls
    disc=Disc(root,x=200,y=110,diametry=180)
    detector=Detector(root,x=200,y=210,diametry=20)
    leds=Leds(root,x=60,y=40,diametry=20)     
    pot = tk.Scale(root, from_=0, to=1000, orient=tk.VERTICAL,length=200)
    pot.place(x=300,y=10)

    buttons=[]    
    for i in range(4):     
        b = tk.Button(root, text=str(i))
        b.place(x=10,y=160-(20+i*40)+10)
        buttons.append(b)
    
    # periodic
    try:
        while(not close_root):
            
            for i in range(4):buttons_state[i] = (buttons[i].cget( "state" )=='active')
            pot_state=pot.get()
            leds.draw(led_state)
            disc.draw(disc_position)
            detector.draw(disc_position==12)
            
            root.update()
            time.sleep(0.01)
    except:
        root_closed=True
        return
    
    root.destroy()
    raise Exception('window closed')

def wrapper(func):
    def new_func(*original_args, **original_kwargs):
        if root_closed: raise Exception('window closed')
        res=func(*original_args, **original_kwargs)
        time.sleep(0.05)
        return res
    return new_func

#----- API -------

prev_led_state=[False,]*4
@wrapper
def led(state):
    _led(state)
    
def _led(state):
    global prev_led_state,disc_position
    
    #update leds
    for i in range(4): led_state[i] = ((state & (1<<i)) != 0)
    #- update ring
    if sum(led_state)==1 and sum(prev_led_state)==1: #only one led True
        if prev_led_state[(led_state.index(True)+1)%4]==True:
            disc_position=(disc_position-1)%48
        elif prev_led_state[(led_state.index(True)-1)%4]==True:
            disc_position=(disc_position+1)%48
    prev_led_state=list(led_state)
            
@wrapper
def but(): return sum(int(buttons_state[i])<<i for i in range(4))

@wrapper
def det(): return disc_position==12

@wrapper
def pot(): return pot_state

@wrapper
def set_port(state):
   new_state=0 
   led_pos=(13,5,9,17)
   for i,lp in enumerate(led_pos):
      bit=(state>>lp)&1
      new_state|=bit<<i
    
   _led(new_state)

@wrapper   
def get_port():
    state = 0
    state |= pot_state
    state |= (disc_position==12)<<30
    
    but_state=sum(int(buttons_state[i])<<i for i in range(4))
    but_pos=(18,12,15,20)
    for i,bp in enumerate(but_pos):
      bit=(but_state>>i)&1
      state|=bit<<bp
    
    return state
    

def open():
    global close_root
    close_root=False
    t = threading.Thread(target=thread)
    t.start()
    
def close():
    global close_root
    close_root=True
    

    