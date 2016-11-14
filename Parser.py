import ply.lex as lex
import ply.yacc as yacc
import re
import arcade


ASK = 5


class Parser():

    def get(self):
        pl_words = {
            'lewo': arcade.key.LEFT,
            'lewą': arcade.key.LEFT,
            'góra': arcade.key.UP,
            'górę': arcade.key.UP,
            'prawo':arcade.key.RIGHT,
            'prawą':arcade.key.RIGHT,
            'dół': arcade.key.DOWN,
            'ASK' : ASK
        }

        #lexer
        tokens = (
            'GO',
            'DIRECTION',
            'NO',
            'NUMBER',
            'ASK'
        )

        t_GO = r'i[sś][cć]|(id(z|ź)|przesu(n|ń) si(ę|e)|p(ó|o)jd(z|ź)|przejd(ź|z)|podejd(z|ź|)|biegnij|pobiegnij)'
        t_DIRECTION = r'(lew(o|ą)|praw(ą|o)|gór(a|ę)|dół)'
        t_NO = 'nie'
        t_ASK = r'(ściąga)|(sciaga)'

        def t_NUMBER(t):
            r'\d+'
            t.value = int(t.value)
            return t

        def t_error(t):
            t.lexer.skip(1)

        lexer = lex.lex()

        def p_expression_ask(p):
            'expression : ASK '
            print("Rozpoznałem pytanie")
            p[0] = 'ASK'

        def p_expression_move(p):
            'expression : GO DIRECTION '
            print('Ide w',p[2])
            p[0] = p[2]

        def p_expression_nmove(p):
            'expression : NO GO DIRECTION'
            print('Nigdzie nie ide!')

        def p_expression_moves(p):
            'expression : GO NUMBER DIRECTION'
            print('Ide ' + str(p[2]) + " razy w " + p[3])
            p[0] = (p[2],p[3])

        def p_error(p):
            print("Nie rozumiem!")

        yacc.yacc()

        cur_direct = ""
        s  = input(">")
        cur_direct = yacc.parse(s)
        if type(cur_direct) is tuple:
            if(cur_direct[1] in pl_words):
                print(pl_words[cur_direct[1]]  , cur_direct[0] )
                return  (pl_words[cur_direct[1]]  , cur_direct[0] )

        if(cur_direct in pl_words):
            return(pl_words[cur_direct])