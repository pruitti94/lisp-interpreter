import ply.yacc as yacc
from LISPLexer import tokens

############################
#lispStart -> lisp|bool|list
############################
def p_lispStart_1(p):
  'lispStart : lisp SEMI'
  p[0] = p[1]

def p_lispStart_2(p):
  'lispStart : bool SEMI'
  p[0] = p[1]
  
def p_lispStart_3(p):
  'lispStart : list SEMI'
  p[0] = p[1]
############################


############################################
#These are all the lisp operations and stuff
############################################

#Simply returns the number  
def p_lisp_1(p):
  'lisp : NUMBER'
  p[0] = ['num',p[1]]

#ADDITION  
#Adds two elements together
def p_lisp_2(p):
  'lisp : LPARENT PLUS lisp lisp RPARENT'
  p[0] = ['aop','+',p[3],p[4]]

#SUBTRACTION
#Subtracts the second element from the first element
def p_lisp_3(p):
  'lisp : LPARENT MINUS lisp lisp RPARENT'
  p[0] = ['-',p[3],p[4]]

#MULTIPLICATION
#Multiplies two elements
def p_lisp_4(p):
  'lisp : LPARENT TIMES lisp lisp RPARENT'
  p[0] = ['*',p[3],p[4]]

#DIVISION
#Divides the first element by the second element
def p_lisp_5(p):
  'lisp : LPARENT DIV lisp lisp RPARENT'
  p[0] = ['/',p[3],p[4]]

#IF
#Checks a boolean condition and returns value based on said result
def p_lisp_6(p):
  'lisp : LPARENT IF bool lisp lisp RPARENT'
  p[0] = ['if',p[3],p[4],p[5]]

#car
def p_lisp_7(p):
  'lisp : LPARENT CAR list RPARENT'
  p[0] = ['car',p[3]]

############################################


###############################################
#These are all the boolean operations and stuff
###############################################

#TRUE
#Returns a value of TRUE
def p_bool_1(p):
  'bool : TRUE'
  p[0] = ['bool',p[1]]

#FALSE
#Returns a value of FALSE
def p_bool_2(p):
  'bool : FALSE'
  p[0] = ['bool',p[1]]

#GREATER
#Compares two elements and returns a boolean value based on >
def p_bool_3(p):
  'bool : LPARENT GREATER lisp lisp RPARENT'
  p[0] = ['comparison',p[2],p[3],p[4]]

#GREATEREQUAL
#compares twos elements and returns a boolean value based on >=
def p_bool_4(p):
  'bool : LPARENT GREATEREQUAL lisp lisp RPARENT'
  p[0] = ['comparison', p[2],p[3],p[4]]

#LESS
#Compares two elements and returns a boolean value based on <
def p_bool_5(p):
  'bool : LPARENT LESS lisp lisp RPARENT'
  p[0] = ['comparison',p[2],p[3],p[4]]

#LESSEQUAL
#Compares two elements and returns a boolean value based on >=
def p_bool_6(p):
  'bool : LPARENT LESSEQUAL lisp lisp RPARENT'
  p[0] = ['comparison', p[2],p[3],p[4]]

#NOTEQUAL
#Compares two elements and returns a boolean value based on <>
def p_bool_7(p):
  'bool : LPARENT NOTEQUAL lisp lisp RPARENT'
  p[0] = ['comparison', p[2],p[3],p[4]]

#EQUAL
#Compares two elements and returns a boolean value based on <>
def p_bool_8(p):
  'bool : LPARENT EQUAL lisp lisp RPARENT'
  p[0] = ['comparison', p[2],p[3],p[4]]

#AND
#Compares two values two values with a logical 'and' and returns a boolean vluae
def p_bool_9(p):
  'bool : LPARENT AND bool bool RPARENT'
  p[0] = ['if',p[2],p[3]]
  
###############################################

##################################
#These are all the list operations
##################################
def p_list_1(p):
  'list : LPARENT list RPARENT'
  p[0] = ['list',p[2]]

def p_list_2(p):
  'list : lisp'
  p[0] = [p[1]]

def p_list_3(p):
  'list : lisp list'
  p[0] = [p[1]] + p[2]

#cons
def p_list_5(p):
  'list : LPARENT CONS lisp list RPARENT'
  p[0] = ['cons',p[3],p[4]]

#cdr
def p_list_6(p):
  'list : LPARENT CDR list RPARENT'
  p[0] = ['cdr',p[3]]

def p_error(p):
  print("Syntax error in input!")

parser = yacc.yacc()

