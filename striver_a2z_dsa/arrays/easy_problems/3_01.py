# Find the Largest element in an array

def getLargestNum(nums):
    largest_num = float('-inf')
    for num in nums:
        if num > largest_num:
            largest_num = num

    return largest_num


if __name__ == "__main__":
    list_values = [13, 46, 24, 52, 20, 9, -1, -10, 32, 32, 100]
    print("Largest Element", getLargestNum(list_values))
