def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr=[4,5,6,8,10,12,1,2,3,4,5,8]
bubble(arr)
print("sorted array is=",arr)
