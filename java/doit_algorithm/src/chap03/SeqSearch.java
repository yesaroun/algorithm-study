// 선형 검색(while 문)

package chap03;

import java.util.Scanner;

public class SeqSearch {
    // 요솟수가 n인 배열 a에서 key와 값이 같은 요소를 선형 검색
    static int seqSearch(int[] a, int n, int key) {
        int i = 0;

        while (true) {
            if (i == n) {
                return -1;      // 검색 실패(-1를 반환)
            }
            if (a[i] == key) {
                return i;       // 검색 성공(인덱스를 반환)
            }
            i++;
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요솟수 : ");
        int num = stdIn.nextInt();
        int[] x = new int[num];         // 요솟수가 num인 배열

        for (int i = 0; i < num; i++) {
            System.out.print("x[" + i + "]: ");
            x[i] = stdIn.nextInt();
        }

        System.out.print("검색할 값: ");        // 키값을 받음
        int ky = stdIn.nextInt();
        int idx = seqSearch(x, num, ky);     // 배열 x에서 값이 ky인 요소를 검색

        if (idx == -1)
            System.out.println("그 값의 요소가 없습니다.");
        else
            System.out.println("그 값은 x[" + idx + "]에 있습니다.");
    }
}
//--==>>
/*
요솟수 : 5
x[0]: 23
x[1]: 21
x[2]: 54
x[3]: 26
x[4]: 12
검색할 값: 12
그 값은 x[4]에 있습니다.
 */











