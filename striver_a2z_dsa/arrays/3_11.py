# Find the number that appears once, and the other numbers twice
# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

def checkNum(nums):
    max_hash_size = max(nums)
    hash_list = [0] * (max_hash_size + 1)

    for num in nums:
        hash_list[num] += 1

    for i in range(len(hash_list)):
        if hash_list[i] == 1:
            return i


def checkNumDict(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count == 1:
            return num


if __name__ == "__main__":
    list_values = [-10, 1, 2, 1, 2, 3, 3]
    print("Number appearing once using Dict", checkNumDict(list_values))
    print("Number appearing once", checkNum(list_values))
