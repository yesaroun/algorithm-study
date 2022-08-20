// 팩토리얼 값을 재귀적으로 구함

package chap05;

import java.util.Scanner;

public class Factorial2 {
    // 음이 아닌 정수 n의 팩토리얼값을 반환
    static int factorial(int n) {
        return (n > 0) ? n * factorial(n - 1) : 1;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("정수를 입력하세요: ");
        int num = stdIn.nextInt();

        System.out.printf("%d의 팩토리얼은 %d입니다.", num, factorial(num));
    }
}
//--==>>
/*
정수를 입력하세요: 5
5의 팩토리얼은 120입니다.
*/