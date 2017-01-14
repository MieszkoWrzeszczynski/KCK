#-*- coding: utf-8 -*-
import os
import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN


class Parser():
    def __init__(self):
        self.cmd = ""
        self.reply = ""
        self.steps = 0
        self.dir = ""
        self.natural_input = ""

    def loadToken(self,fileName):
        dirPath = os.path.dirname(os.path.realpath(__file__))
        dirPathTokens = os.path.join(dirPath,"app_resources/tokenizing","tokens")

        with open(os.path.join(dirPathTokens, fileName)) as file:
            return '|'.join(file.read().split())

    def get(self):
        #lexer
        tokens = (
            'GO',
            'NUMBER',
            'LEFT',
            'RIGHT',
            'TOP',
            'DOWN',
            'ASK',
            'KICK',
            )

        @TOKEN(self.loadToken("t_GO"))
        def t_GO(t):
            return t

        @TOKEN(self.loadToken("t_RIGHT"))
        def t_RIGHT(t):
            return t

        @TOKEN(self.loadToken("t_LEFT"))
        def t_LEFT(t):
            return t

        @TOKEN(self.loadToken("t_TOP"))
        def t_TOP(t):
            return t

        @TOKEN(self.loadToken("t_DOWN"))
        def t_DOWN(t):
            return t

        def t_NUMBER(t):
            r'\d+'
            t.value = int(t.value)
            return t

        t_ASK = r'[sś]ci[aą]ga'
        t_KICK = r'wyrzucam|wyrzucić'


        def t_error(t):
            t.lexer.skip(1)

        lexer = lex.lex()

        def p_move(p):
            '''expression  : GO direction
                    | GO num direction
                    | GO direction num'''

            self.cmd="move"
            if len(p) is 3:
                self.steps = 1
                self.reply = "Idę"
            else:
                #self.reply = "Idę " + str(self.steps) + " razy w " + self.reply
                self.reply = "Już idę!"
            p[0] = {
                "command" : "move",
                "direction" : self.dir,
                "steps" : self.steps,
                "reply": self.reply,
                "natural_input": self.natural_input
            }

        def p_num(p):
            'num : NUMBER'
            self.steps = p[1]

        def p_direction(p):
            '''direction : left
                        | right
                        | top
                        | down'''

        def p_left(p):
            'left : LEFT'
            self.reply = "lewo"
            self.dir = 65361 #arcade.key.LEFT

        def p_right(p):
            'right : RIGHT'
            self.dir = 65363 #arcade.key.RIGHT

        def p_top(p):
            'top : TOP'
            self.dir = 65362 #arcade.key.UP

        def p_down(p):
            'down : DOWN'
            self.dir = 65364 #arcade.key.DOWN

        def p_expression_ask(p):
            'expression  : ASK '
            p[0] = { "command" : "bot","natural_input": self.natural_input}

        def p_expression_kick(p):
            'expression  : KICK'
            p[0] = { "command" : "kick","natural_input": self.natural_input}

        def p_error(p):
            '''there's must be sth. Otherwise, it returns none'''

        yacc.yacc()

        self.natural_input = input('User: ').lower()
        if (yacc.parse(self.natural_input) is None):
            return { "command" : "bot","natural_input": self.natural_input}
        else:
            return yacc.parse(self.natural_input)
