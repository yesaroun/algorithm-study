// 아이디를 부여하는 클래스

package chap03;

class Id {
    private static int counter = 0;     // 아이디를 몇 개 부여했는지 저장 (클래스 변수)
    private int id;                     // 아이디 (인스턴스 변수)

    // 생성자
    public Id() { id = ++ counter; }    // (생성자)

    // counter를 반환하는 클래스 메서드
    public static int getCounter() { return counter; }

    // 아이디를 반환하는 인스턴스 메서드
    public int getId() { return id; }
}

public class IdTester {
    public static void main(String[] args) {
        Id a = new Id();    // 아이디 1
        Id b = new Id();    // 아이디 2

        System.out.printf("a의 아이디: %d\n", a.getId());
        System.out.printf("b의 아이디: %d\n", b.getId());

        System.out.println("부여한 아이디의 개수: " + Id.getCounter());
    }
}
//--==>>
/*
a의 아이디: 1
b의 아이디: 2
부여한 아이디의 개수: 2
 */
