#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN

class Parser():

    def loadToken(fileName):
        dirPath = os.path.dirname(os.path.realpath(__file__))
        dirPathTokens = os.path.join(dirPath,"tokenizing","tokens")

        with open(os.path.join(dirPathTokens, fileName)) as file:
            return '|'.join(file.read().split())

    #lexer
    tokens = (
        'GO',
        'NUMBER',
        'LEFT',
        'RIGHT',
        'TOP',
        'DOWN',
        'ASK'
        )

    @TOKEN(loadToken("t_GO"))
    def t_GO(t):
        return t

    @TOKEN(loadToken("t_RIGHT"))
    def t_RIGHT(t):
        return t

    @TOKEN(loadToken("t_LEFT"))
    def t_LEFT(t):
        return t

    @TOKEN(loadToken("t_TOP"))
    def t_TOP(t):
        return t

    @TOKEN(loadToken("t_DOWN"))
    def t_DOWN(t):
        return t

    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    t_ASK = r'[sś]ci[aą]ga'

    def t_error(t):
        t.lexer.skip(1)

    lexer = lex.lex()

    def p_move(p):
        '''expression  : GO direction
                | GO num direction
                | GO direction num'''
        global reply, cmd
        cmd="move"
        #print("p_move")
        if len(p) is 3:
            global steps
            steps=1
            reply = "Idę w " + reply
        else:
            reply = "Idę " + str(steps) + " razy w " + reply
        p[0] = ("move",dir,steps, reply)

    def p_num(p):
        'num : NUMBER'
        #print("p_num")
        global steps
        steps=p[1]

    def p_direction(p):
        '''direction : left
                    | right
                    | top
                    | down'''
        #print("p_direction()")

    def p_left(p):
        'left : LEFT'
        global dir, reply
        reply="lewo"
        dir="left"
        #print("Idę w lewo")

    def p_right(p):
        'right : RIGHT'
        global dir
        dir = "right"
        #print("Idę w prawo")

    def p_top(p):
        'top : TOP'
        global dir
        dir = "top"
        #print("Idę do góry")

    def p_down(p):
        'down : DOWN'
        global dir
        dir = "down"
        #print("Idę na dół")

    def p_expression_ask(p):
        'expression  : ASK '
        print("Rozpoznałem pytanie")
        p[0] = 'ASK'

    def p_error(p):
        print("Nie rozumiem!")



    yacc.yacc()

    def get(self):
        s = input('> ').lower()
        return yacc.parse(s)

obj = Parser()
print(obj.get())

'''
obj = Parser()
while True:
    s = input('> ').lower()
    if s == "q": break
    print(obj.get(s))
'''
'''
data = "idź lewy"
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.value," ", tok.type)
'''

