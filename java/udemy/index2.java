public class index2 {
    public static void main(String[] args) {
        // Input
        int[] scores = { 100, 75, 50, 37, 90, 95 };
        int sum = 0;
        int N = scores.length;

        for (int i = 0; i < N; i++) {
            if (scores[i] >= 80) {
                sum += scores[i];
            }
        }

        System.out.printf("%d명의 80점 이상 총합: %d", N, sum);
    }
}
