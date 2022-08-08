// n단의 피라미드를 출력하는 메서드를 작성하세요
// static void spira(int n)

package chap01;

import java.util.Scanner;

public class StarPira {

    static void spira(int n) {
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n - i - 1; k++) {
                System.out.print(" ");
            }
            for (int j = 0; j < (i + 1) * 2 - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;

        do {
            System.out.print("n단: ");
            n = stdIn.nextInt();
        } while (n <= 0);

        spira(n);
    }
}
//--==>>
/*
n단: 4
   *
  ***
 *****
*******
 */
