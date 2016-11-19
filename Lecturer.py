import arcade

class Lecturer(arcade.Sprite):

    def __init__(self,x,y, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.center_x = x
        self.center_y = y