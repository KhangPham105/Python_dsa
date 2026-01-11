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
print()
bubble_sort(arr)
print(arr)