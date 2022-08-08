package chap01;

import java.util.Scanner;

public class Max4 {
    static int max4(int a, int b, int c, int d){
        int max = a;

        if (b > max)
            max = b;
        if (c > max)
            max = c;
        if (d > max)
            max = d;

        return max;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("첫 번째 정수 입력 : ");
        int a = scanner.nextInt();
        System.out.print("두 번째 정수 입력 : ");
        int b = scanner.nextInt();
        System.out.print("세 번째 정수 입력 : ");
        int c = scanner.nextInt();
        System.out.print("네 번째 정수 입력 : ");
        int d = scanner.nextInt();

        int max = max4(a, b, c, d);

        System.out.println("최댓값은 " + max + "입니다.");
    }
}
//--==>>
/*
첫 번째 정수 입력 : 34
두 번째 정수 입력 : 23
세 번째 정수 입력 : 54
네 번째 정수 입력 : 76
최댓값은 76입니다.
*/
