
def binary_search(arr, element, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == element:
        return mid
    elif arr[mid] < element:
        return binary_search(arr, element, mid+1, right)
    else:
        return binary_search(arr, element, left, mid-1)
