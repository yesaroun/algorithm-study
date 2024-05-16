// https://leetcode.com/problems/two-sum/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let sortedNums = nums.slice().sort((a, b) => a - b);
  let start = 0;
  let end = sortedNums.length - 1;
  while (start < end) {
    if (sortedNums[start] + sortedNums[end] > target) {
      end--;
    } else if (sortedNums[start] + sortedNums[end] < target) {
      start++;
    } else {
      let index1 = nums.indexOf(sortedNums[start]);
      let index2 = nums.lastIndexOf(sortedNums[end]);
      return [index1, index2];
    }
  }
  return [];
};

twoSum([2,7,11,15], 9)