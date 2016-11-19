import arcade
from Student import Student
from Lecturer import Lecturer
from Parser import Parser
from Physics import Physics
from rivescript import RiveScript


class App(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, title="Egzaminator")
        self.background_list = None
        self.lecturer = None
        self.table_list = None
        self.score = 0
        self.physics_engine = None
        self.parser = Parser()
        self.bot = RiveScript()
        self.bot.load_directory("./bot_resources")
        self.bot.sort_replies()
        self.MOVEMENT_SPEED = 15
        self.SPRITE_SCALING = 1

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.lecturer = Lecturer(120,250,"images/lecturer.png", self.SPRITE_SCALING)
        self.students = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.table_list = arcade.SpriteList()
        self.items = arcade.SpriteList()
        self.drawBackground()
        map = self.get_map()
        self.drawMap(map)
        self.physics_engine = Physics(self.lecturer,self.items)

    def botAnswer(self,input):
        reply = self.bot.reply("localuser", input)
        print('Student: ', reply)

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
        position_y = 32;

        for line in map:
            for table in line:
                if(table):
                    table = arcade.Sprite("images/table.png",self.SPRITE_SCALING )
                    table.width = 32;
                    table.height = 32;
                    table.center_x = position_x
                    table.center_y = position_y
                    self.items.append(table)

                    student = Student(position_x,position_y + 32, "images/student.png", self.SPRITE_SCALING,32)
                    student.width = 32;
                    student.height = 28;
                    student.center_x = position_x 
                    student.center_y = position_y + 32
                    self.items.append(student)
                    self.students.append(student)

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
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
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
            studentCollison = self.physics_engine.getCollided()

        if(studentCollison):
            print("Zderzyłem się ze studentem!")


    def animate(self, dt):
        """ Movement and game logic """
        input = self.parser.get()
        if(input["command"] == "move"):
            self.moveNSteps(input["steps"],input["direction"])
        elif((input["command"] == "ask") and (self.physics_engine.getCollided())):
            print(input["natural_input"])
            print(self.botAnswer(input["natural_input"]))

    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.UP:
            self.lecturer.change_y = self.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.lecturer.change_y = -self.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.lecturer.change_x = -self.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
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