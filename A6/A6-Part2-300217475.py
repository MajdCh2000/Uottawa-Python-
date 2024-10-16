# Course: IT1 1120
# Assignment number: 6
# Chantiri, Majd
# Student number: 300217475

class Rectangle:
    "Class that represents a rectangle in the place"
    def __init__(self,x,y,w,h):
        '''
        (x coord, y coord, width, height) -> None
        Initializes the rectangle to (x coord, y coord, width, height)
        Precondition: ALL ENTERED Height and Width VALUES MUST BE POSITIVE
        '''
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        if h <0 or w <0:
            raise ValueError()
            

    def height(self):
        '''representing the rectangles height'''
        return self.h

    def width(self):
        '''representing the rectangles width'''
        return self.w
    
    def x(self):
        '''representing the rectangles x coordinates'''
        return self.x

    def y(self):
        '''representing the rectangles y coordinates'''
        return self.y

    def __str__(self):
        '''Full string represention of the rectangles'''
        return('Rectangle[x=' + str(self.x) + ',y=' + str(self.y) + ',width='+ str(self.w) + ',height=' + str(self.h)+']')
        
    def contains(self,x,y):
        '''return true if the the given coordinates
        are inside the bounds of the rectange'''
        if not (x > self.x and x < (self.w + abs(self.x))):
            return False
        if not (y < self.y and y < (self.h + abs(self.y))):
            return False
        else:
            return True

    def intersects(self,rect):
        '''Returns true if 2 rectangles intersects and false otherwise.'''
        if ((self.x > (rect.w + rect.x)) or (rect.x > (self.w + self.x))):
            return False
        elif ((self.y > (rect.h + rect.y)) or (rect.y > (self.h + self.y))):
            return False
        else:
            return True

    def __eq__(self, rect):
        '''return true if both rectangles have same attributes and false otherwise'''
        return self.x == rect.x and self.y == rect.y and self.w == rect.w and self.h == rect.h
