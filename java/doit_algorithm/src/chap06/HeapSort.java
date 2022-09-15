// 힙 정렬

package chap06;

import java.util.Scanner;

public class HeapSort {
    // 배열 요소 a[idx1]과 a[idx2]의 값을 교환
    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    // a[left]~a[right]를 힙으로 만듬
    static void downHeap(int[] a, int left, int right) {
        int temp = a[left];         // 루트
        int child;                  // 큰값을 갖는 자식
        int parent;                 // 부모

        for (parent = left; parent < (right + 1) / 2; parent = child) {
            int cl = parent * 2 + 1;        // 왼쪽 자식
            int cr = cl + 1;                // 오른쪽 자식
            child = (cr <= right && a[cr] > a[cl]) ? cr : cl;   // 큰쪽을 자식에 대입
            if (temp >= a[child])
                break;
            a[parent] = a[child];
        }
        a[parent] = temp;
    }

    // 힙 정렬
    static void heaSort(int[] a, int n) {
        for (int i = (n - 1) / 2; i >= 0; i--)      // a[i]~a[n-1]을 힙으로 만듬
            downHeap(a, i, n - 1);
        for (int i = n - 1; i > 0; i--) {
            swap(a, 0, i);  // 가장 큰 요소와 아직 정렬되지 않은 부분의 마지막 요소를 교환
            downHeap(a, 0, i - 1);  // a[0]~a[i-1]을 힙으로 만듬
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("힙 정렬");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.print("x[" + i + "]: ");
            x[i] = stdIn.nextInt();
        }

        heaSort(x, nx); // 배열 x를 힙 정렬

        System.out.println("오름차순으로 정렬합니다.");
        for (int i = 0; i < nx; i++)
            System.out.println("x[" + i + "] = " + x[i]);
    }
}
//--==>>
/*
힙 정렬
요솟수 : 7
x[0]: 6
x[1]: 4
x[2]: 3
x[3]: 7
x[4]: 1
x[5]: 9
x[6]: 8
오름차순으로 정렬합니다.
x[0] = 1
x[1] = 3
x[2] = 4
x[3] = 6
x[4] = 7
x[5] = 8
x[6] = 9
 */