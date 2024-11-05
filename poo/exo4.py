import math

class Angle:
    def __init__(self,angle):
        if angle < 0 or angle > 360:
            raise ValueError
        self.angle = angle
    def __str__(self):
        return str(self.angle) + "degrés"
    def ajoute(self, n):
        return (self.angle + n)%360
    def cos(self):
        return math.cos(self.anlge*(math.pi/180))
    def sin(self):
        return math.cos(self.anlge*(math.pi/180))
