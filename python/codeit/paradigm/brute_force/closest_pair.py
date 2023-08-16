# 제곱근 사용을 위한 sqrt 함수
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1: int, store2: int) -> float:
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def my_closest_pair(coordinates: list) -> list:
    closest_distance = float("inf")
    total_store = len(coordinates)
    result_stores = []
    for store_1 in range(0, total_store):
        for store_2 in range(store_1 + 1, total_store):
            result = distance(coordinates[store_1], coordinates[store_2])
            if closest_distance > result:
                closest_distance = result
                result_stores = [coordinates[store_1], coordinates[store_2]]
    return result_stores


def closest_pair(coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # 현재까지 가장 가까운 두 매장
    pair: list[tuple[int, int]] = [coordinates[0], coordinates[1]]

    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1: tuple[int, int] = coordinates[i]
            store2: tuple[int, int] = coordinates[j]

            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]

    return pair


# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
