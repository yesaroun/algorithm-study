// 배열 요소에 값을 읽어 들여 역순으로 정렬

package chap02;

import java.util.Arrays;
import java.util.Scanner;

public class ReverseArray {

    // 배열 요소 a[idx1]과 a[idx2]의 값을 바꿈
    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    // 배열 a의 요소를 역순으로 정렬
    static void reverse(int[] a) {
        for (int i = 0; i < a.length / 2; i++) {
            swap(a, i, a.length - i - 1);
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요솟수: ");
        int num = stdIn.nextInt();

        int[] x = new int[num];

        for (int i = 0; i < num; i++) {
            System.out.print("x[" + i + "]: ");
            x[i] = stdIn.nextInt();
        }

        // 배열 a의 요소를 역순으로 정렬
        reverse(x);

        System.out.println("요소를 역순으로 정렬했습니다.");
        System.out.println("x = " + Arrays.toString(x));
    }
}
//--==>>
/*
요솟수: 3
x[0]: 5
x[1]: 3
x[2]: 1
요소를 역순으로 정렬했습니다.
x = [1, 3, 5]
 */