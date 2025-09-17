# Check if an Array is Sorted

def isSorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            return True
        return False


if __name__ == "__main__":
    list_values = [13, 46, 24, 52, 20, 9, -1, -10, 32, 32, 100]
    print(isSorted(list_values))
