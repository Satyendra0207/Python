from  array import*
def selectionsort(n,a):
    for i in range(n): # Traverse through all list elements
        min = i
        for j in range(n): 
            if a[j]>a[min]: #for ascending order ------a[j]<a[min] for descending order
                min=j
                a[min],a[i] =a[i],a[min] # element at j is small
                
    return a
                
'''    #print(a)
b=array('i',[8,7,13,1,12,10])
x=len(b)
print(b,'\n')
b=selectionsort(x,b)
print(b)'''
