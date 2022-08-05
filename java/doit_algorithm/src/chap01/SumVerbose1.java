// 1부터 n까지의 합과 그 값을 구하는 과정을 출력

package chap01;

import java.util.Scanner;

public class SumVerbose1 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;

        System.out.println("1부터 n까지의 합을 구합니다.");

        // n의 값이 1이상의 값인지 확인
        do {
            System.out.print("n값: ");
            n = stdIn.nextInt();
        } while (n <= 0);

        // 합
        int sum = 0;

        // 계산 과정 출력 + 합계 계산
        for (int i = 1; i <= n; i++) {
            // 중간과정
            if (i < n)
                System.out.print(i + " + ");
            // 마지막 과정
            else
                System.out.print(i + " = ");
            sum += i;
        }

        // 합계 출력
        System.out.println(sum);
    }
}
//--==>>
/*
1부터 n까지의 합을 구합니다.
n값: 5
1 + 2 + 3 + 4 + 5 = 15
 */
