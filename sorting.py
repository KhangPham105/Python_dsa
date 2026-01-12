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
print(arr3)
insertion_sort(arr3)
print(arr3)