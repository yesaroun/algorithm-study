// Input
let scores: number[] = [100, 75, 50, 37, 90, 95];
let sum: number = 0;
const N: number = scores.length;

// Process
for (let i: number = 0; i < N; i++) {
  if (scores[i] >= 80) {
    sum += scores[i];
  }
}

// Output
console.log(`${N}명의 80점 이상 총점: ${sum}`);
