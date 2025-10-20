# Longest Subarray with given Sum K(Positives)
def longest_subArray_O3(nums, sum_k):
    subArray_len = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_sum = 0
            for k in range(i, j+1):
                current_sum += nums[k]
            if current_sum == sum_k:
                subArray_len = max(subArray_len, j - i + 1)

    return subArray_len


if __name__ == "__main__":
    sum_k = int(input("Enter k: "))
    list_values = [2, 3, 9, 5, 1, 3, 1, 9]
    print(f"Length of longest subarray with {sum_k}:", longest_subArray_O3(
        list_values, sum_k))
