package chap01;

// 정수 a,b를 포함하여 그 사이의 모든 정수의합을 구하여 반환하는 메서드를 작성하세요.
// static int sumof(int a, int b)

import java.util.Scanner;

public class SumOf {

    static int sumof(int a, int b) {

        int total = 0;

        // b를 큰 수로 지정
        if (a > b){
            int temp = a;
            a = b;
            b = temp;
        }

        // 가우스의 덧셈 활용
        /*
        if ((b - a) % 2 == 1) {
            total = (a + b) * ((b - a + 1) / 2);
        } else {
            total = (a + b) * ((b - a) / 2) + ((a + b) / 2);
        }
        */

        for (int i = a; i <= b; i++) {
            total += i;
        }

        return total;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("a부터 b까지의 합을 구합니다.");
        System.out.print("a의 값: ");
        int a = stdIn.nextInt();
        System.out.print("b의 값: ");
        int b = stdIn.nextInt();

        int total = sumof(a, b);

        System.out.printf("%d 부터 %d까지의 합은 %d입니다.\n", a, b, total);
    }
}
//--==>>
/*
a부터 b까지의 합을 구합니다.
a의 값: 12
b의 값: 5
12 부터 5까지의 합은 68입니다.
(계산(합)은 문제 없이 되나 작은 수(5)가 a의 위치에서 출력되도록 수정해야함)
*/