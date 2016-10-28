#!/usr/bin/python3

import ply.lex as lex
import ply.yacc as yacc
import replacePolish

#lexer
tokens = (
    'CMD',
    'DIRECTION',
#    'OTHER'
    )

t_CMD = r'idź'
t_DIRECTION = r'(lewo|prawo|góra|dół)'

#t_OTHER = r'\w+'
t_ignore = " \t"

def t_error(t):
#    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#parser
def p_expression_move(p):
    'expression : CMD DIRECTION '
    print('Ide')

def p_error(p):
    print("Nie rozumiem!")

yacc.yacc()

while True: # pętla główna
    #try:
    s  = input('> ')
   # except EOFError:
    #    break
    yacc.parse(s)
