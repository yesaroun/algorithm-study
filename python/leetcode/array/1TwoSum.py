# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        start = 0
        end = len(sorted_nums) - 1
        while start < end:
            if sorted_nums[start] + sorted_nums[end] > target:
                end = end - 1
            elif sorted_nums[start] + sorted_nums[end] < target:
                start = start + 1
            else:
                index1 = nums.index(sorted_nums[start])
                # index가 같은 경우를 대비해서 idnex1은 넘김
                index2 = nums.index(sorted_nums[end])
                if index1 == index2:
                    index2 = nums.index(sorted_nums[end], index1 + 1)
                if index1 > index2:
                    index1, index2 = index2, index1
                return [index1, index2]

solution = Solution()
solution.twoSum([3, 2, 4], 6)
solution.twoSum([3, 3], 6)
solution.twoSum([-1,-2,-3,-4,-5], -8)

# 61ms
# 50ms
# 62ms
# 7ms
