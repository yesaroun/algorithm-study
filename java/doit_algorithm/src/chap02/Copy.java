// 배열 b의 모든 요소를 배열 a에 복사하는 메서드 copy를 작성하세요.
// static void copy(int[] a, int[] b)

package chap02;

import java.util.Scanner;

public class Copy {

    // 배열 b의 요소를 배열 a에 복사
    static void copy(int[] a, int[] b) {
        int num = a.length <= b.length ? a.length : b.length;
        for (int i = 0; i < num; i++) {
            a[i] = b[i];
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("a의 요솟수는 : ");
        int numa = stdIn.nextInt();
        int[] a = new int[numa];
        for (int i = 0; i < numa; i++) {
            System.out.print("a[" + i + "] : ");
            a[i] = stdIn.nextInt();
        }

        System.out.print("b의 요솟수는 : ");
        int numb = stdIn.nextInt();
        int[] b = new int[numb];
        for (int i = 0; i <numb; i++) {
            System.out.print("b[" + i + "] : ");
            b[i] = stdIn.nextInt();
        }

        copy(a, b);

        System.out.println("배열 b의 모든 요소를 배열 a에 copy 하였습니다.");
        for (int i = 0; i < numa; i++) {
            System.out.println("a[" + i + "] = " + a[i]);
        }
    }
}
//--==>>
/*
a의 요솟수는 : 5
a[0] : 1
a[1] : 2
a[2] : 3
a[3] : 4
a[4] : 5
b의 요솟수는 : 4
b[0] : 4
b[1] : 8
b[2] : 12
b[3] : 16
배열 b의 모든 요소를 배열 a에 copy 하였습니다.
a[0] = 4
a[1] = 8
a[2] = 12
a[3] = 16
a[4] = 5
 */