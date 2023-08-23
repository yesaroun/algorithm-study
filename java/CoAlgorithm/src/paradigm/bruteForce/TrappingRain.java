package paradigm.bruteForce;

public class TrappingRain {

    public static int trappingRain(int[] buildings) {
        int totalHeight = 0;

        // 리스트의 각 인덱스를 돌면서 해당 칸에 담기는 빗물의 양을 구한다.
        // 0번 인덱스의 마지막 인덱스를 볼 필요 없다.
        for (int i = 1; i < buildings.length - 1; i++) {
            // 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 높이를 구한다.
            int maxLeft = getMax(buildings, 0, i);
            int maxRight = getMax(buildings, i, buildings.length);

            // 현재 인덱스에 빗물이 담길 수 있는 높이
            int upperBound = Math.min(maxLeft, maxRight);

            // 현재 인덱스에 담기는 빗물의 양을 계산
            // 만약 upperBound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
            totalHeight += Math.max(0, upperBound - buildings[i]);
        }
        return totalHeight;
    }

    public static int getMax(int[] arr, int start, int end) {
        int max = arr[start];
        for (int i = start + 1; i < end; i++) {
            max = Math.max(max, arr[i]);
        }
        return max;
    }

    public static void main(String[] args) {
        int[] buildings1 = {3, 0, 0, 2, 0, 4};
        int[] buildings2 = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};

        System.out.println(trappingRain(buildings1));   // 10
        System.out.println(trappingRain(buildings2));   // 6
    }
}
