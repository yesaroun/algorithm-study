// 셀 버전(버전 2: h값은 ..., 40, 13, 4, 1)

package chap06;

import java.util.Scanner;

public class ShellSort2 {
    // 셀 정렬
    static void shellSort(int[] a, int n) {
        int h;
        for (h = 1; h < n; h = h * 3 + 1)
            ;
        // 이 for문은 h의 초깃값을 구한다(1부터 시작하여 값의 3배하고 1을 더하면서 n을 넘지 않는 가장 큰 값)

        for (; h > 0; h /= 3)
            for (int i = h; i < n; i++) {
                int j;
                int tmp = a[i];
                for (j = i - h; j >= 0 && a[j] > tmp; j -= h)
                    a[j + h] = a[j];
                a[j + h] = tmp;
            }
        // 버전1과 다른 점은 반복핳 때마다 h값을 3으로 나눈다. 이를 반복해 마지막에 h 값은 1이된다.
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("셀 정렬(버전 2)");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.print("x[" + i + "]: ");
            x[i] = stdIn.nextInt();
        }

        shellSort(x, nx);           // 배열 x를 셀 정렬

        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i++ )
            System.out.printf("x[$d]=%d\n", i, x[i]);
    }
}
//--==>>
/*
셀 정렬(버전 2)
요솟수 : 7
x[0]: 6
x[1]: 4
x[2]: 3
x[3]: 7
x[4]: 1
x[5]: 9
x[6]: 8
오름차순으로 정렬했습니다.
x[$d]=0
x[$d]=1
x[$d]=2
x[$d]=3
x[$d]=4
x[$d]=5
x[$d]=6
 */