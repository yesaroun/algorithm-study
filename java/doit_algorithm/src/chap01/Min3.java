package chap01;

import java.util.Scanner;

public class Min3{

    static int min3(int a, int b, int c){
        int min = a;

        if (min > b)
            min = b;
        if (min > c)
            min = c;

        return min;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("first int : ");
        int a = scanner.nextInt();
        System.out.print("second int : ");
        int b = scanner.nextInt();
        System.out.print("third int : ");
        int c = scanner.nextInt();

        int min = min3(a, b, c);

        System.out.println("최솟값은 " + min + "입니다.");
    }
}
