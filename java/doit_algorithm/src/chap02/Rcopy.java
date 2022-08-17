// 배열 b의 모든 요소를 배열 a에 역순으로 복사하는 메서드 rcopy를 작성하세요.
// static void rcopy(int[] a, int[] b)

package chap02;

import java.util.Scanner;

public class Rcopy {
    static void rcopy(int[] a, int[] b) {
        int num = a.length <= b.length ? a.length : b.length;
        for (int i = 0; i < num; i++) {
            a[i] = b[b.length - i - 1];
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("a의 요솟수는 : ");
        int numa = stdIn.nextInt();
        int[] a = new int[numa];

        for (int i = 0; i < numa; i++) {
            System.out.printf("a[%d] : ", i);
            a[i] = stdIn.nextInt();
        }

        System.out.print("b의 요솟수는 : ");
        int numb = stdIn.nextInt();
        int[] b = new int[numb];

        for (int i = 0; i < numb; i++) {
            System.out.printf("b[%d] : ", i);
            b[i] = stdIn.nextInt();
        }

        rcopy(a, b);

        System.out.println("배열 b의 모든 요소를 배열 a에 역순으로 copy 하였습니다.");
        for (int i = 0; i < numa; i++)
            System.out.println("a[" + i + "] = " + a[i]);
    }
}
//--==>>
/*
a의 요솟수는 : 3
a[0] : 1
a[1] : 2
a[2] : 3
b의 요솟수는 : 4
b[0] : 4
b[1] : 8
b[2] : 12
b[3] : 16
배열 b의 모든 요소를 배열 a에 역순으로 copy 하였습니다.
a[0] = 16
a[1] = 12
a[2] = 8
 */