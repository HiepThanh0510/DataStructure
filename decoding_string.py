def decodeString(encodedString):
  string = ""
  k = 0  
  stack = [] # string and k
  for es in encodedString:
    # find k
    if es.isdigit():
      k = k*10 + int(es)
    # push to string and k to stack
    elif  es == "[":
      stack.append(string)
      stack.append(k)
      string = '' # next string is in []
      k = 0 
    # get string 
    elif  es.isalpha():
      string += es
    elif  es == "]":
      num = stack.pop()
      pre_string = stack.pop()
      string = pre_string + num*string 
  return string

coded_str = "2[hiep]4[thanh]deptrai"
print(decodeString(coded_str)) #the result is hiephiepthanhthanhthanhthanhdeptrai

