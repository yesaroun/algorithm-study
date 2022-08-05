// 지정한 개수의 기호를 중간에 줄 바꿈 없이 연속해서 보여주는 프로그램으로 +, - 기호를 번갈아 출력한다.

package chap01;

import java.util.Scanner;

public class Alternative1 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;

        System.out.println("+와 -를 번갈아 n개 출력합니다.");

        do {
            System.out.print("n값: ");
            n = stdIn.nextInt();
        } while (n <= 0);

        for (int i = 0; i < n; i++) {
            // i가 짝수인 경우 + 출력
            if(i % 2 == 0)
                System.out.print("+");
            // i가 홀수 인 경우 - 출력
            else
                System.out.print("-");
        }
    }
}
//--==>>
/*
+와 -를 번갈아 n개 출력합니다.
n값: 5
+-+-+
 */