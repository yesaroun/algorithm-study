package paradigm.bruteForce;

public class ProductCalculator {
    public static int minProduct(int[] leftList, int[] rightList) {
        int minResult = Integer.MAX_VALUE;
        for (int left : leftList) {
            for (int right : rightList) {
                int currentResult = left * right;
                minResult = Math.min(minResult, currentResult);
            }
        }
        return minResult;
    }

    public static void main(String[] args) {
        int[] leftList = {1, 3, 4};
        int[] rightList = {3, 4, 5};
        System.out.println(minProduct(leftList, rightList));    // 3

        int[] leftList2 = {-3, 4, -9};
        int[] rightList2 = {3, -2, 1};
        System.out.println(minProduct(leftList2, rightList2));  // 27
    }
}
