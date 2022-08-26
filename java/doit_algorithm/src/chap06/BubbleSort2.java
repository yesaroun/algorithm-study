// 버블 환정렬(버전 2: 교환 횟수에 따른 멈춤)

package chap06;

import java.util.Scanner;

public class BubbleSort2 {
    // 배열 요소 a[idx1]와 a[idx2]의 값을 교환
    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1]; a[idx1] = a[idx2]; a[idx2] = t;
    }

    // 단순교환정렬(버전 2 : 교환 횟수에 따른 멈춤)
    static void bubbleSort(int[] a, int n) {
        for (int i = 0; i < n - 1; i++) {
            int exchg = 0;                  // 패스에서 교환하는 횟수
            for (int j = n - 1; j > i; j--)
                if (a[j - 1] > a[j]) {
                    swap(a, j - 1, j);
                    exchg++;
                }
            if (exchg == 0) break;          // 교환이 이루어지지 않으면 멈춤
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("버블 정렬");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.printf("x[%d]: ", i);
            x[i] = stdIn.nextInt();
        }

        bubbleSort(x, nx);              // 배열 x를 단순교환 정렬

        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i++)
            System.out.printf("x[%d]=%d\n", i, x[i]);
    }
}
//--==>>
/*
요솟수 : 5
x[0]: 20
x[1]: 30
x[2]: 10
x[3]: 40
x[4]: 50
오름차순으로 정렬했습니다.
x[0]=10
x[1]=20
x[2]=30
x[3]=40
x[4]=50
 */