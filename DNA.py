def findRepeatedDnaSequences(s):

    def remove_left(deque):
        
        res = None
        if len(deque) >= 1:
            res = deque[0]
            del deque[0]
        return res

    # count repeated 10-letter-long sequences
    maps = {}
    # extract 10 consecutive letter in s
    deque = []
    # list results
    res = []

    for i in range(len(s)):
        # enqueue first 10 nucleotides
        if len(deque) < 10:
            deque.append(s[i])

        # from the 11th element check if this sequence exist -> it becomes the key of maps with value 1
        # check until the end of the string, and if the sequence exist increase by 1
        else:
            # maps.get(key , 0) if the key doesnot exist, it return 0
            maps["".join(deque)] = maps.get("".join(deque) , 0) + 1
            remove_left(deque)
            deque.append(s[i])
    # check the last sequence
    maps["".join(deque)] = maps.get("".join(deque) , 0) + 1
    
    # check sequence repeated more than 1
    for sub_str in maps.keys():
        if maps[sub_str] > 1:
            res.append(sub_str)
    return res

s = "TTTTTGGGGGTTTTTGGGGGGTTTTTAAACCC"
print(findRepeatedDnaSequences(s))

s = "TTTTTGGGGGTTTTTGGGGG"
print(findRepeatedDnaSequences(s))