# Linear Search algorithm

def LinearSearch(arr,n,x):
    for i in range(0,n):
        if (arr[i]==x):
            return -1
    return i
x=85
arr=[4,8,9,5,85,3,7]
n=len(arr)

l=LinearSearch(arr,n,x)
print(arr)
if(l==-1):
    print("Linear search present ")
else:
    print("linear search  mising")

# example dirct checjk
a=[4,6,62,62,5,151,14,55,15,151]
x=45
if(a==x):
    print("present")
else:
    print("no")

# BINARY SEARCH ALGORITHM
def binary(arr,x):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
        return  -1
arr=[8,65,6,2,7,78,56,12,45,86,22]
x=86
result=binary(arr,x)
if result == -1:
    print("element present")
else:
    print("not present")