// Input
var scores = [100, 75, 50, 37, 90, 95];
var sum = 0;
var N = scores.length;
// Process
for (var score = 0; score < N; score++) {
    if (scores[score] >= 80) {
        sum += scores[score];
    }
}
// Output
console.log("".concat(N, "\uBA85\uC758 80\uC810 \uC774\uC0C1 \uCD1D\uC810: ").concat(sum));
