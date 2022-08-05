// 두 변수 a, b에 정수를 입력하고 b - a를 출력하는 프로그램을 작성하세요.
// 단, 변수 b에 입력한 값이 a값 이하이면 변수 b값을 다시 입력하세요.

package chap01;

import java.util.Scanner;

public class Difference {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("a값: ");
        int a = stdIn.nextInt();
        int b = 0;

        do {
            System.out.print("b값: ");
            b = stdIn.nextInt();

            if (a > b) {
                System.out.println("a보다 큰 값을 입력하세요!");
            }
        } while (a > b);
        // 다른 방식
        /*
        while (true) {
			System.out.print("b의 값 : ");
			b = stdIn.nextInt();
			if (b > a) break;
			System.out.println("a보다 큰 값을 입력하세요!");
		}
        */

        System.out.printf("b - a 값은 %d입니다.", b-a);
    }
}
