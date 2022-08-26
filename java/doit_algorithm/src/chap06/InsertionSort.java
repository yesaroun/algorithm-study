// 단순 삽입 정렬

package chap06;

import java.util.Scanner;

public class InsertionSort {
    // 단순 삽입 정렬
    static void insertionSort(int[] a, int n) {
        for (int i = 1; i < n; i++) {
            int j;
            int tmp = a[i];
            for (j = 1; j > 0 && a[j - 1] > tmp; j--)
                a[j] = a[j - 1];
            a[j] = tmp;
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("단순 삽입 정렬");
        System.out.print("요솟수: ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i ++) {
            System.out.printf("x[%d] : ", i);
            x[i] = stdIn.nextInt();
        }

        insertionSort(x, nx);               // 배열 x를 단순 삽입 정렬

        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i ++)
            System.out.printf("x[%d] = %d\n", i, x[i]);
    }
}
//--==>>
/*
단순 삽입 정렬
요솟수: 6
x[0] : 2
x[1] : 3
x[2] : 1
x[3] : 6
x[4] : 5
x[5] : 4
오름차순으로 정렬했습니다.
x[0] = 1
x[1] = 4
x[2] = 1
x[3] = 6
x[4] = 5
x[5] = 4
 */