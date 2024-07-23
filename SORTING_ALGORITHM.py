# Bubble sort
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp

data=[-5,6,8,4,78,566541,69]
bubbleSort(data)
print("original data given:")
print("sorted data printed:",data)

# Selection sort Algorithm
def selectionSort(array,size):
    for step in range(size):
        minIND=step
        for i in range(step+1,size):
            if array[i]<array[minIND]:
                minIND=i
                (array[step],array[minIND])=(array[minIND],array[step])

data2=[54,66,8459,897498,6441,6,654,987]
size=len(data)
selectionSort(data,size)
print(data2)

# Insertion sort Algorithm
def InsertionSort(array):
    for step in range(1,len(array)):
        key=array[step]
        j=step-1

        while j>=0 and key < array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key

data3=[78,65,6,63,56,5,6,56,54]
InsertionSort(data3)
print("sorted array insertion",data3)

# QUick sort algoritm
#def partion(array,low,high):
 #   pivot=array[high]