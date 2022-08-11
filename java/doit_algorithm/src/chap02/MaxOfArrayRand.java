package chap02;

import java.util.Random;
import java.util.Scanner;

public class MaxOfArrayRand {

    // 배열 a의 최댓값을 구하여 반환
    static int maxOf(int[] a) {
        int max = a[0];
        for (int i = 1; i < a.length; i++){
            if (a[i] > max) {
                max = a[i];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        Random rand = new Random();
        Scanner stdIn = new Scanner(System.in);

        System.out.println("키의 최댓값을 구합니다.");
        System.out.print("사람 수: ");
        // 배열의 요소수를 입력받음
        int num = stdIn.nextInt();

        // 요솟수가 num인 배열을 생성
        int[] height = new int[num];

        System.out.println("킷값은 아래와 같습니다.");
        for (int i = 0; i < num; i++) {
            height[i] = 100 + rand.nextInt(90);
            System.out.println("height[" + i + "]: " + height[i]);
        }

        System.out.println("최댓값은 " + maxOf(height) + "입니다.");
    }
}
//--==>>
/*
키의 최댓값을 구합니다.
사람 수: 5
킷값은 아래와 같습니다.
height[0]: 176
height[1]: 114
height[2]: 149
height[3]: 144
height[4]: 121
최댓값은 176입니다.
 */
