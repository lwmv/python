#!/usr/bin/python
# Quick sort
from random import shuffle
class QuickSort:
    def sort(a,threeWay=False):
        # shuffle needed for performance guarantee
        shuffle(a)
        if threeWay == False:
            QuickSort.qsort(a,0,len(a)-1)
        else:
            QuickSort.threeWay(a,0,len(a)-1)
        

    def qsort(a,low,high):
        if low >= high:
            return
        j = QuickSort.partition(a,low,high)
        QuickSort.qsort(a,low,j-1)
        QuickSort.qsort(a,j+1,high)

    def partition(a,low,high):
        key = a[low]
        i = low
        j = high+1
        while True:
            while True:
                i += 1
                if a[i]>=key or i==high:
                    break
            while True:
                j -= 1
                if a[j]<=key or j==low:
                    break
            #while a[i]<=key and i<high:
            #    i += 1
            #while a[j]>=key and j>low:
            #    j -= 1
            if i<j:
                a[i],a[j] = a[j],a[i]
            else:
                break
        a[low],a[j] = a[j],a[low]
        return j


############ 3-way quicksort ##############
    def threeWay(a,low,high):
        if low >= high:
            return
        lt = low
        gt = high
        key = a[low]
        i = low
        while i<=gt:
            if a[i] < key:
                a[lt],a[i] = a[i],a[lt]
                lt += 1
                i += 1
            elif a[i] > key:
                a[gt],a[i] = a[i],a[gt]
                gt -= 1
            else:
                i += 1
        QuickSort.threeWay(a,low,lt-1)
        QuickSort.threeWay(a,gt+1,high)


if __name__ == '__main__':
    def isSorted(a):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                return False
        else:
            return True

    #a = list('KRATELEPUIMQCXOS')
    a = list(range(20))
    shuffle(a)
    #a =[10, 0, 12, 2, 13, 8, 11, 14, 15, 9, 1, 4, 6, 17, 18, 16, 3, 19, 7, 5]
    #a=[1,2,1,2,1,2,1,2,1,2,1]
    print(a)
    i = QuickSort.sort(a,threeWay=True)
    print(a)
    print(isSorted(a))


