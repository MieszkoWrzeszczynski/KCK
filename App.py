# -*- coding: utf-8 -*-

import arcade
import random
from random import randint

from Student import Student
from Lecturer import Lecturer
from Parser import Parser
from Physics import Physics
from ProgramBot import ProgramBot

class App(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height, title="Egzaminator")
        self.background_list = None
        self.lecturer = None
        self.students_amount = 11
        self.score = 0
        self.physics_engine = None
        self.program_bot = ProgramBot()
        self.parser = Parser()
        self.MOVEMENT_SPEED = 15
        self.SPRITE_SCALING = 1
        self.resourcesSetup(11)
        self.wilhelm = arcade.sound.load_sound("app_resources/sounds/wilhelm.ogg")
        self.setup()
        print("Wpisz coś aby uruchomić program")


    def resourcesSetup(self,amount_of_files):

        names     =  open("app_resources/students_informations/names").readline().split(" ")
        surnames  =  open("app_resources/students_informations/surnames").readline().split(" ")
        attitudes =  open("app_resources/students_informations/attitude").readline().split(" ")
        prompt    = []

        template = """
        // Bot variables

        ! var name = {0}
        ! var surname = {1}
        ! var attitude = {2}
        ! var prompt = {3}
        ! var cheat = {4}
        """

        for i in range(amount_of_files):
            with open('app_resources/bot_resources/bot_'+ str(i), 'w') as the_file:
                the_file.write(template.format(
                    random.choice(names),
                    random.choice(surnames),
                    random.choice(attitudes),
                    random.choice([True,False]),
                    random.choice([True,False])
                ))

    def setup(self):
        self.lecturer = Lecturer(120,250,"app_resources/images/lecturer.png", self.SPRITE_SCALING)
        self.background_list = arcade.SpriteList()
        self.items = arcade.SpriteList()
        self.drawBackground()
        self.map = self.get_map()
        self.drawMap(self.map)
        self.physics_engine = Physics(self.lecturer,self.items)

    def get_map(self):
        map_file = open("app_resources/maps/map" + str(randint(0,3)) + ".csv")
        map_array = []
        for line in map_file:
            line = line.strip()
            map_row = line.split(",")
            for index, item in enumerate(map_row):
                map_row[index] = int(item)
            map_array.append(map_row)
        return map_array

    def drawMap(self,map):

        position_x = 0;
        position_y = 15;
        student_number = 0

        for line in self.map:
            for table in line:
                if(table):
                    student = Student(
                        position_x,
                        position_y + 32,
                        "app_resources/images/student.png",
                         self.SPRITE_SCALING,
                        "bot_" + str(student_number)
                    )
                    student.width = 32;
                    student.height = 61;
                    id = Student.id;
                    student.center_x = position_x
                    student.center_y = position_y + 32
                    self.items.append(student)

                position_x += 62

            position_y += 55
            position_x = 0
            student_number += 1

    def drawBackground(self):

        position_x = 0;
        position_y = 0;

        for x in range(11):
            for y in range(11):
                background_sprite = arcade.Sprite("app_resources/images/background.png", self.SPRITE_SCALING)
                background_sprite.width = 62;
                background_sprite.height = 62;
                background_sprite.center_x = position_x
                background_sprite.center_y = position_y
                self.background_list.append(background_sprite)
                position_x += 62

            position_y += 62
            position_x = 0

    def on_draw(self):
        arcade.start_render()

        self.background_list.draw()
        self.items.draw()
        self.lecturer.draw()

        self.on_key_release(65361, 0)
        self.on_key_release(65362, 0)

        # Put the text on the screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


    def moveNSteps(self,steps,direct):

        for i in range(steps):
            self.on_key_press(direct,0)
            self.physics_engine.update()
            self.on_draw()
            student = self.physics_engine.getCollided()

        if(student["collision"]):
            print("Zderzyłem się ze studentem o imieniu " + student["student_id"].getName())

    def animate(self,dt):

        user_input = self.parser.get()

        if(user_input["command"] == "move"):
            self.program_bot.answer("run")
            self.moveNSteps(user_input["steps"],user_input["direction"])
        elif(user_input["command"] == "kick"):
            student = self.physics_engine.getCollided()
            arcade.sound.play_sound(self.wilhelm)
            if(student["student_id"].cheat == True):
                self.score += 1
            student["student_id"].kill()
        elif(user_input["command"] == "bot"):
            if(self.physics_engine.getCollided()["student_id"] != None):
                student = self.physics_engine.getCollided();
                student["student_id"].answer(user_input["natural_input"])
            else:
                self.program_bot.answer(user_input["natural_input"])

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP and self.lecturer.center_y < 590:
            self.lecturer.change_y = self.MOVEMENT_SPEED
        elif key == arcade.key.DOWN and self.lecturer.center_y > 30:
            self.lecturer.change_y = -self.MOVEMENT_SPEED
        elif key == arcade.key.LEFT and self.lecturer.center_x > 30:
            self.lecturer.change_x = -self.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT and self.lecturer.center_x < 590:
            self.lecturer.change_x = self.MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.lecturer.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.lecturer.change_x = 0

def main():
    window = App(620,620)
    arcade.run()


main()