# Left Rotate the Array by One

def leftRotate(nums):
    n = len(nums)
    temp = nums[0]
    for i in range(n - 1):
        nums[i] = nums[i + 1]
    nums[n - 1] = temp
    return nums


if __name__ == "__main__":
    list_values = [1, 1, 24, 24, 9, 9, -10, 32, 32, 100]
    print(leftRotate(list_values))
