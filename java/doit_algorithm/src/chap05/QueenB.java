// 각 열에 퀸 1개를 배치하는 조합을 재귀적으로 나열

package chap05;

public class QueenB {
    static int[] pos = new int[8];      // 각 열에 있는 퀸의 위치

    // 각 열에 있는 퀸의 위치를 출력
    static void print() {
        for (int i = 0; i < 8; i++)
            System.out.printf("%2d", pos[i]);
        System.out.println();
    }

    // i열에 퀸을 배치
    static void set(int i) {            // i는 열
        for (int j = 0; j < 8; j++) {   // j는 행
            pos[i] = j;                 // 퀸을 j행에 배치
            if(i == 7)                  // 모든 열에 배치
                print();
            else
                set(i + 1);             // 다음 열에 퀸을 배치
        }
    }

    public static void main(String[] args) {
        set(0);                         // 0열에 퀸을 배치
    }
}
//--==>>
/*
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 2
(... 생략 ...)
7 7 7 7 7 7 7 7
 */