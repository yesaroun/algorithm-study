// 신체검사 데이터 배열에서 이진 검색

package chap03;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class PhysExamSearch {
    // 신체검사 데이터를 정의
    static class PhyscData {
        private String name;        // 이름
        private int height;         // 키
        private double vision;      // 시력

        // 생성자
        public PhyscData(String name, int height, double vision) {
            this.name = name;
            this.height = height;
            this.vision = vision;
        }

        // 문자열로 만들어 반환하는 메서드
        public String toString() {
            return name + " " + height + " " + vision;
        }

        // 키의 오름차순으로 정렬하기 위한 comparator
        public static final Comparator<PhyscData> HEIGHT_ORDER = new HeightOrderComparator();

        private static class HeightOrderComparator implements Comparator<PhyscData> {
            public int compare(PhyscData d1, PhyscData d2) {
                return (d1.height > d2.height) ? 1 :
                        (d1.height < d2.height) ? -1 : 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        PhyscData[] x = {       // 키의 오름차순으로 정렬
                new PhyscData("kang", 162, 0.3),
                new PhyscData("lee", 168, 0.4),
                new PhyscData("hwang", 169, 0.8),
                new PhyscData("you", 171, 1.5),
                new PhyscData("kim", 173, 0.7),
                new PhyscData("jang", 174, 1.2),
                new PhyscData("park", 175, 2.0),
        };
        System.out.print("키가 몇 cm인 사람을 찾고 있나요?: ");
        int height = stdIn.nextInt();                   // 키값 입력받음
        int idx = Arrays.binarySearch(
                x,                                              // 배열 x에서
                new PhyscData("", height, 0.0),    // 키가 height인 요소를
                PhyscData.HEIGHT_ORDER                          // HEIGHT_ORDER에 의해 검색
        );
        if (idx < 0)
            System.out.println("그 값의 요소가 없습니다.");
        else {
            System.out.println("그 값은 x[" + idx + "]에 있습니다.");
            System.out.println("찾은 데이터: " + x[idx]);
        }
    }
}
//--==>>
/*
키가 몇 cm인 사람을 찾고 있나요?: 171
그 값은 x[3]에 있습니다.
찾은 데이터: you 171 1.5
 */