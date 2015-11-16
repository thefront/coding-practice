#!/usr/local/bin/python3
# NAME: Richard Tzeng
# FILE: circle.py
# DATE: <21014-07-20 Mon>
# DESC: This defines the Circle class that subclasses Shape, with is_collision(),
# distance(), and __str__methods. 

import math
from shape import Shape

class Circle(Shape):
    """ Circle class: inherits from Shape inherits move and location and has
        a method for area of the circle"""
    pi = 3.14159
    def __init__(self, x=0, y=0, r=1):
        """Create a Circle with the given radius"""
        Shape.__init__(self, x, y)
        self.radius = r

    def area(self):
        """Circle area method: returns the area of the circle"""
        return self.radius * self.radius * self.pi

    #__str(self)__ is where we can define what we see when we try to print
    # an instance.
    def __str__(self):
        return "Circle of radius %s at coordinates (%d, %d)" % (self.radius,
        self.x, self.y)

    @classmethod
    def is_collision(Circle, c1, c2):
        """determinces if the two circles collide"""
        collision_dist = c1.radius + c2.radius
        if Circle.distance(c1, c2) < collision_dist:
            return 'True'

    @classmethod
    def distance(self, c1, c2):
        """calculates distance between two circles"""
        # assign coordinates to variables
        c1_x,c1_y = c1.location()        
        c2_x,c2_y = c2.location()        
        # determince if x,y positions are negative or not
        # for x distance
        if c1_x == c2_x:
            a = 0
        elif c1_x < c2_x:
            a = c2_x - c1_x
        else:
            a = c1_x - c2_x
        # for y distance 
        if c1_y == c2_y:
            b = 0
        elif c1_y < c2_y:
            b = c2_y - c1_y
        else:
            b = c1_y - c2_y

        # using Pythagorean theorem, find the distance
        return math.sqrt((a * a) + (b * b))

def main():
    # run some tests here.
    """Testing ~Circle~ class for is_collision(), location(), __str__()"""
    i2 = 0
    c1 = Circle(-10, 0, 8)
    c2 = Circle(10, 0, 8)
    # Do 20 tests that move the two circles long the x-axis.
    for i in range(20):
        print('--')
        print('Circle 1: ', c1)
        print('Circle 2: ', c2)
        print("Collision? ", Circle.is_collision(c1,c2))
        if 0 < i2 < 5:
            i2 -= i
        else:
            i2 += i
        c1.move(i, 0)
        c2.move(i2, 0)

# detect running interactively
if __name__ == '__main__':
    main() 

