from dataclasses import dataclass
from typing import Union

@dataclass
class RGB:
    r: float
    g: float
    b: float
    
    def __setattr__(self, attr, val):
        if type(val) == int:
            val = min(val, 255)
            val = val / 255.0
        
        self.__dict__[attr] = val

@dataclass
class Vector:
    x: int = 0
    y: int = 0
    
    def __getitem__(self, key):
        if type(key) != int:
            raise ValueError(f'Expected int, got {type(key)}')
        
        if key == 0: return self.x
        elif key == 1: return self.y
        else: 
            raise IndexError(key)

    def __add__(self, v: 'Vector'):
        if type(v) != Vector:
            raise TypeError('Argument v must be of type "Vector"')
        
        self.x += v.x
        self.y += v.x
        
    def __sub__(self, v):
        if type(v) != Vector:
            raise TypeError('Argument v must be of type "Vector"')
        
        self.x -= v.x
        self.y -= v.y
        
    def __mul__(self, v: Union[int, 'Vector']):
        if type(v) == int:
            self.x *= v
            self.y *= v
            
        elif type(v) == Vector:
            self.x *= v.x
            self.y *= v.y
            
    def slice(self) -> slice:
        """Get a slice object from the vector's x and y values

        :return: Slice object
        :rtype: slice
        """        
        
        return slice(self.x, self.y)