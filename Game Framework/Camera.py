import math

class Camera:

    def __init__(self, x , y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shake_intensity = 0.0

    
    def shake_camera(self, shake_intensity):

        self.shake_intensity = shake_intensity

        if(self.shake_intensity > 0.01):
            self.shake_intensity =  self.shake_intensity * 0.9
        
        self.x += math.cos(self.shake_intensity) * 2 
        self.y += math.sin(self.shake_intensity) * 2