def intersect(num_list1, num_list2):
    dict1={}
    dict2={}
    res=[]

    # count occurrence of each number in list 1
    for num1 in num_list1:
        dict1[num1] = dict1.get(num1, 0) + 1
       

    # count occurrence of each number in list 2
    for num2 in num_list2:
        dict2[num2] = dict2.get(num2, 0) + 1
      

    # if dict1 or dict2 is empty, return empty list
    if not dict1 or not dict2:
        return res

    # count number which occur in both list => shoulde choose the shortest one
    len_num_list1 = len(num_list1)
    len_num_list2 = len(num_list2)
    temp_list = []
    if len_num_list1 <= len_num_list2:
        temp_list = num_list1
    else:
        temp_list = num_list2

  
    for n in temp_list:        
        if n in dict1 and n in dict2:
            dict1[n]-=1
            dict2[n]-=1
            if dict1[n]==0:
                del dict1[n]
            if dict2[n]==0:
                del dict2[n]
            res.append(n)
    return res

num_list1 = [4, 9, 5]
num_list2 = [9, 4, 9, 8, 4]
print(intersect(num_list1, num_list2))

num_list1 = [1, 3, 3, 3, 1]
num_list2 = [3, 3]
print(intersect(num_list1, num_list2))