// 신체검사 데이터용 클래스 배열에서 평균 키와 시력의 분포를 구함

package chap02;

import java.util.Scanner;

public class PhysicalExamination {

    static final int VMAX = 21;     // 시력 분포(0.0 ~ 0.1 단위로 21개)

    static class PhyscData {
        String name;                // 이름
        int height;                 // 키
        double vision;              // 시력

        PhyscData(String name, int height, double vision) {
            this.name = name;
            this.height = height;
            this.vision = vision;
        }
    }

    // 키와 평균값을 구함
    static double aveHeight(PhyscData[] dat) {
        double sum = 0;

        for (int i = 0; i < dat.length; i++) {
            sum += dat[i].height;
        }

        return sum / dat.length;
    }

    // 시력 분포를 구함
    static void distVision(PhyscData[] dat, int[] dist) {
        int i = 0;
        dist[i] = 0;
        for (i = 0; i < dat.length; i++) {
            if (dat[i].vision >= 0.0 && dat[i].vision <= VMAX / 10.0) {
                dist[(int)(dat[i].vision * 10)]++;
            }
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        PhyscData[] x = {
                new PhyscData("kang", 162, 0.3),
                new PhyscData("kim", 173, 0.7),
                new PhyscData("park", 175, 2.0),
                new PhyscData("you", 171, 1.5),
                new PhyscData("lee", 168, 0.4),
                new PhyscData("jang", 174, 1.2),
                new PhyscData("hwang", 169, 0.8),
        };
        int[] vdist = new int[VMAX];        // 시력 분포

        System.out.println("■ 신체검사 리스트 ■");
        System.out.println("이름      키       시력");
        System.out.println("--------------------");
        for (int i = 0; i < x.length; i++) {
            System.out.printf("%-8s%3d%5.1f\n", x[i].name, x[i].height, x[i].vision);
        }

        System.out.printf("\n평균 키: %5.1fcm\n", aveHeight(x));

        distVision(x, vdist);

        System.out.println("\n시력 분포");
        for (int i = 0; i < VMAX; i++) {
            System.out.printf("%3.1f~: %2d명\n", i / 10.0, vdist[i]);
        }
    }
}
//--==>>
/*
■ 신체검사 리스트 ■
이름      키       시력
--------------------
kang    162  0.3
kim     173  0.7
park    175  2.0
you     171  1.5
lee     168  0.4
jang    174  1.2
hwang   169  0.8

평균 키: 170.3cm

시력 분포
0.0~:  0명
0.1~:  0명
0.2~:  0명
0.3~:  1명
0.4~:  1명
0.5~:  0명
0.6~:  0명
0.7~:  1명
0.8~:  1명
0.9~:  0명
1.0~:  0명
1.1~:  0명
1.2~:  1명
1.3~:  0명
1.4~:  0명
1.5~:  1명
1.6~:  0명
1.7~:  0명
1.8~:  0명
1.9~:  0명
2.0~:  1명
 */




















