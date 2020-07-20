def linear_search(arr, target):
    # Your code here

    # set the counter to return the index inside the array
    n=-1
    # write a for loop for each number in the array
    for num in arr:
        # increment the counter
        n+=1
        # if the num is the same as the target, return the index
        if num == target:
            return n
    # if it isn't found, return -1 / False
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here

    # set the low to 0
    low = 0
    # set the high to the length of the array minus 1
    high = len(arr)-1

    # for the iterative example, start a while loop, while the low value is less than the high value
    while low <= high:
        # calculate the mid index by adding high and low
        # and finding the remainder, dividing by 2
        mid = (low+high) // 2
        # now set the guess using the middle index
        guess = arr[mid]
        # Case 1: the guess is correct
        if guess == target:
            # if so, return the index
            return mid
        # Case 2: the guess is too high
        if guess > target:
            # if so, change the high value to mid-1
            high = mid-1
        # Case 3: the guess is too low
        if guess < target:
            # if so, change the low value to mid+1
            low = mid+1

    return -1  # not found
