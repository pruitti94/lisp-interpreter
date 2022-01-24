from LISPParser import parser

def eval(tree):
  if tree[0] == 'list' or tree[0] == 'cdr' or tree[0] == 'car' or tree[0] == 'cons':
    #print('this is a list operation')
    return eval_list(tree)
  elif tree[0] == 'bool' or tree[0] == 'comparison':
    #print('this is a boolean or comparison')
    return eval_bool(tree)
  elif tree[0] == 'num' or tree[0] == 'aop':
    #print('this is a lisp operation');
    return eval_num(tree)
  else:
    return None

def eval_num(tree):
  if tree[0] == 'num':
    return tree[1]
  if tree[1] == '+' or tree[1] == '-' or tree[1] == '*' or tree[1] == '/':
    v1 = eval(tree[2])
    v2 = eval(tree[3])
    if tree[1] == '+':
      return v1+v2
    elif tree[1] == '*':
      return v1*v2
    elif tree[1] == '-':
      return v1-v2
    if v2 != 0:
      return v1/v2
    else:
      return('ERROR ERROR ERROR ERROR DIVIDE BY ZERO!')

def cdr_helper(tree):
    if not tree:
        #print('CANNOT CDR ON EMPTY LIST!!!!')
        return('CANNOT CDR ON EMPTY LIST!!!!')
    newList = []
    for x in tree[1:]:
        newList.append(x)
    return newList
    
def car_helper(tree):
    x = tree[1][1][0]
    return x
    
def eval_list(tree):
  myNewList = []

  if tree[0] == 'list' and tree[1] != '()':
    return tree[1]
    
  elif tree[0] == 'list' and tree[1] == '()':
    return('EMPTY LIST()');

  elif tree[0] == 'cdr':
    return cdr_helper(eval(tree[1]))
    
  elif tree[0] == 'car':
    print('this is the car method lol')
    if tree[1] == '()':
        return('')
    #print(tree)
    #print('TEST TEST TEST')
    y = eval(tree[1])
    if y == None:
        return('')
    eval(y)
    return eval(y[0])
    
  elif tree[0] == 'cons':
    print('hello')
    tree[2][1].append((tree[1]))
    print(tree[2][1])
    return('')

def eval_bool(tree):
  print('THIS IS THE BOOL EVALUATION METHOD')
  return

    
    
def read_input():
  result = ''
  while True:
    data = input('LISP: ').strip()
    if ';' in data:
      i = data.index(';')
      result += data[0:i+1]
      break
    else:
      result += data + ' '
  return result

def main():
  while True:
    data = read_input() 
    if data == 'exit;':
      break
    try:
      tree = parser.parse(data)
    except Exception as inst:
      print(inst.args[0])
      continue
    print(tree)
    try:
      answer = eval(tree)
      #if isinstance(answer,str):
      #  print('\nEVALUATION ERROR: '+answer+'\n')
      #else:
      print(str(answer)+'\n')
    except Exception as inst:
      print(inst.args[0])
       
 
main()
