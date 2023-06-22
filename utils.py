def findMax(arr):
    max = arr[0]
    for number in arr:
        if number > max:
            max = number
        return max
