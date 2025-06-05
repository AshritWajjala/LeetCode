# 88) Merge Sorted array

def merge(list1, m, list2, n):
    for i in range(n):
        list1[m+i]=list2[i]
                
        return list1.sort()