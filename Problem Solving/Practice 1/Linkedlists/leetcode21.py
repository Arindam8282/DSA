def mergeTwoLists(list1: [], list2: []) -> []:
    mergerList = [] 
    item = None
    while len(list1)!=0 and len(list2)!=0:
        if list1[0] < list2[0]:
            item = list1.pop(0)

        else:
            item = list2.pop(0)
        mergerList.append(item) 
    if len(list1)==0:
        mergerList.extend(list2)
    else:
        mergerList.extend(list1)
    return mergerList
print(mergeTwoLists([1,3,5,10],[1,2,6,7,9]))

    