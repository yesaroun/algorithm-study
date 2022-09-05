// 요소의 이동 횟수를 계산하도록 버전 1을 수정한 프로그램을 작성하시오.

package chap06;

import java.util.Scanner;

public class ShellSortEx1 {
    // 셀 정렬
    static int shellSort(int[] a, int n) {
        int count = 0;
        for (int h = n / 2; h > 0; h /= 2)
            for (int i = h; i < n; i++) {
                int j;
                int tmp = a[i];
                for (j = i - h; j >= 0 && a[j] > tmp; i -= h)
                    a[j + h] = a[j];
                    count += 1;
                a[j + h] = tmp;
            }
        return count;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("셀 정렬(버전1)");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for(int i = 0; i < nx; i++) {
            System.out.printf("x[%d]: ", i);
            x[i] = stdIn.nextInt();
        }

        int result = shellSort(x, nx);       // 배열 x를 셀 정렬

        System.out.printf("%d회 이동하였습니다.\n", result);
        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i++)
            System.out.printf("x[%d]=%d\n", i , x[i]);
    }
}
