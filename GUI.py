import arcade
import re
import lex
import yacc 

SPRITE_SCALING = 1
SCREEN_WIDTH = 620
SCREEN_HEIGHT = 620
MOVEMENT_SPEED = 15


class Input():
    def get(self):
        pl_words = {
            'lewo': 1,
            'lewą': 1,
            'góra': 2,
            'górę': 2,
            'prawo':3,
            'prawą':3,
            'dół': 4
        }

        #lexer
        tokens = (
            'GO',
            'DIRECTION',
            'NO',
            'NUMBER'
            )

        t_GO = r'(id(z|ź)|przesu(n|ń) si(ę|e)|p(ó|o)jd(z|ź)|przejd(ź|z)|podejd(z|ź|)|biegnij|pobiegnij)'
        t_DIRECTION = r'(lew(o|ą)|praw(ą|o)|gór(a|ę)|dół)'
        t_NO = 'nie'

        def t_NUMBER(t):
            r'\d+'
            t.value = int(t.value)
            return t

        def t_error(t):
            t.lexer.skip(1)

        lexer = lex.lex()

        def p_expression_move(p):
            'expression : GO DIRECTION '
            print('Ide w',p[2])
            p[0] = p[2]

        def p_expression_nmove(p):
            'expression : NO GO DIRECTION'
            print('Nigdzie nie ide!')

        def p_expression_moves(p):
            'expression : GO NUMBER DIRECTION'
            print('Ide ' + str(p[2]) + " razy w " + p[3])
            p[0] = (p[2],p[3])

        def p_error(p):
            print("Nie rozumiem!")

        yacc.yacc()

        cur_direct = ""
        s  = input()
        cur_direct = yacc.parse(s)

        if(cur_direct in pl_words):
            return(pl_words[cur_direct])

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
        self.input = Input()

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.left_down = False
        self.lecturer = Lecturer(120,250,"images/lecturer.png", 1)
        self.background_list = arcade.SpriteList()
        self.table_list = arcade.SpriteList()
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

        key = self.input.get()

        if(key == 1):
           self.on_key_press(65361,0)
           #n steps on left
           # self.physics_engine.update()
           # self.on_draw()
           # self.on_key_press(65361,0)
           # self.physics_engine.update()
           # self.on_draw()
           # self.on_key_press(65361,0)
           # self.physics_engine.update()
           # self.on_draw()
           # self.on_key_press(65361,0)
           # self.physics_engine.update()
           # self.on_draw()
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