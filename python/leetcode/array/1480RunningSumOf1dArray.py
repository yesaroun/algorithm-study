from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


def test_solution():
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.runningSum(nums=nums)
        assert (
            result == expected
        ), f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
