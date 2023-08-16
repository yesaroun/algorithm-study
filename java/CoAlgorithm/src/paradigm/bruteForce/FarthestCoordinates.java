package paradigm.bruteForce;

public class FarthestCoordinates {
    public static double distance(int[] coord1, int[] coord2) {
        return Math.sqrt(Math.pow(coord1[0] - coord2[1], 2) + Math.pow(coord1[1] - coord2[1], 2));
    }

    public static int[][] farthestCoordinates(int[][] coordinates) {
        int[][] farthestPair = {coordinates[0], coordinates[1]};
        double maxDistance = distance(coordinates[0], coordinates[1]);

        for (int i = 0; i < coordinates.length - 1; i++) {
            for (int j = i + 1; j < coordinates.length; j++) {
                int[] coord1 = coordinates[i];
                int[] coord2 = coordinates[j];
                double curDistance = distance(coord1, coord2);

                if (curDistance > maxDistance) {
                    farthestPair[0] = coordinates[i];
                    farthestPair[1] = coordinates[j];
                    maxDistance = curDistance;
                }
            }
        }

        return farthestPair;
    }

    public static void main(String[] args) {
        int[][] testCoordinates = {{4, 1}, {1, 30}, {34, 50}, {5, 3}, {13, 19}, {32, 4}};
        int[][] result = farthestCoordinates(testCoordinates);
        for (int[] coord : result) {
            System.out.print("(" + coord[0] + ", " + coord[1] + ") ");
        }
        // (4, 1) (34, 50)
    }
}
