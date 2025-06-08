def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0  
    
    while low <= high:
        iterations += 1  
        mid = (high + low) // 2
        
        if arr[mid] == x:
            return (iterations, arr[mid])
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    if low >= len(arr):  
        return (iterations, arr[-1] if arr[-1] >= x else None)
    elif low == 0 and arr[0] < x:
        return (iterations, arr[0] if arr[0] >= x else None)
    else:
        return (iterations, arr[low]) 

arr = [2.1, 3.2, 4.3, 10.1, 40.6]
x = 5.0
result = binary_search(arr, x)
print(f"{result}")
