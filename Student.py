import arcade
import re

from rivescript import RiveScript
from polDel import polishDel


class Student(arcade.Sprite):
    id = 0

    def __init__(self,x,y, filename, sprite_scaling,points,name):

        super().__init__(filename, sprite_scaling)
        self.center_x = x
        self.center_y = y
        self.exam_points = points
        self.brain = RiveScript(utf8=True)
        self.brain.unicode_punctuation = re.compile(r'[.,!?;*]')
        self.brain.load_directory("./bot_resources")
        self.brain.sort_replies()
        Student.id =  Student.id + 1
        self.id = Student.id 
        self.name = name

    def answer(self,input):

        reply = self.brain.reply("localuser", polishDel(input))
        print('Student ' + self.name + ':', reply)