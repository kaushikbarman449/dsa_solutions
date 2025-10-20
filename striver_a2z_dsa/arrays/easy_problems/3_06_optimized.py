# Rotate array by K elements in O(1) space complexity

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def leftRotateByK(nums, k):
    n = len(nums)
    k = k % n

    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    reverse(nums, 0, n - 1)

    return nums


if __name__ == "__main__":
    list_values = [1, 1, 24, 24, 9, 9, -10, 32, 32, 100]
    k = int(input("Enter elements to be rotated: "))
    print(leftRotateByK(list_values, k))
