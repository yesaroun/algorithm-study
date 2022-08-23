// 실습5-1(Factorial)의 factorial 메서드를 재귀 메서드 호출을 사용하지 말고 작성하세요
// 팩토리얼 값을 구함

package chap05;

import java.util.Scanner;

public class FactorialEx {
    // 음이 아닌 정수 n의 팩토리얼값을 반환
    static int factorial(int n) {
        if(n > 0) {
            int result = 1;
            for (int i = 1; i <= n; i++) {
                result *= i;
            }
            return result;
        } else
            return 1;
    }

    /*      이 방식이 더 좋다고 생각
    //--- 음이 아닌 정숫값 n의 팩토리얼 값을 반환 ---//
	static int factorial(int n) {
		int fact = 1;

		while (n > 1)
			fact *= n--;
		return fact;
	}
     */

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("정수를 입력하세요: ");
        int x = stdIn.nextInt();

        System.out.println(x + "의 팩토리얼은 " + factorial(x) + "입니다.");
    }
}
//--==>>
/*
정수를 입력하세요: 15
15의 팩토리얼은 2004310016입니다.
 */
