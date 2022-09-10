// 연습 6-11
// 퀵 정렬(비재귀 버전 : 스특에 푸시 팝하는 과정을 출력)

package chap06;

import java.util.Scanner;

public class QuickSort2Verbose {

    // 배열의 요소 a[idx1]과 a[idx2]를 교환
    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1]; a[idx1] = a[idx2]; a[idx2] = t;
    }

    // 퀵 정렬(비재귀 버전)
    static void quickSort(int[] a, int left, int right) {
        IntStack lstack = new IntStack(right - left + 1);
        IntStack rstack = new IntStack(right - left + 1);

        lstack.push(left);
        rstack.push(right);
        System.out.printf("a[%d]~a[%d]을 나누는 문제를 스택에 푸시합니다.\n", left, right);
        System.out.print("Lstack:");    lstack.dump();
        System.out.print("Rstack:");    rstack.dump();

        while (lstack.isEmpty() != true) {
            int pl = left = lstack.pop();
            // 왼쪽 커서
            int pr = right = rstack.pop();
            // 오른쪽 커서
            int x = a[(left + right) / 2];
            // 피벗은 가운데 요소
            System.out.printf("스택에서 나누는 문제를 꺼냈습니다. a[%d]~a[%d]을 나눕니다.\n", left, right);

            do {
                while (a[pl] < x) pl++;
                while (a[pr] > x) pr--;
                if (pl <= pr)
                    swap(a, pl++, pr--);
            } while (pl <= pr);

            if (left < pr) {
                lstack.push(left);
                // 왼쪽 그룹의 범위의
                rstack.push(pr);
                // 인덱스를 푸시
                System.out.printf("a[%d]~a[%d]을 나누는 문제를 스택에 푸시합니다. \n", left, pr);
                System.out.print("Lstack:");    lstack.dump();
                System.out.print("Rstack:");    rstack.dump();
            }
            if (pl < right) {
                lstack.push(pl);
                // 오른쪽 그룹 범위의
                rstack.push(right);
                // 인덱스를 푸시
                System.out.printf("a[%d]~a[%d]을 나누는 문제를 스택에 푸시합니다. \n", left, pr);
                System.out.print("Lstack:");    lstack.dump();
                System.out.print("Rstack:");    rstack.dump();
            }
        }
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
요솟수 : 10
x[0]: 50
x[1]: 10
x[2]: 60
x[3]: 70
x[4]: 20
x[5]: 30
x[6]: 80
x[7]: 90
x[8]: 40
x[9]: 100
a[0]~a[9]을 나누는 문제를 스택에 푸시합니다.
Lstack:0
Rstack:9
스택에서 나누는 문제를 꺼냈습니다. a[0]~a[9]을 나눕니다.
a[0]~a[1]을 나누는 문제를 스택에 푸시합니다.
Lstack:0
Rstack:1
a[0]~a[1]을 나누는 문제를 스택에 푸시합니다.
Lstack:0 2
Rstack:1 9
스택에서 나누는 문제를 꺼냈습니다. a[2]~a[9]을 나눕니다.
a[2]~a[2]을 나누는 문제를 스택에 푸시합니다.
Lstack:0 3
Rstack:1 9
스택에서 나누는 문제를 꺼냈습니다. a[3]~a[9]을 나눕니다.
a[3]~a[6]을 나누는 문제를 스택에 푸시합니다.
Lstack:0 3
Rstack:1 6
a[3]~a[6]을 나누는 문제를 스택에 푸시합니다.
Lstack:0 3 7
Rstack:1 6 9
스택에서 나누는 문제를 꺼냈습니다. a[7]~a[9]을 나눕니다.
a[7]~a[7]을 나누는 문제를 스택에 푸시합니다.
Lstack:0 3 8
Rstack:1 6 9
스택에서 나누는 문제를 꺼냈습니다. a[8]~a[9]을 나눕니다.
스택에서 나누는 문제를 꺼냈습니다. a[3]~a[6]을 나눕니다.
a[3]~a[3]을 나누는 문제를 스택에 푸시합니다.
Lstack:0 5
Rstack:1 6
스택에서 나누는 문제를 꺼냈습니다. a[5]~a[6]을 나눕니다.
스택에서 나누는 문제를 꺼냈습니다. a[0]~a[1]을 나눕니다.
오름차순으로 정렬했습니다.
x[0] = 10
x[1] = 20
x[2] = 30
x[3] = 40
x[4] = 50
x[5] = 60
x[6] = 70
x[7] = 80
x[8] = 90
x[9] = 100
 */