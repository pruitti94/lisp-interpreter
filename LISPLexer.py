import ply.lex as lex

reserved = { 'if': 'IF', 'and': 'AND', 'or': 'OR', 'car': 'CAR', 'cdr': 'CDR', 'cons': 'CONS', 'true': 'TRUE', 'false': 'FALSE' }

tokens = ['LPARENT','RPARENT','SEMI','CAR','CDR','CONS','GREATER','GREATEREQUAL','LESS','LESSEQUAL','NOTEQUAL','EQUAL','PLUS','MINUS','TIMES','DIV','NUMBER'] + \
  list(reserved.values())

t_TRUE = r'[tT][rR][uU][eE]'
t_FALSE = r'[fF][aA][lL][sS][eE]'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_SEMI = r';'
t_CAR = r'[cC][aA][rR]'
t_CDR = r'[cC][dD][rR]'
t_CONS = r'[cC][oO][nN][sS]'
t_IF = r'[iI][fF]'
t_AND = r'[aA][nN][dD]'
t_OR = r'[oO][rR]'
t_GREATER = r'\>'
t_GREATEREQUAL =r'\>='
t_LESS = r'\<'
t_LESSEQUAL = r'\<='
t_NOTEQUAL = r'\<\>'
t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'

def t_NUMBER(t):
  r'[-+]?[0-9]+(\.([0-9]+)?)?'
  t.value = float(t.value)
  t.type = 'NUMBER'
  return t

# Ignored characters
t_ignore = " \r\n\t\s"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  #t.lexer.skip(1)
  raise Exception('LEXER ERROR')

lexer = lex.lex()
## Test it out
data = '''
(if (>= 2 3) 40 50)
'''
#
## Give the lexer some input
print("Tokenizing: ",data)
lexer.input(data)

## Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
