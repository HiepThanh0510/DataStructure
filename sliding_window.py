def find_maxSlidingWindow(num_list, k):
    def remove_left(deque):
        """
        Simulate a function of deque
        Remove and return the leftmost of the list
        """
        res = None
        if len(deque) >= 1:
            res = deque[0]
            del deque[0]
        return res

    # if k = 1 max number is itself
    if k == 1:
      return num_list

    deque = []
    res = []
    # start and end are parts of sliding window
    start = 0
    end = 0

    for end, val in enumerate(num_list):
        # Make sure the leftmost element of deque is the greatest and the rightmost is the smallest in deque
        if len(deque) > 0:
            while deque[-1] < val:
                deque.pop()
                if len(deque) == 0:
                    break
      
        deque.append(val)
        # Start to find maximum when size of window = k (example: k=3, start=0, end=2)
        if end >= k -1:
            res.append(deque[0])
            if num_list[start] == deque[0]:
                remove_left(deque)

            start += 1

    return res

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
sub_list = []
res = []
for ele in num_list:
  sub_list.append(ele)
  if len(sub_list) == k:
    res.append(max(sub_list))
    del (sub_list[0])

print(res)