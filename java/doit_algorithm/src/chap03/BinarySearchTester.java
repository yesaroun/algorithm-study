// Arrays.binarySearch로 이진 검색

package chap03;

import java.util.Arrays;
import java.util.Scanner;

public class BinarySearchTester {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요솟수: ");
        int num = stdIn.nextInt();
        int[] x = new int[num];                     // 요솟수가 num인 배열

        System.out.println("오름차순으로 입력하세요.");

        System.out.print("x[0] : ");                 // 배열의 첫 요소를 먼저 입력받음
        x[0] = stdIn.nextInt();

        for (int i = 1; i < num; i++) {
            do {
                System.out.printf("x[%d] : ", i);
                x[i] = stdIn.nextInt();
            } while (x[i] < x [i - 1]);             // 바로 앞의 요소보다 작으면 다시 입력받음
        }

        System.out.print("검색할 값: ");              // 키 값을 입력받음
        int ky = stdIn.nextInt();

        int idx = Arrays.binarySearch(x, ky);       // 배열 x에서 값이 ky인 요소를 검색

        if (idx < 0)
            System.out.println("그 값의 요소가 없습니다.");
        else
            System.out.printf("그 값은 %d에 있습니다.", idx);
    }
}
//--==>>
/*
요솟수: 7
오름차순으로 입력하세요.
x[0] : 1
x[1] : 3
x[2] : 5
x[3] : 7
x[4] : 9
x[5] : 11
x[6] : 13
검색할 값: 11
그 값은 5에 있습니다.
 */
