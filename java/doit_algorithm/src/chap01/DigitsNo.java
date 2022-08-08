// 양의 정수를 입력하고 자릿수를 출력한느 프로그램을 작성하세요.
// 예를 들어 135를 입력하면 '그 수는 3자리 입니다.'라고 출력합니다.

package chap01;

import java.util.Scanner;

public class DigitsNo {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int num = 0;
        int count = 0;

        do {
            System.out.print("숫자를 입력하세요 : ");
            num = stdIn.nextInt();
        } while (num <= 0);

        for (int i = 1; i < num; i *= 10 ) {
            count++;
        }
        // 다른 방식
        /*
        while (n > 0) {
			n /= 10;         // n을 10으로 나눕니다
			no++;
		}
         */

        System.out.printf("그 수는 %d자리 입니다.", count);
    }
}
//--==>>
/*
숫자를 입력하세요 : -4
숫자를 입력하세요 : 5
그 수는 1자리 입니다.
*/
