// 퀵 정렬(개선한 버전)

package chap06;

import java.util.Scanner;

public class QuickSort3 {

    // 배열 요소 a[idx1]과 a[idx2]의 값을 교환
    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1]; a[idx1] = a[idx2]; a[idx2] = t;
    }

    // x[a], x[b], x[c]를 정렬(가운데 값의 인덱스를 반환)
    static int sort3elem(int[] x, int a, int b, int c) {
        if(x[b] < x[a]) swap(x, b, a);
        if(x[c] < x[b]) swap(x, c, b);
        if(x[b] < x[a]) swap(x, b, a);
        return b;
    }

    // 퀵 정렬
    static void quickSort(int[] a, int left, int right) {
        int pl = left;      // 왼쪽 커서
        int pr = right;     // 오른쪽 커서
        int m = sort3elem(a, pl, (pl + pr) / 2, pr);        // 처음, 가운데, 끝 요소를 정렬
        int x = a[m];       // 피벗

        swap(a, m, right - 1);      // 가운데 요소와 끝에서 두 번째 요소를 교환
        pl++;                             // 왼쪽 커서를 오른쪽으로 1만큼 진행
        pr -= 2;                          // 오른쪽 커서를 왼쪽으로 2만큼 징행

        do {
            while (a[pl] < x) pl++;
            while (a[pr] > x) pr--;
            if (pl <= pr)
                swap(a, pl++, pr--);
        } while (pl <= pr);

        if (left < pr) quickSort(a, left, pr);
        if (pl < right) quickSort(a, pl, right);
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("퀵 정렬");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.print("x[" + i + "]: ");
            x[i] = stdIn.nextInt();
        }

        quickSort(x, 0, nx - 1);    // 배열 x를 퀵 정렬

        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i++)
            System.out.println("x[" + i + "] = " + x[i]);
    }
}
//--==>>
/*
퀵 정렬
요솟수 : 7
x[0]: 4
x[1]: 9
x[2]: 7
x[3]: 2
x[4]: 1
x[5]: 3
x[6]: 5
오름차순으로 정렬했습니다.
x[0] = 1
x[1] = 2
x[2] = 3
x[3] = 4
x[4] = 5
x[5] = 7
x[6] = 9
 */