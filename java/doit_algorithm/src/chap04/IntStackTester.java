// int 형 고정 길이 스택의 사용 예

package chap04;

import java.util.Scanner;

public class IntStackTester {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        IntStack s = new IntStack(64);      // 최대 64개를 푸시할 수 있는 스택

        while (true) {
            System.out.println();                   // 메뉴 구분을 위한 빈 행 추가
            System.out.printf("현재 데이터 개수: %d / %d\n", s.size(), s.getCapacity());
            System.out.print("(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: ");

            int menu = stdIn.nextInt();
            if(menu == 0) break;

            int x;

            switch (menu) {
                case 1:                             // 푸시
                    System.out.print("데이터: ");
                    x = stdIn.nextInt();
                    try {
                        s.push(x);
                    } catch (IntStack.OverflowIntStackException e) {
                        System.out.println("스택이 가득 찼습니다.");
                    }
                    break;

                case 2:                             // 팝
                    try {
                        x = s.pop();
                        System.out.println("팝한 데이터는 " + x + "입니다.");
                    } catch (IntStack.EmptyIntStackException e) {
                        System.out.println("스택이 비어 있습니다.");
                    }
                    break;

                case 3:                             // 피크
                    try {
                        x = s.peek();
                        System.out.println("피크한 데이터는 " + x + "입니다.");
                    } catch (IntStack.EmptyIntStackException e) {
                        System.out.println("스택이 비어 있습니다.");
                    }
                    break;

                case 4:                             // 덤프
                    s.dump();
                    break;
            }
        }
    }
}
//--==>>
/*
현재 데이터 개수: 0 / 64
(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: 1
데이터: 1

현재 데이터 개수: 1 / 64
(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: 1
데이터: 2

현재 데이터 개수: 2 / 64
(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: 1
데이터: 4

현재 데이터 개수: 3 / 64
(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: 3
피크한 데이터는 4입니다.

현재 데이터 개수: 3 / 64
(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: 4
1 2 4

현재 데이터 개수: 3 / 64
(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: 2
팝한 데이터는 4입니다.

현재 데이터 개수: 2 / 64
(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: 2
팝한 데이터는 2입니다.

현재 데이터 개수: 1 / 64
(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: 4
1

현재 데이터 개수: 1 / 64
(1) 푸시  (2) 팝  (3) 피크  (4) 덤프  (0) 종료: 0
 */