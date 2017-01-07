import arcade
import re
import ast

from rivescript import RiveScript
from app_resources.assets import polishDel


class Student(arcade.Sprite):
    id = 0

    def __init__(self,x,y,filename,sprite_scaling,bot_resources_variable):

        super().__init__(filename, sprite_scaling)
        Student.id =  Student.id + 1
        self.center_x = x
        self.center_y = y
        self.brain = RiveScript(utf8=True)
        self.brain.unicode_punctuation = re.compile(r'[.,!?;*]')
        self.brain.load_file("app_resources/bot_resources/student.rive")
        self.brain.load_file("app_resources/bot_resources/" + bot_resources_variable)
        self.brain.sort_replies()
        self.id = Student.id
        self.config = self.loadConfig(bot_resources_variable)
        self.name = self.getName()
        self.surname = self.getSurname()
        self.cheat = self.checkCheatStatus()

    def loadConfig(self,filename):
        config_file = open("app_resources/bot_resources/" + filename,'r')
        file_content = [line.rstrip('\n') for line in config_file]
        return file_content

    def answer(self,input):

        reply = self.brain.reply("localuser", polishDel(input))
        print('Student ' + self.name + ' ' + self.surname + ':',reply)

    def getName(self):
        return self.regexCheck("name")

    def getSurname(self):
        return self.regexCheck("surname")

    def checkCheatStatus(self):
        return ast.literal_eval(self.regexCheck("cheat"))

    def regexCheck(self,to_check):
        regex = re.compile('! var (%s) = (.*)'%to_check)
        for item in self.config:
            if(regex.findall(item)):
                match = regex.findall(item)
                return match[0][1]