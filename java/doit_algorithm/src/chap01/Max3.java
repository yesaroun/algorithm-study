package chap01;

import java.util.Scanner;

class Max3 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("세 정수의 최댓값을 구합니다.");
        System.out.print("a의 값: "); int a = stdIn.nextInt();
        System.out.print("b의 값: "); int b = stdIn.nextInt();
        System.out.print("c의 값: "); int c = stdIn.nextInt();

        int max = a;
        if (b > max) max = b;
        if (c > max) max = c;

        System.out.println("최대값은 " + max + "입니다.");

    }
}
//--==>>
/*
세 정수의 최댓값을 구합니다.
a의 값: 3
b의 값: 9
c의 값: 10
최대값은 10입니다.
*/
