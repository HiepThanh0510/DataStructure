def calcualte(s):
  def div(num1, num2):
    # assume num2 != 0
    result = None 
    if num1 >=0:
      result = num1//num2
    else:
      result = (num1//num2) + 1
    return result  

  operators = "+-*/"
  # nums = "0123456789"
  currentNum = ''
  currentOp = '+' # assume positive numbers
  stack = []
  len_s = len(s)
  for i in range(len_s):
    char = s[i]
    if char.isspace() and (i < len(s)-1):
      continue
    # Find num
    if char.isdigit():
      currentNum += char
    
    # operator or end of string 
    if char in operators or (i==len(s)-1):
      if currentOp == "+":
        stack.append(int(currentNum))
      elif currentOp == "-":
        stack.append(-int(currentNum))
      elif currentOp == "*":
        stack[-1] = stack[-1]*int(currentNum)
      elif currentOp == "/":
        stack[-1] = div(stack[-1],int(currentNum))
        # Skip, assume valid expression
        
      currentNum = ''
      currentOp = char
  return sum(stack)

print(calcualte("4/2 + 9/3")) #the result is 5