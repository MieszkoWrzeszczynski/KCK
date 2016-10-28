#!/usr/bin/python3

import ply.lex as lex
import ply.yacc as yacc
import replacePolish

#lexer
tokens = (
    'CMD',
    'DIRECTION',
    'NO'
#    'OTHER'
    )

t_CMD = 'idź'
t_DIRECTION = r'(lewo|prawo|góra|dół)'
t_NO = 'nie'

#t_OTHER = r'\w+'
t_ignore = " \t"

def t_error(t):
#    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#parser
def p_expression_move(p):
    'expression : CMD DIRECTION '
    print('Ide w',p[2])

def p_expression_nmove(p):
    'expression : NO CMD DIRECTION'
    print('Nigdzie nie ide!')

def p_error(p):
    print("Nie rozumiem!")

yacc.yacc()

# pętla główna
while True:
    s  = input('> ')
    yacc.parse(s)
