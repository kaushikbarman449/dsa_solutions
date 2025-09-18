# Rotate array by K elements

def leftRotateByK(nums, k):
    n = len(nums)
    k = k % n

    temp = [0] * k
    for i in range(k):
        temp[i] = nums[i]

    for i in range(k, n):
        nums[i - k] = nums[i]

    for i in range(n-k, n):
        nums[i] = temp[i - (n-k)]

    return nums


if __name__ == "__main__":
    list_values = [1, 1, 24, 24, 9, 9, -10, 32, 32, 100]
    k = int(input("Enter elements to be rotated: "))
    print(leftRotateByK(list_values, k))
