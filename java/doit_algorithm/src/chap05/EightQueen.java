// 8퀸 문제 풀이

package chap05;

public class EightQueen {
    static boolean[] flag_a = new boolean[8];       // 각 행에 퀸을 배치했는지 체크
    static boolean[] flag_b = new boolean[15];      // / 대각선 방향으로 퀸을 배치했는지 체크
    static boolean[] flag_c = new boolean[15];      // \ 대각선 방향으로 퀸을 배치했는지 체크
    static int[] pos = new int[8];                  // 각 열에 있는 퀸의 위치

    // 각 열에 있는 퀸의 위치를 출력
    static void print() {
        for (int i = 0; i < 8; i++)
            System.out.printf("%2d", pos[i]);
        System.out.println();
    }

    // i 열의 알맞은 위치에 퀸을 배치
    static void set(int i) {
        for (int j = 0; j < 8; j++) {
            if (flag_a[j] == false &&           // 가로(j행)에 아직 배치하지 않음
                flag_b[i + j] == false &&       // / 대각선에 아직 배치하지 않음
                flag_c[i - j + 7] == false) {   // \ 대각선에 아직 배치하지 않음
                pos[i] = j;                     // 퀸을 j행에 배치
                if (i == 7)                     // 모든 열에 배치
                    print();
                else {
                    flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = true;
                    set(i + 1);
                    flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = false;
                }
            }
        }
    }

    public static void main(String[] args) {
        set(0);
    }
}
//--==>>
/*
 0 4 7 5 2 6 1 3
 0 5 7 2 6 3 1 4
 (.. 생략 ..)
 7 2 0 5 1 4 6 3
 7 3 0 2 5 1 6 4
 */