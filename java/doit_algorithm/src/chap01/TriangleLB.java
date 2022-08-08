// 왼쪽 아래가 직각인 이등변삼각형을 출력

package chap01;

import java.util.Scanner;

public class TriangleLB {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;

        System.out.println("왼쪽 아래가 직각인 이등변삼각형을 출력합니다.");

        do {
            System.out.print("몇 단 삼각형입니까?: ");
            n = stdIn.nextInt();
        } while (n <= 0);
    }
}
