# Two sum

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return seen[diff], i
        seen[num] = i


if __name__ == "__main__":
    target = int(input("Enter target value: "))
    nums = [2, 7, 11, 15]
    print(f"Indices for {target}: {twoSum(nums, target)}")
