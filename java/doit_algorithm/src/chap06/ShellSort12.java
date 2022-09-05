// 셀 정렬(버전 1)을 알아보기 쉽게 수정

package chap06;

import java.util.Scanner;

public class ShellSort12 {
    static void shellSort12(int[]a, int n) {
        for (int h = n/2; h > 0; h /= 2) {
            System.out.printf("%d-정렬\n", h);
            for(int i = h; i < n; i++) {
                int j;
                int tmp = a[i];

                // 확인을 위해서 i 비교 코드
                System.out.printf("a[%d]와 a[%d]비교 \n", i, i - h);

                for (j = i - h; j >= 0 && a[j] > tmp; j -= h){
                    a[j + h] = a[j];
                }
                a[j + h] = tmp;

                // 확인을 위해서 a[k]출력 코드
                for (int k = 0; k < n; k ++)
                    System.out.printf("%d ", a[k]);
                System.out.println();
            }
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("셸 정렬(버전 1)");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.print("x[" + i + "]: ");
            x[i] = stdIn.nextInt();
        }

        shellSort12(x, nx);       // 배열 x를 셸로 정렬

        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i++)
            System.out.println("x[" + i + "]= " + x[i]);
    }
}
