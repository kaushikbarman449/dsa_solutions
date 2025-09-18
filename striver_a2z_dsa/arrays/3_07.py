# Move all Zeros to the end of the array

def moveZeroes(nums):
    n = len(nums)

    # point j to the last element
    j = -1

    # iterate through the list to find the first index in the list containing 0
    for i in range(n):
        if nums[i] == 0:
            j = i
            break

    # After iterating if j is still -1 that means there are no 0s in the list
    if j == -1:
        return nums

    for i in range(j + 1, n):
        if nums[i] != 0:
            # swap the jth element with the next non-zero index element
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    return nums


if __name__ == "__main__":
    list_values = [1, 0, 2, 3, 0, 4, 0, 0, 1]
    print("Original List: ", list_values)
    print(moveZeroes(list_values))
