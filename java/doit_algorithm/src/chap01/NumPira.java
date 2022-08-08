// 아래를 향한 n단의 숫자 피라미드를 출력하는 메서드를 작성하세요.
// static void npira(int n)

package chap01;

import java.util.Scanner;

public class NumPira {

    static void npira(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= (i) * 2 - 1; k++) {
                System.out.print(i);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;

        do {
            System.out.print("n단 : ");
            n = stdIn.nextInt();
        } while (n < 0);

        npira(n);
    }
}
//--==>>
/*
n단 : 5
     1
    222
   33333
  4444444
 555555555
 */