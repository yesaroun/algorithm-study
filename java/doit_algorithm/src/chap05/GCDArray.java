// 배열 a의 모든 요소의 최대공약수를 구하는 다음 메서드를 작성하세요.
// static int gcdArray(int[] a)

package chap05;

import java.util.Scanner;

public class GCDArray {

    // 정수값 x, y의 최대 공약수를 비귀재적으로 구함
    static int gcd(int x, int y) {
        while (y != 0) {
            int temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }

    //--- 요솟수가 n인 배열 a의 모든 요소의 최대 공약수를 구합니다 ---//
    static int gcdArray(int[] a, int start, int no) {
        if (no == 1)
            return a[start];
        else if (no == 2)
            return gcd(a[start], a[start + 1]);
        else
            return gcd(a[start], gcdArray(a, start + 1, no - 1));
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        System.out.print("몇 개 정수의 최대 공약수를 구할까요? : ");
        int num;
        do {
            num = stdIn.nextInt();
        } while (num <= 1);

        int[] x = new int[num];

        for (int i = 0; i < num; i++) {
            System.out.print("x[" + i + "] : ");
            x[i] = stdIn.nextInt();
        }

        System.out.println("최대 공약수는 " + gcdArray(x, 0, num) + "입니다.");
    }
}
//--==>>
/*
몇 개 정수의 최대 공약수를 구할까요? : 4
x[0] : 3
x[1] : 9
x[2] : 21
x[3] : 30
최대 공약수는 3입니다.
 */