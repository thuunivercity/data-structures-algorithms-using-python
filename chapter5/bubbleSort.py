#The author made a mistake, and I modify it. Pls check it carfully.

def bubbleSort(list):
    n = len(list)
    for i in range(n-1):
        for j in range(n-1-i):
            if list[j] > list[j+1]:
                # this formula is more pythonic.
                list[j], list[j+1] = list[j+1], list[j]
    return list

testlist = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print testlist
print bubbleSort(testlist)
