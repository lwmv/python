#!/usr/bin/python
# heap sort
class HeapSort:
    def sort(a):
        HeapSort.heapify(a)
        HeapSort.hsort(a)
    
    def heapify(a):
        n = len(a)
        k = n//2
        while k>=1:
            HeapSort.sink(a,k,n) 
            k -= 1 
    
    def hsort(a):
        n = len(a)
        while n>1:
            a[0],a[n-1] = a[n-1],a[0]
            n -= 1
            HeapSort.sink(a,1,n)


    def sink(a,k,n):
        key = a[k-1]
        while 2*k <= n:
            c = 2*k
            if c < n and a[c-1]<a[c]:
                c += 1
            if not(key<a[c-1]):
                break
            else:
                a[k-1] = a[c-1]
                k = c
        a[k-1] = key

if __name__ == '__main__':
    import random
    s = list(range(10))
    random.shuffle(s)
    print(s)
    HeapSort.sort(s)
    print(s)

