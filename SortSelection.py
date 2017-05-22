def SortSelection(ArrToSort):
    a = ArrToSort
    for i in range(len(a)):
        Min = i
        for j in range(i+1, len(a)):
            if a[j] < a[Min]:
                Min = j
        tmp = a[Min]
        a[Min] = a[i]
        a[i] = tmp
    return a

ary = [5,3,10,1,2,3,5,4,79,78,23,109]
print  (ary)
print  (SortSelection(ary))