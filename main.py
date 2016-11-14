#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN


def loadToken(fileName):
    dirPath = os.path.dirname(os.path.realpath(__file__))
    dirPathTokens = dirPath + "\\tokenizing\\tokens\\"
    with open(dirPathTokens + fileName) as file:
        return '|'.join(file.read().split())



#lexer
tokens = (
    'GO',
    'NUMBER',
    'LEFT',
    'RIGHT',
    'TOP',
    'DOWN'
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

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

def p_move(p):
    'move : GO direction'
    print("p_move()")

def p_direction(p):
    '''direction : left
                | right
                | top
                | down
                '''
    print("p_direction()")


def p_left(p):
    'left : LEFT'
    print("lewo")

def p_right(p):
    'right : RIGHT'
    print("prawo")

def p_top(p):
    'top : TOP'
    print("góra")

def p_down(p):
    'down : DOWN'
    print("dół")


def p_error(p):
    print("Nie rozumiem!")

yacc.yacc()


# pętla główna
while True:
    s = input('> ').lower()
    if s == "q": break
    yacc.parse(s)










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

