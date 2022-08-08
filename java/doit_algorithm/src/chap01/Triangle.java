// 직각이등변삼각형을 출력하는 부분을 아래와 같은 형식의 메서드로 작성하세요.
// static void triangleLB(int n)
// 또 왼쪽 위, 오른쪽 위, 오른쪽 아래가 직각인 이등변 삼각형을 출력하는 메서드를 각각 작성하세요.
/*
static void triangleLU(int n)
static void triangleRU(int n)
static void triangleRB(int n)
 */

package chap01;

import java.util.Scanner;

public class Triangle {

    static void triangleLB(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i+1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    static void triangleLU(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    static void triangleRU(int n) {
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < i; k++) {
                System.out.print(" ");
            }
            for (int j = 0; j < n - i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }

    static void triangleRB(int n) {
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n - i - 1; k++) {
                System.out.print(" ");
            }
            for (int j = 0; j < i+1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;

        do {
            System.out.print("n의 값: ");
            n = stdIn.nextInt();
        } while (n <= 0);

        System.out.println("왼쪽 아래 직각삼각형");
        triangleLB(n);			// 왼쪽 아래가 직각인 직각삼각형

        System.out.println("왼쪽 위 직각삼각형");
        triangleLU(n);			// 왼쪽 위가 직각인 직각삼각형

        System.out.println("오른쪽 위 직각삼각형");
        triangleRU(n);			// 오른쪽 위가 직각인 직각삼각형

        System.out.println("오른쪽 아래 직각삼각형");
        triangleRB(n);			// 오른쪽 아래가 직각인 직각삼각형
    }
}
//--==>>
/*
n의 값: 4
왼쪽 아래 직각삼각형
*
**
***
****
왼쪽 위 직각삼각형
****
***
**
*
오른쪽 위 직각삼각형
****
 ***
  **
   *
오른쪽 아래 직각삼각형
   *
  **
 ***
****
 */
