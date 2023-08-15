"use strict";
function minProduct(leftList, rightList) {
    let minResult = Number.POSITIVE_INFINITY;
    for (const left of leftList) {
        for (const right of rightList) {
            const currentResult = left * right;
            minResult = Math.min(minResult, currentResult);
        }
    }
    return minResult;
}
if (require.main === module) {
    console.log(minProduct([1, 3, 4], [3, 4, 5])); // 3
    console.log(minProduct([-3, 4, -9], [3, -2, 1])); // -27
}
