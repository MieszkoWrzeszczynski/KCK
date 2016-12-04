# -*- coding: utf-8 -*-

import arcade
import random
from random import randint

from Student import Student
from Lecturer import Lecturer
from Parser import Parser
from Physics import Physics


class App(arcade.Window):

    def __init__(self, width, height):
        
        super().__init__(width, height, title="Egzaminator")
        self.background_list = None
        self.lecturer = None
        self.table_list = None
        self.score = 0
        self.physics_engine = None
        self.parser = Parser()
        self.MOVEMENT_SPEED = 15
        self.SPRITE_SCALING = 1
        self.students_name = None

    def setup(self):

        """ Set up the game and initialize the variables. """
        self.lecturer = Lecturer(120,250,"images/lecturer.png", self.SPRITE_SCALING)
        self.students = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.table_list = arcade.SpriteList()
        self.items = arcade.SpriteList()
        self.students_name = ["Jan","Stanisław","Andrzej","Józef","Tadeusz","Jerzy","Zbigniew","Krzysztof","Henryk","Ryszard","Kazimierz","Marek","Marian","Piotr","Janusz"]
        self.drawBackground()
        self.map = self.get_map()
        self.drawMap(self.map)
        self.physics_engine = Physics(self.lecturer,self.items)
        

    def get_map(self):

        map_file = open("maps/map.csv")
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

        for line in self.map:
            for table in line:
                if(table):
                    student = Student(position_x,position_y + 32,
                    "images/student.png", self.SPRITE_SCALING,randint(100,200),random.choice(self.students_name))
                    student.width = 32;
                    student.height = 28;
                    id = Student.id;
                    student.center_x = position_x 
                    student.center_y = position_y + 32
                    self.items.append(student)
                    self.students.append(student)

                    table = arcade.Sprite("images/table.png",self.SPRITE_SCALING )
                    table.width = 32;
                    table.height = 32;
                    table.center_x = position_x
                    table.center_y = position_y
                    table.id = Student.id;
                    self.items.append(table)

                position_x += 62
            position_y += 62
            position_x = 0

    def drawBackground(self):

        position_x = 0;
        position_y = 0;
        
        for x in range(11):
            for y in range(11):
                background_sprite = arcade.Sprite("images/background.png", self.SPRITE_SCALING)
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
            collided = self.physics_engine.getCollided()

        if(collided["collision"]):
            print("Zderzyłem się ze studentem nr: " + str(collided["student_id"]))

    def animate(self, dt):

        input = self.parser.get()
       
        if(input["command"] == "move"):
            self.moveNSteps(input["steps"],input["direction"])
        elif(input["command"] == "ask"):
            physics = self.physics_engine.getCollided()
            if(physics["collision"]):
                print(self.students[physics["student_id"]].answer(input["natural_input"]))

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
    window.setup()
    arcade.run()

main()