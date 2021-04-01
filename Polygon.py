import turtle
import time

class Polygon:
    def __init__(self, side, name, linecolor='black', linewidth=1, stepsize=100, speed=3):
        self.side = side
        self.name = name
        self.angle = (self.side-2)*180/self.side
        self.linecolor = linecolor
        self.linewidth = linewidth
        self.color = linecolor
        self.stepsize = stepsize
        self.speed = speed

    def get_name(self):
        return self.name

    def draw(self):
    # Initialize everything
        # turtle.color(self.color)
        turtle.getscreen()
        t = turtle.Turtle()
        t.width(self.linewidth)
        t.pencolor(self.linecolor)
        t.speed(self.speed)

        for i in range(self.side):
            t.forward(self.stepsize)
            t.left(180-self.angle)
        
        time.sleep(1)

        t.clear()


        

class Triangle(Polygon):
    def __init__(self, linecolor='black', linewidth=1):
        super().__init__(3,'triangle', linecolor, linewidth)

class Square(Polygon):
    def __init__(self, linecolor='black', linewidth=1):
        super().__init__(4,'square', linecolor, linewidth)

class Pentagon(Polygon):
    def __init__(self, linecolor='black', linewidth=1):
        super().__init__(5,'pentagon', linecolor, linewidth)

class Circle(Polygon):
    def __init__(self, linecolor='black', linewidth=1, stepsize=5, speed='fastest'):
        super().__init__(100,'circle', linecolor, linewidth,stepsize,speed)


p1 = Triangle()
p1.draw()

p2 = Square()
p2.draw()

p3 = Circle('red')
p3.draw()
