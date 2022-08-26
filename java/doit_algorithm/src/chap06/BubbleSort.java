// 버블 정렬(버전 1)

package chap06;

import java.util.Scanner;

public class BubbleSort {
    //a[idx1]과 a[idx2]의 값을 교환
    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    // 버블 정렬
    static void bubbleSort(int[] a, int n) {
        for (int i = 0; i < n - 1; i++)
            for (int j = n - 1; j > i; j--)
                if (a[j - 1] > a[j])
                    swap(a, j - 1, j);
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("버즐 정렬(버전 1)");
        System.out.print("요솟수: ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.printf("x[%d] : ", i);
            x[i] = stdIn.nextInt();
        }

        bubbleSort(x, nx);      // 배열 x를 버블 정렬

        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i++)
            System.out.printf("x[%d] = %d\n", i, x[i]);
    }
}
//--==>>
/*
버즐 정렬(버전 1)
요솟수: 5
x[0] : 10
x[1] : 40
x[2] : 50
x[3] : 20
x[4] : 30
오름차순으로 정렬했습니다.
x[0] = 10
x[1] = 20
x[2] = 30
x[3] = 40
x[4] = 50
 */