// Arrays.sort 메서드를 사용하여 정렬(퀵 정렬)

package chap06;

import java.util.Arrays;
import java.util.Scanner;

public class ArraysSortTester {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요솟수 : ");
        int num = stdIn.nextInt();
        int[] x = new int[num];     // 길이가 num인 배열

        for (int i = 0; i < num; i++) {
            System.out.printf("x[%d]: ", i);
            x[i] = stdIn.nextInt();
        }

        Arrays.sort(x);     // 배열 x를 정렬

        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < num; i++)
            System.out.printf("x[%d] = %d\n", i, x[i]);
    }
}
//--==>>
/*
요솟수 : 5
x[0]: 10
x[1]: 50
x[2]: 40
x[3]: 30
x[4]: 20
오름차순으로 정렬했습니다.
x[0] = 10
x[1] = 20
x[2] = 30
x[3] = 40
x[4] = 50
 */