def mergeSortedLists(listA, listB):
    newList = list()
    a = 0
    b = 0
    
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1
     
    while a < len(listA):
        newList.append(listA[a])
        a += 1
    while b < len(listB):
        newList.append(listB[b])
        b += 1
    
    return newList
testlistA = [2, 8, 15, 23, 37]
testlistB = [4, 6, 15, 20]

print('List A ={}'.format(testlistA) + '\nList B ={}'.format(testlistB))
print('After merge sorted lists:{}'.format(mergeSortedLists(testlistA, testlistB)))

