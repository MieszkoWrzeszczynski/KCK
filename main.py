#!/usr/bin/python3

import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN

#lexer
tokens = (
    'GO',
    'DIRECTION',
    'NO',
    'NUMBER',
    )

t_GO = r'\b(i[sś][cć]|id[zź]|przesu[nń]|p[oó]jd[zź]|przejd[źz]|podejd[zź]|biegnij|pobiegnij|piegnij)\b'


data = "lewo prawo gora dol dół dołem left right top down"
data = data.split() #make data a list of keywords

@TOKEN('|'.join(data))
def t_DIRECTION(t):
    return t


#t_DIRECTION = r'\b(lew[oą]|praw[ąo]|g[oó]r([ąa]|[eę])|d[óo][lł])\b'
#t_UNKNOWN = r'\w'
t_NO = 'nie'
#t_ignore = r' [woz] | do | na | si[eę]'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()


#parser
def p_expression_move(p):
   'expression : GO DIRECTION'
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

'''
# pętla główna
while True:
    s = input('> ')
    yacc.parse(s.lower())

'''

data = "idz 3 razy w prawo lewo lewą top down"
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.value," ", tok.type)


