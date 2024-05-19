/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let maxSize = null;
  let start = 0;
  let end = height.length - 1;

  // 중첩 for문으로 모두 다 접근할 필요 없이(O(n^2))
  // 낮은 쪽의 포인터(start, end)를 이동 시키는 방식(O(n))
  // -> 면적을 최대로 하려면 height를 최대한 높게 해야하기 때문
  //    물론 width도 최대한 크게 유지해야하기에 점점 좁혀 들어감
  while (start < end) {
    let width = end - start;

    // 높이가 낮은게 tempHeight
    let minHeight;
    if (height[start] >= height[end]) {
      minHeight = height[end];
    } else {
      minHeight = height[start];
    }

    let size = width * minHeight;

    if (maxSize === null) {
      maxSize = size;
    } else if (maxSize < size) {
      maxSize = size;
    }

    if (height[start] >= height[end]) {
      end--;
    } else {
      start++;
    }
  }
  return maxSize;
};

let a = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]);
let b = maxArea([1, 1]);
let c = maxArea([4, 4, 2, 11, 0, 11, 5, 11, 13, 8]);
// 55

console.log(a, b, c);
