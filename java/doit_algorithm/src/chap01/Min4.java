package chap01;

import java.util.Scanner;

public class Min4 {
    static int min4(int a, int b, int c, int d) {
        int min = a;

        if (b < min)
            min = b;
        if (c < min)
            min = c;
        if (d < min)
            min = d;

        return min;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first number : ");
        int a = scanner.nextInt();
        System.out.print("Enter the second number : ");
        int b = scanner.nextInt();
        System.out.println("Enter the third number : ");
        int c = scanner.nextInt();
        System.out.println("Enter the fourth number : ");
        int d = scanner.nextInt();

        int min = min4(a, b, c, d);

        System.out.println("최솟값은 " + min + "입니다.");
    }
}
