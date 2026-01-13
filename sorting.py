import random

def bubble_sort(arr):
    check=False
    while(check==False):
        check=True
        for i in range(len(arr)-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1]= arr[i+1], arr[i]
                check=False
arr = [random.randint(1, 100) for _ in range(10)]
print("Bubble sort test:")
print(arr)
bubble_sort(arr)
print(arr)

def insertion_sort(arr):
    count=len(arr)
    if (count >1 ):
        current=1
        while (current < count):
            temp=arr[current]
            walker=current-1
            while ((walker>=0) and (temp<arr[walker])):
                arr[walker+1]=arr[walker]
                walker-=1
            arr[walker+1]=temp
            current+=1

arr2 = [random.randint(1, 100) for _ in range(10)]
print()
print("Insertion sort test:")
print(arr2)
insertion_sort(arr2)
print(arr2)

def selection_sort(arr):
    count=len(arr)
    if (count>1):
        current=0
        while (current <count):
            swap_index=-1
            min_element=arr[current]
            walker=current
            while (walker<count ):
                if (arr[walker]<min_element):
                    swap_index=walker
                    min_element=arr[walker]
                walker+=1
            arr[swap_index]=arr[current]
            arr[current]=min_element
            current+=1

arr3 = [random.randint(1, 100) for _ in range(10)]
print()
print("Selection sort test:")
print(arr3)
insertion_sort(arr3)
print(arr3)

def shell_sort(arr):
    count=len(arr)
    interval=count/2
    while (interval >=0):
        i=0
        for i in count and i+interval <count:
            if (arr[i] < arr[i+interval]):
                arr[i], arr[i+interval]=arr[i+interval], arr[i]
        interval/=2

arr4 = [random.randint(1, 100) for _ in range(10)]
print()
print("Shell sort test:")
print(arr4)
insertion_sort(arr4)
print(arr4)

def partition(arr, low, high):
    pivotIndex=(high+low)//2
    pivot=arr[pivotIndex]
    arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]
    i=low
    for j in range(low, high-1):
        if (arr[j]<=pivot):
            arr[i], arr[j]=arr[j], arr[i]
            i+=1
    arr[i], arr[high]= arr[high], arr[i]

def quick_sort(arr,low, high):
    if low<high:
        pivot_index=partition(arr, low, high)

        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)

arr5 = [random.randint(1, 100) for _ in range(10)]
print()
print("Quick sort test:")
print(arr5)
insertion_sort(arr5)
print(arr5)