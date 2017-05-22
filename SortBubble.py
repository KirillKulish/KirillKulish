def SortBubble(ArrToSort):
    a = ArrToSort
    for i in range(len(a),0,-1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp
                print (a)
    return a

ary = [5,3,10,1,2,3,5,4,79,78,23,109]
print (ary)
print (SortBubble(ary))