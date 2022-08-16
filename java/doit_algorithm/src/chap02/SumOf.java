// 배열 a의 모든 요소의 합계를 구하여 반환하는 메서드를 작성하세요.
// static int sumOf(int[] a)

package chap02;

import java.util.Scanner;

public class SumOf {

    static int sumOf(int[] a) {
        int sum = 0;

        for (int i = 0; i < a.length; i++) {
            sum += a[i];
        }

        return sum;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요솟수 : ");
        int count = stdIn.nextInt();

        int[] x = new int[count];

        for (int i = 0; i<x.length; i++) {
            System.out.print("x[" + i + "] : ");
            x[i] = stdIn.nextInt();
        }

        System.out.println("모든 요소의 합계는 " + sumOf(x) + "입니다.");

    }
}
//--==>>
/*
요솟수 : 4
x[0] : 12
x[1] : 23
x[2] : 12
x[3] : 32
모든 요소의 합계는 79입니다.
 */
