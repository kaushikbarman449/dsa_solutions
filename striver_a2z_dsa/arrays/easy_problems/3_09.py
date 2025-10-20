# Find the missing number in an array

def findMissingNum(nums, N):
    missing_ints = []
    nums = sorted(nums)

    i, j = 1, 0

    while i <= N:
        if j >= len(nums) or nums[j] != i:
            missing_ints.append(i)
        else:
            j += 1
        i += 1

    return missing_ints


if __name__ == "__main__":
    list_values = [1, 2, 4, 7, 10]
    N = int(input("Enter N: "))
    print("Missing Elements", findMissingNum(list_values, N))
