import arcade
import re


SPRITE_SCALING = 1
SCREEN_WIDTH = 620
SCREEN_HEIGHT = 620
MOVEMENT_SPEED = 15


class Input():
    
    def __init__(self):
        self.input = None 

    def normalize(self):
        result = re.findall(r'\w+', self.input)
        result = list(map(lambda x: x.lower(), result))
        print(result)
        return  self.checkWords(result)

    def checkWords(self,list_of_words):
        for word in list_of_words:
            if(word   == "lewo"):
                return 1
            elif(word == "góra"):
                return 2
            elif(word == "prawo"):
                return 3
            elif(word == "dół"):
                return 4

    def getInput(self):
        self.input = input()
        return self.normalize()

class Lecturer(arcade.Sprite):

    def __init__(self,x,y, filename, sprite_scaling):
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)
        self.center_x = x
        self.center_y = y

class Gui(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, title="Egzaminator")
        self.background_list = None
        self.lecturer = None
        self.table_list = None
        self.score = 0
        self.physics_engine = None
        self.input = None 

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.left_down = False
        self.lecturer = Lecturer(120,250,"images/lecturer.png", 1)
        self.background_list = arcade.SpriteList()
        self.table_list = arcade.SpriteList()
        self.input = Input()
        map = self.get_map()

        self.drawBackground()
        self.drawMap(map)
        self.physics_engine = arcade.PhysicsEngineSimple(self.lecturer,self.table_list)

    def get_map(self):
        map_file = open("map.csv")
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
                    table = arcade.Sprite("images/table.png", 1)
                    table.width = 32;
                    table.height = 32;
                    table.center_x = position_x
                    table.center_y = position_y
                    self.table_list.append(table)
                position_x += 62
            position_y += 62
            position_x = 0

    def drawBackground(self):
        position_x = 0;
        position_y = 0;
        
        for x in range(11):
            for y in range(11):
                background_sprite = arcade.Sprite("images/background.png", 1)
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
        self.table_list.draw()
        self.lecturer.draw()

        self.on_key_release(65361, 0)
        self.on_key_release(65362, 0)

        # Put the text on the screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def ifCollided(self):
        self.hit_list = \
            arcade.check_for_collision_with_list(self.lecturer,self.table_list)

        if(len(self.hit_list) > 0):
            return True

    def animate(self, dt):
        """ Movement and game logic """

        key = self.input.getInput()

        if(key == 1):
           self.on_key_press(65361,0)
        elif(key == 2):
           self.on_key_press(65362,0)
        elif(key == 3):
           self.on_key_press(65363,0)
        elif(key == 4):
           self.on_key_press(65364,0)

        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.lecturer.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.lecturer.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.lecturer.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.lecturer.change_x = MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.lecturer.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.lecturer.change_x = 0

def main():
    window = Gui(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

main()