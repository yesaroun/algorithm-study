// 연습 6-10
// 셀 정렬(버전1 : 요소의 이동 회수를 카운트)

package chap06;

import java.util.Scanner;

class ShellSort1Ex {
    //--- 셀 정렬(요소의 이동 회수를 반환)---//
    static int shellSort(int[] a, int n) {
        int count = 0;      // 이동 회수

        for (int h = n / 2; h > 0; h /= 2)
            for (int i = h; i < n; i++) {
                int j;
                int tmp = a[i];
                for (j = i - h; j >= 0 && a[j] > tmp; j -= h) {
                    a[j + h] = a[j];
                    count++;
                }
                a[j + h] = tmp;
                count++;
            }
        return count;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("셀 정렬");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.print("x[" + i + "] : ");
            x[i] = stdIn.nextInt();
        }

        int count = shellSort(x, nx);
        // 배열 x를 셸 정렬

        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i++)
            System.out.println("x[" + i + "] = " + x[i]);
        System.out.printf("요소의 이동 회수는 %d회입니다.", count);
    }
}
//--==>> 셀 정렬
//요솟수 : 9
//x[0] : 20
//x[1] : 30
//x[2] : 60
//x[3] : 90
//x[4] : 80
//x[5] : 10
//x[6] : 5
//x[7] : 40
//x[8] : 70
//오름차순으로 정렬했습니다.
//x[0] = 5
//x[1] = 10
//x[2] = 20
//x[3] = 30
//x[4] = 40
//x[5] = 60
//x[6] = 70
//x[7] = 80
//x[8] = 90
//요소의 이동 회수는 29회입니다.