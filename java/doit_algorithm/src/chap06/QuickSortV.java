// 퀵 정렬(배열의 분활 과정을 표시)

package chap06;

import java.util.Scanner;

public class QuickSortV {
    // 배열 요소 a[idx1]와 a[idx2]의 값을 교환
    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1]; a[idx1] = a[idx2]; a[idx2] = t;
    }

    // 퀵 정렬(배열의 분할 과정을 표시)
    static void quickSort(int[] a, int left, int right) {
        int pl = left;                  // 왼쪽 커서
        int pr = right;                 // 오른쪽 커서
        int x = a[(pl + pr) / 2];       // 피벗

        System.out.printf("a[%d]~a[%d] : {", left, right);
        for (int i = left; i < right; i++)
            System.out.printf("%d , ", a[i]);
        System.out.printf("%d}\n", a[right]);

        do {
            while (a[pl] < x) pl++;
            while (a[pr] > x) pr--;
            if (pl <= pr)
                swap(a, pl++, pr--);
        } while (pl <= pr);

        if (left < pr)  quickSort(a, left, pr);
        if (pl < right) quickSort(a, pl, right);
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("퀵 정렬");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.print("x[" + i + "] : ");
            x[i] = stdIn.nextInt();
        }

        quickSort(x, 0, nx - 1);    // 배열 x를 퀵 정렬

        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i++)
            System.out.println("x[" + i + "]=" + x[i]);
    }
}
//--==>>
/*
퀵 정렬
요솟수 : 9
x[0] : 90
x[1] : 50
x[2] : 10
x[3] : 80
x[4] : 70
x[5] : 20
x[6] : 30
x[7] : 40
x[8] : 60
a[0]~a[8] : {90 , 50 , 10 , 80 , 70 , 20 , 30 , 40 , 60}
a[0]~a[5] : {60 , 50 , 10 , 40 , 30 , 20}
a[1]~a[5] : {50 , 60 , 40 , 30 , 20}
a[1]~a[2] : {20 , 30}
a[4]~a[5] : {60 , 50}
a[6]~a[8] : {70 , 80 , 90}
오름차순으로 정렬했습니다.
x[0]=10
x[1]=20
x[2]=30
x[3]=40
x[4]=50
x[5]=60
x[6]=70
x[7]=80
x[8]=90
 */