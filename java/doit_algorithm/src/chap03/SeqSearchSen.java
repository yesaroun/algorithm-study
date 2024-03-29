// 선형 검색(보초법)

package chap03;

import java.util.Scanner;

public class SeqSearchSen {
    // 요솟수가 n인 배열 a에서 key와 값이 같은 요소를 보초법으로 선형 검색
    static int seqSearchSen(int[] a, int n, int key) {
        int i = 0;

        a[n] = key;             // 보초를 추가

        while (true) {
            if (a[i] == key)    // 검색 성공
                break;
            i++;
        }
        return i == n ? -1 : i;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요솟수: ");
        int num = stdIn.nextInt();
        int[] x = new int[num + 1];     // 요솟수가 num+1인 배열

        for (int i = 0; i < num; i++) {
            System.out.printf("x[%d] : ", i);
            x[i] = stdIn.nextInt();
        }

        System.out.print("검색할 값: ");   // 키 값을 입력받음
        int ky = stdIn.nextInt();

        int idx = seqSearchSen(x, num, ky); // 배열 x에서 값이 ky인 요소를 검색

        if (idx == -1)
            System.out.println("그 값의 요소가 없습니다.");
        else
            System.out.printf("그 값은 x[%d]에 있습니다.\n", idx);
    }
}
//--==>>
/*
요솟수: 4
x[0] : 1
x[1] : 2
x[2] : 3
x[3] : 4
검색할 값: 3
그 값은 x[2]에 있습니다.
 */
