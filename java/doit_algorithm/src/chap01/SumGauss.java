package chap01;

// 1~10의 합은 (1 + 10) * 5와 같이 구할 수 있습니다.
// 이를 '가우스의 덧셈'이라고 하는데 이 방법을 이용하여 1부터 n까지의 정수 합을 구하는 프로그램을 작성하세요.

import java.util.Scanner;

public class SumGauss {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("1부터 n까지의 합을 구하는 프로그램");
        System.out.print("n의 값 : ");
        int n = scanner.nextInt();

        // 내 풀이
        /*
        int total = 0;
        // 계산식
        if (n % 2 == 1) {
            total = (1 + n) * (n/2) + (n/2)+1;
        } else {
            total = (1 + n) * (n/2);
        }
        */

        int total = (1 + n) * (n / 2) + (n % 2 == 1 ? (1 + n) / 2 : 0);

        System.out.printf("1부터 %d까지의 합은 %d입니다.\n", n, total);
    }
}
