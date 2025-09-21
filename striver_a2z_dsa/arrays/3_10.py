# Count Maximum Consecutive One's in the array

def countMaxOnes(nums):
    count = 0
    max_count = 0
    for j in range(len(nums)):
        if nums[j] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count


if __name__ == "__main__":
    list_values = [1, 0, 1, 1, 1, 1, 0, 1]
    print("Maximum consecutive ones", countMaxOnes(list_values))
