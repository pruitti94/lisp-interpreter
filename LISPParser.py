import ply.yacc as yacc
from LISPLexer import tokens

def p_lispStart_1(p):
  'lispStart : lisp SEMI'
  p[0] = p[1]

def p_lispStart_2(p):
  'lispStart : bool SEMI'
  p[0] = p[1]
  
def p_lispStart_3(p):
  'lispStart : list SEMI'
  p[0] = p[1]

def p_bool_1(p):
  'bool : TRUE'
  p[0] = ['bool',p[1]]
  
def p_bool_2(p):
  'bool : FALSE'
  p[0] = ['bool',p[1]]

def p_list_1(p):
  'list : LPARENT lisp list RPARENT'
  p[0] = ['list', p[2], p[3]]

def p_lisp_1(p):
  'lisp : NUMBER'
  p[0] = ['num',p[1]]
  
#Adds two elements together
def p_lisp_2(p):
  'lisp : LPARENT PLUS lisp lisp RPARENT'
  p[0] = ['+',p[3],p[4]]

#Subtracts the second element from the first element
def p_lisp_3(p):
  'lisp : LPARENT MINUS lisp lisp RPARENT'
  p[0] = ['-',p[3],p[4]]

#Multiplies two elements
def p_lisp_4(p):
  'lisp : LPARENT TIMES lisp lisp RPARENT'
  p[0] = ['*',p[3],p[4]]

#Divides the first element by the second element
def p_lisp_5(p):
  'lisp : LPARENT DIV lisp lisp RPARENT'
  p[0] = ['/',p[3],p[4]]

def p_error(p):
  print("Syntax error in input!")

parser = yacc.yacc()

