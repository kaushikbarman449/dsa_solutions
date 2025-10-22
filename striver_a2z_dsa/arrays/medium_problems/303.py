# Find the Majority Element that occurs more than N/2 times

def checkMajorityElement(nums):
    seen_count = {}
    for num in nums:
        if num not in seen_count:
            seen_count[num] = 0
        seen_count[num] += 1

    for key, value in seen_count.items():
        if value > len(nums) // 2:
            return key

    return None


def checkMajElUsingMooreVotingAlgorithm(nums):
    count = 0
    el = None

    for i in range(len(nums)):
        if count == 0:
            count = 1
            el = nums[i]
        elif el == nums[i]:
            count += 1
        else:
            count -= 1

    count_el = 0

    for i in range(len(nums)):
        if nums[i] == el:
            count_el += 1

    if count_el > len(nums) // 2:
        return el

    return None


if __name__ == "__main__":
    nums = [-1, -2, -1, -2, -1, -2, -1]
    N = len(nums)
    print(
        f"Element that occurs more than {N} / 2 times: {checkMajorityElement(nums)}")
    print(
        f"Element that occurs more than {N} / 2 times using Moor's Voting Algorithm: {checkMajElUsingMooreVotingAlgorithm(nums)}")
