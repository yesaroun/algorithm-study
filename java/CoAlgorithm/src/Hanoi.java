public class Hanoi {
    public static void moveDisk(int diskNum, int startPeg, int endPeg) {
        System.out.printf("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동%n", diskNum, startPeg, endPeg);
    }

    public static void hanoi(int numDisks, int startPeg, int endPeg) {
        if (numDisks == 0) {
            return;
        } else {
            int otherPeg = 6 - startPeg - endPeg;

            hanoi(numDisks - 1, startPeg, otherPeg);

            moveDisk(numDisks, startPeg, endPeg);

            hanoi(numDisks - 1, otherPeg, endPeg);
        }
    }

    public static void main(String[] args) {
        hanoi(3, 1, 3);
    }
}
