from typing import Union, Type
from datatypes import RGB, Vector

import numpy as np

"""Utility tool for creating art programatically
"""

class BaseObject:
    """Base object
    """
    
    def __init__(self, width: int, height: int, pos: Vector = Vector(0, 0), pixels: np.ndarray = np.array([]), update_on_frame: bool = False) -> None:
        """Base object constructor

        :param width: Object's width in pixels
        :type width: int
        :param height: Object's height in pixels
        :type height: int
        :param pixels: Initial bidimensional array of pixels, defaults to []
        :type pixels: np.array, optional
        :param pos: Initial position, defaults to Vector(0, 0)
        :type pos: Vector, optional
        
        """
        
        self.update_on_frame = update_on_frame

        self.width = width
        self.height = height
        if type(pixels) in [list, tuple]:
            pixels = np.array(pixels)
        self.pixels = pixels
        self.pos = pos
    
    def __setattr__(self, attr, val):
        if attr == "pixels": 
            pass
        
        self.__dict__[attr] = val
    
    def __getitem__(self, *args, **kw):
        return self.pixels.__setattr__(*args, **kw)
    
    def set_pixel(self, color: RGB, x: Union[Vector, int], y: int):
        """Change a single pixel's color value. To set a whole area of pixels, use numpy subscripting instead (see :func:`~__main__.BaseObject.__setattr__`).

        :param color: RGB color value
        :type color: RGB
        :param v: x value if x is not Vector, else Vector for the position
        :type v: Union[Vector, int]
        :param y: y value if x isn't vector, else unused
        :type y: int
        
        """
        

        if type(x) == Vector:
            x = x.x
            y = x.y
            
        self.pixels[y][x] = color

    def fill_polygon(self, color: RGB, *args):
        """Create a filled polygon

        :param color: Color to fill it with
        :type color: RGB
        :raises ValueError: None
        
        """
        
        if len(args) == 1:
            if type(args[0]) != list:
                raise ValueError('Positions must be given in ')

class Builtins:
    class Rectangle(BaseObject):
        def __init__(self, width, height, *args, **kwargs):
            self.fill_polygon()
            
        def draw(self, _):
            return 0
    
class Canvas:
    def __init__(self, init_objects = Union[Type[BaseObject], list]):
        self.canvas = np.array(np.array([]))
        
        if type(init_objects) not in [list, tuple]:
            init_objects = [init_objects]
        
        for obj in init_objects:
            self.place_object(obj)
            
        def place_object(self, obj: Type[BaseObject]):
            self.canvas

can = Canvas()