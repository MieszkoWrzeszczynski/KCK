import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
    'CMD',
    'DIR'
  )

# Regular expression rules for simple tokens
t_CMD = r"id[zź]"
t_DIR = r"gora"

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
data = "3idz gora"
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.value," ", tok.type)