// 배열을 나눔

package chap06;

import java.util.Scanner;

public class Partition {
    // 비열 요소 a[idx1]과 a[idx2]의 값을 교환
    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    // 배열을 나눔
    static void partition(int[] a, int n) {
        int pl = 0;         // 왼쪽 커서
        int pr = n - 1;     // 오른쪽 커서
        int x = a[n / 2];   // 피벗(가운데 요소)

        do {
            while (a[pl] < x) pl++;
            while (a[pr] > x) pr--;
            if (pl <= pr)
                swap(a, pl++, pr--);
        } while (pl <= pr);

        System.out.printf("피벗값은 %d입니다.", x);

        System.out.println("피벗 이하의 그룹");
        for (int i = 0; i <= pl - 1; i++)           // a[0]~a[pl - 1]
            System.out.print(a[i] + " ");
        System.out.println();

        if (pl > pr + 1) {
            System.out.println("피벗과 같은 그룹");
            for (int i = pr + 1; i <= pl - 1; i++)  // a[pr + 1]~a[pl - 1]
                System.out.print(a[i] + " ");
            System.out.println();
        }

        System.out.println("피벗 이상의 그룹");
        for (int i = pr + 1; i < n; i++)            // a[pr + 1]~a[n - 1]
            System.out.print(a[i] + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("배열을 나눕니다.");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.print("x[" + i + "]: ");
            x[i] = stdIn.nextInt();
        }
        partition(x, nx);       // 배열 x를 나눔
    }
}
//--==>>
/*
배열을 나눕니다.
요솟수 : 7
x[0]: 9
x[1]: 2
x[2]: 3
x[3]: 7
x[4]: 5
x[5]: 9
x[6]: 3
피벗값은 7입니다.피벗 이하의 그룹
3 2 3 5
피벗 이상의 그룹
7 9 9
 */