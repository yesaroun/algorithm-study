// 배열 요소를 역순으로 정렬하는 과정을 하나 하나 나타내는 프로그램을 작성하세요.

package chap02;

import java.util.Arrays;
import java.util.Scanner;

public class ReverseArrayEx {

    // 배열 요소 교환
    static void swap(int[] a, int idx1, int idx2) {
        int temp = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = temp;
    }

    // 배열 a를 역순으로 정렬
    static void reverse(int[] a) {
        System.out.println(Arrays.toString(a));
        for (int i = 0; i < a.length / 2; i++ ) {
            System.out.println("a[" + i + "]과 a[" + (a.length - i - 1) + "]를 교환합니다.");
            swap(a, i, a.length - i - 1);
            System.out.println(Arrays.toString(a));
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요솟수를 입력하세요 : ");
        int num = stdIn.nextInt();

        int[] x = new int[num];

        for (int i = 0; i < num; i++) {
            System.out.print("x[" + i + "] = ");
            x[i] = stdIn.nextInt();
        }

        reverse(x);

        System.out.println("역순 정렬을 마쳤습니다.");
    }
}
//--==>>
/*
요솟수를 입력하세요 : 5
x[0] = 12
x[1] = 65
x[2] = 3
x[3] = 53
x[4] = 43
[12, 65, 3, 53, 43]
a[0]과 a[4]를 교환합니다.
[43, 65, 3, 53, 12]
a[1]과 a[3]를 교환합니다.
[43, 53, 3, 65, 12]
역순 정렬을 마쳤습니다.
 */
