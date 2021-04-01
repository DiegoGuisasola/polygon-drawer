import turtle
import time

class Polygon:
    def __init__(self, side, name='non-set', linecolor='black', linewidth=1, stepsize=100, speed=3):
        try:
            if side < 3:
                self.side = -1
                raise ValueError
            else:
                self.side = side
        except:
            print('ValueError: The amount of sides must be greater than 2')
            
        
        
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

        if self.side == -1: # Handles error: self.side < 3
            return
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
    def __init__(self, radius = 50, linecolor='black', linewidth=1, stepsize=5, speed='fastest'):
        super().__init__(1, 'circle', linecolor, linewidth,stepsize,speed)
        self.radius = radius
    
    def draw(self):
        t = turtle.Turtle()
        t.circle(self.radius)


def draw_example():
    p1 = Triangle('red')
    p1.draw()

    p2 = Square('red')
    p2.draw()

    p3 = Circle(linecolor='red')
    p3.draw()

if __name__ == '__main__':
    draw_example()