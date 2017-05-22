def SortInsertion(ArrToSort):

    a = ArrToSort
    for i in range(len(a)):
        b = a[i]
        j = i;
        while (a[j-1] > b) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
        a[j] = b
        print (a)
    assert isinstance(a,object)
    return a

ary = [5,3,10,1,2,3,5,4,79,78,23,109]
print (ary)
print (SortInsertion(ary))