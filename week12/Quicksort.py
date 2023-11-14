def Quicksort(arr):
    if(len(arr) <= 1):
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return Quicksort(less) + [pivot] + Quicksort(greater)

numbers = [50, 10, 20, 100, 90, 80, 40, 120, 200, 30, 0]
print(Quicksort(numbers))