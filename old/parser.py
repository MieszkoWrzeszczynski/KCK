#parser
def p_expression_move(p):

   #'expression : GO LEFT'
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
