# binary search using selection sort 
from selection_sort import selectionsort #selection_sort.py is a python file 
def binarysearch(l,key):
    lower=0
    heigher=len(l)-1
    i=0
    j=0
    while i<len(l):
        mid=int((lower+heigher)/2)
        if l[mid]==key:
            print(f'Element {key} found at {mid+1} position')
            j=1
            break
        elif l[mid]>key:
            if heigher>mid:
                break     
            else:
                heigher=mid-1
                i=+1
                continue
            
        elif l[mid]<key:
            if lower>mid:
               break     
            else:
                lower=mid+1
                i=+1
                continue
            
    if j==0:    
        print(f'Element is not in the list')

m=list()
n=int(input('\n Enter no of elements='))
print('\n Enter elements-')
for i in range(n):
    b=int(input())
    m.insert(i,b)
b=selectionsort(n,m)
print(b)
ele=int(input('Element for search-'))
binarysearch(m,ele)


    
