// 버블 정렬(버전 3: 교환 횟수에 따른 멈춤)
package chap06;

import java.util.Scanner;

public class BubbleSort3 {
    // 배열 요소 a[idx1]와 a[idx2]의 값을 교환
    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];    a[idx1] = a[idx2];  a[idx2] = t;
    }

    // 버블 정렬(버전 3: 스캔 범위를 한정)
    static void bubbleSort(int[] a, int n) {
        int k = 0;                  // a[k]보다 앞쪽으 정렬을 마침
        while (k < n - 1) {
            int last = n - 1;       // 마지막으로 교환한 위치
            for (int j = n - 1; j > k; j--)
                if (a[j - 1] > a[j]) {
                    swap(a, j - 1, j);
                    last = j;
                }
            k = last;
        }
    }
}
