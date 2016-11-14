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
    'DIRECTION',
    'NO',
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



data = "idź w prawo"
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.value," ", tok.type)


