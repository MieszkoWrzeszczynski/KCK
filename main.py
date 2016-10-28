#!/usr/bin/python3

import ply.lex as lex
import ply.yacc as yacc
import replacePolish

tokens = (
    'CMD',
    'DIRECTION',
    'OTHER'
    )

t_CMD = r'idź'
t_DIRECTION = r'(lewo|prawo|góra|dół)'

t_OTHER = r'\w+'

t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
'''
def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    'expression : expression DIRECTION '
    if

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

yacc.yacc()
'''
"""
while True:
    try:
        s = input('> ')
    except EOFError:
        break
    yacc.parse(s)
"""

# Test it out
data = '''
idź lewo prawo prawostronny idź lewostronny tak
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)