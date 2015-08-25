#!/usr/local/bin/python3
# NAME: Richard Tzeng
# FILE: shape.py
# DATE: <21014-07-18 Fri>
# DESC: This defines the Shape Class. There is a method that can move the 
# circle to a different position. From The Quick Python Book (p. 30)

class Shape:
    """Shape Class: has method move(), location(), and __init__()"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY

    def location(self):
        """Returns a tuple containing the ~x,y~ coordinates of an object"""
        self.here = (self.x, self.y)        
        return self.here
