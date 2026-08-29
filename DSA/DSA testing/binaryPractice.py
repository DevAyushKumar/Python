arr1 = [-2,3,4,7,8,9,11,13]
arr2 = [13,-2,3,4,7,8,9,11]
arr3 = [8,9,11,13,-2,3,4,7]

target = 11

def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target <= arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(search(arr1, target))
print(search(arr2, target))
print(search(arr3, target))