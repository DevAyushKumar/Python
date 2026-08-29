arr = [1,2,3,4,5,6,7,8,9,10]

def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif target <= arr[mid]:
            right = mid - 1
        else :
            left = mid - 1
    return -1

a = int(input("Enter the number to be searched: "))
print(search(arr, a))