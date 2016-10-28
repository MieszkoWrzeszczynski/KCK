#!/usr/bin/python3

import ply.lex as lex
import ply.yacc as yacc

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

#parser
def p_expression_move(p):
    'expression : GO DIRECTION '
    print('Ide w',p[2])

def p_expression_nmove(p):
    'expression : NO GO DIRECTION'
    print('Nigdzie nie ide!')

def p_expression_moves(p):
    'expression : GO NUMBER DIRECTION'
    print('Ide ' + str(p[2]) + " razy w " + p[3])

def p_error(p):
    print("Nie rozumiem!")

yacc.yacc()

# pętla główna
while True:
    s  = input('> ')
    yacc.parse(s.lower())