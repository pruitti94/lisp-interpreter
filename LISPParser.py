import ply.yacc as yacc
from LISPLexer import tokens

def p_lispStart(p):
  'lispStart : lisp SEMI'
  p[0] = p[1]

def p_lisp_1(p):
  'lisp : NUMBER'
  p[0] = ['num',p[1]]
  
def p_lisp_2(p):
  'lisp : TRUE'
  p[0] = ['bool',p[1]]
  
def p_lisp_3(p):
  'lisp : FALSE'
  p[0] = ['bool',p[1]]

#Adds two elements together
def p_lisp_4(p):
  'lisp : LPARENT PLUS lisp lisp RPARENT'
  p[0] = ['+',p[3],p[4]]

#Subtracts the second element from the first element
def p_lisp_5(p):
  'lisp : LPARENT MINUS lisp lisp RPARENT'
  p[0] = ['-',p[3],p[4]]

#Multiplies two elements
def p_lisp_6(p):
  'lisp : LPARENT TIMES lisp lisp RPARENT'
  p[0] = ['*',p[3],p[4]]

#Divides the first element by the second element
def p_lisp_7(p):
  'lisp : LPARENT DIV lisp lisp RPARENT'
  p[0] = ['/',p[3],p[4]]

#if statement
def p_lisp_8(p):
  'lisp : LPARENT IF lisp lisp lisp RPARENT'
  p[0] = ['if',p[3],p[4],p[5]]

#and statement
def p_lisp9(p):
  'lisp : LPARENT AND lisp lisp RPARENT'
  p[0] = ['and',p[3],p[4]]

def p_lisp10(p):
  'lisp : LPARENT OR lisp lisp RPARENT'
  p[0] = ['or',p[3],p[4]]

def p_lisp11(p):
  'lisp : LPARENT alist lisp RPARENT'
  p[0] = ['list',p[2],p[3]]

deef p_alist_1(p):
    'alist : 

def p_error(p):
  print("Syntax error in input!")

parser = yacc.yacc()

