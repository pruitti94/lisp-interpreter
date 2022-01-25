from LISPParser import parser

def eval(tree):
  if tree[0] == 'list' or tree[0] == 'cdr' or tree[0] == 'car' or tree[0] == 'cons':
    #print('this is a list operation')
    return eval_list(tree)
  elif tree[0] == 'bool' or tree[0] == 'comparison' or tree[0] == 'and' or tree[0] == 'or' :
    #print('this is a boolean or comparison')
    return eval_bool(tree)
  elif tree[0] == 'num' or tree[0] == 'aop' or tree[0] == 'if':
    #print('this is a lisp operation');
    return eval_num(tree)
  #else:
  #return None

def eval_num(tree):
  if tree[0] == 'num':
    return tree[1]
  if tree[1] == '+' or tree[1] == '-' or tree[1] == '*' or tree[1] == '/':
    v1 = eval(tree[2])
    v2 = eval(tree[3])
    if type(v1) != float or type(v2) != float:
        return
    if tree[1] == '+':
      return v1+v2
    elif tree[1] == '*':
      return v1*v2
    elif tree[1] == '-':
      return v1-v2
    if v2 != 0:
      return v1/v2
    else:
      return('ERROR DIVIDE BY ZERO!')
  if tree[0] == 'if':
    print('THIS IS AN IF STATEMENT')
    result = eval(tree[1])
    if (result == True):
        print('TRUE!!!!')
        return eval(tree[2])
    else:
        print('FALSE!!!!!')
        return eval(tree[3])
        
def cdr_helper(tree):
    print('cdr helper method here')
    if not tree:
        #print('CANNOT CDR ON EMPTY LIST!!!!')
        return('CANNOT CDR ON EMPTY LIST!!!!')
    newList = []
    #for x in tree[1:]:
    #    newList.append(x)
    #print(newList)
    tree.pop(0)
    print(tree)
    return tree

def car_helper(tree):
    if not tree:
        return('CANNOT CAR ON EMPTY LIST!!!!')
    x = tree[1][1][0]
    return x

def cons_helper(tree, newValue):
    print('ORIGINAL TREE')
    print(tree)
    tree.insert(0,newValue)
    print('NEW TREE')
    print(tree)
    return tree
    
def eval_list(tree):
  myNewList = []

  if tree[0] == 'list' and tree[1] != None:
    return(tree[1])
    
  elif tree[0] == 'list' and tree[1] == None:
    print('THIS LIST IS EMPTY')
    return([]);

  elif tree[0] == 'cdr':
    print('this is the cdr method')
    return cdr_helper(eval(tree[1]))
    
  elif tree[0] == 'car':
    print('this is the car method lol')
    if tree[1] == []:
        return('CANNOT CAR ON EMPTY LIST')
    print('printing tree 1')
    print(tree)
    #print(tree)
    #print('TEST TEST TEST')
    y = eval(tree[1])
    if y == None:
        return('')
    eval(y)
    return eval(y[0])
    
  elif tree[0] == 'cons':
    print('hello, this is the cons method')
    return cons_helper(eval(tree[2]), (tree[1]))

def eval_bool(tree):
  print('THIS IS THE BOOL EVALUATION METHOD')
  if tree[1] == ('True'):
    return True
  elif tree[1] == ('False'):
    return False
  elif tree[0] == ('and'):
    v1 = eval(tree[1])
    v2 = eval(tree[2])
    return v1 and v2
  elif tree[0] == ('or'):
    v1 = eval(tree[1])
    v2 = eval(tree[2])
    return v1 or v2
  elif tree[0] == 'comparison':
    print('THIS IS A COMPARISON!')
    if tree[1] == '>':
        print('This is a greater than sign!')
        v1 = eval(tree[2])
        v2 = eval(tree[3])
        print(v1)
        print(v2)
        return (v1 > v2)

    elif tree[1][1] == '<':
        print('This is a less than sign!')
        v1 = eval(tree[2])
        v2 = eval(tree[3])
        print(v1)
        print(v2)
        return (v1 < v2)
            
    elif tree[1][1] == '>=':
        print('This is a greater than or equal to sign!')
        v1 = eval(tree[2])
        v2 = eval(tree[3])
        print(v1)
        print(v2)
        return (v1 >= v2)
            
    elif tree[1][1] == '<=':
        print('This is a less than or equal to sign!')
        v1 = eval(tree[2])
        v2 = eval(tree[3])
        print(v1)
        print(v2)
        return (v1 <= v2)

    elif tree[1][1] == '=':
        print('This is an equal to sign!')
        v1 = eval(tree[2])
        v2 = eval(tree[3])
        print(v1)
        print(v2)
        return (v1 == v2)

    elif tree[1][1] == '<>':
        print('This is an equal to sign!')
        v1 = eval(tree[2])
        v2 = eval(tree[3])
        print(v1)
        print(v2)
        return (v1 != v2)

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
  #print(type(result));
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
    try:
      answer = eval(tree)
      if (answer is None):
        #print('ANSWER IS NONE')
        answer = 'Syntax error in input!'
      #if isinstance(answer,str):
      #  print('Syntax issue')
      else:exit;
      if type(answer) == list:
        print('the answer is a list')
        print('the answer is ' +str(answer))
        print(len(answer))
        for i in range(len(answer)):
            print(eval(answer[i]))
      else:
        print(str(answer))
    except Exception as inst:
        #print('issue here')
        data = read_input()
        print(inst.args[0])
       
 
main()
