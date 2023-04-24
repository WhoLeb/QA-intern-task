def is_greater_precedence(op1, op2):
    pre = {'+':0, '-': 0, '*':1, '/':1, '^':2}
    return pre[op1] >= pre[ op2]

def shunting_yard(expression):
    tokens = expression.split()
    op_stack = []
    out_queue = []
    try:
        for token in tokens:
            if token not in ['+', '-', '*', '/', '(', ')']:
                out_queue.append(token)
            if token in ['+', '-', '*', '/']:
                print("operator")
                while op_stack and op_stack[-1] in ['+', '-', '*', '/'] and (is_greater_precedence(op_stack[-1], token)):
                    out_queue.append(op_stack.pop())
                op_stack.append(token)
            if token == '(':
                op_stack.append(token)
            if token == ')':
                while op_stack[-1] != '(':
                    if not op_stack:
                        raise Exception
                    out_queue.append(op_stack.pop())
                if op_stack[-1] != '(':
                    raise Exception
                op_stack.pop()
        while op_stack:
            if op_stack[-1] == '(':
                raise Exception
            out_queue.append(op_stack.pop())
    except Exception:
        print("mismatched parentheses")
    return out_queue

def evaluate(expression):
  stack = []
    
  for ele in expression:
      
    if ele not in '/*+-':
      stack.append(int(ele))
      
    else:
      right = stack.pop()
      left = stack.pop()
        
      if ele == '+':
        stack.append(left + right)
          
      elif ele == '-':
        stack.append(left - right)
          
      elif ele == '*':
        stack.append(left * right)
          
      elif ele == '/':
        stack.append(int(left / right))
    
  return stack.pop()

expression = "2 + 2 * 3"
print(shunting_yard(expression))

print(evaluate(shunting_yard(expression)))

