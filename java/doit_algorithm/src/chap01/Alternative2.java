package chap01;

import java.util.Scanner;

public class Alternative2 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;

        System.out.println("+와 -를 번갈아 n개 출력합니다.");

        do {
            System.out.print("n값: ");
            n = stdIn.nextInt();
        } while (n <= 0);

        for (int i = 0; i < n / 2; i++)
            System.out.print("+-");

        // n이 홀수인 경우
        if (n % 2 != 0)
            System.out.print("+");
    }
}
//--==>>
/*
+와 -를 번갈아 n개 출력합니다.
n값: 7
+-+-+-+
 */