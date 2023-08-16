from math import sqrt


def distance(coord1: tuple[int, int], coord2: tuple[int, int]) -> float:
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def farthest_coordinates(coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
    farthest_pair: list[tuple[int, int]] = [coordinates[0], coordinates[1]]
    max_distance: float = distance(coordinates[0], coordinates[1])

    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            coord1: tuple[int, int] = coordinates[i]
            coord2: tuple[int, int] = coordinates[j]
            cur_distance: float = distance(coord1, coord2)

            if cur_distance > max_distance:
                farthest_pair = [coordinates[i], coordinates[j]]
                max_distance = cur_distance

    return farthest_pair


if __name__ == "__main__":
    test_coordinates = [(4, 1), (1, 30), (34, 50), (5, 3), (13, 19), (32, 4)]
    print(farthest_coordinates(test_coordinates))  # [(4, 1), (34, 50)]
