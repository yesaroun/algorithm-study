// 배열을 복제

package chap02;

import java.util.Arrays;

public class CloneArray {
    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = a.clone();        // b는 a의 복제를 참조

        b[3] = 0;                   // 한 요소에만 0을 대입

        System.out.println("a = " + Arrays.toString(a));
        System.out.println("b = " + Arrays.toString(b));
    }
}
//--==>>
/*
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 0, 5]
 */
// 배열 변수 b의 참조가 배열 a의 본체 그 자체가 아니라 그 복제이다.