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