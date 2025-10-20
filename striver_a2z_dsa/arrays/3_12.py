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


def longest_subArray_O2(nums, sum_k):
    subArray_len = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == sum_k:
                subArray_len = max(subArray_len, j - i + 1)

    return subArray_len


def longest_subArray_On(nums, sum_k):
    prefix_map = {}
    prefix_sum = 0
    max_len = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum == sum_k:
            max_len = i + 1

        if (prefix_sum - sum_k) in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - sum_k])

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len


if __name__ == "__main__":
    sum_k = int(input("Enter k: "))
    list_values = [2, 3, 9, 5, 1, 3, 1, 9, 0, 0, 0, 0]
    print(f"Length of longest subarray with {sum_k} in O(3):", longest_subArray_O3(
        list_values, sum_k))
    print(f"Length of longest subarray with {sum_k} in O(2):", longest_subArray_O2(
        list_values, sum_k))
    print(f"Length of longest subarray with {sum_k} in O(n):", longest_subArray_On(
        list_values, sum_k))
