"""
런던에 엄청난 폭우가 쏟아진다고 가정합시다. 정말 재난 영화에서나 나올 법한 양의 비가 내려서, 고층 건물이 비에 잠길 정도입니다.
그렇게 되었을 때, 건물과 건물 사이에 얼마큼의 빗물이 담길 수 있는지 알고 싶은데요. 그것을 계산해 주는 함수 trapping_rain을 작성해 보려고 합니다.
함수 trapping_rain은 건물 높이 정보를 보관하는 리스트 buildings를 파라미터로 받고, 담기는 빗물의 총량을 리턴해 줍니다.
예를 들어서 파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다.
그러면 0번 인덱스에 높이 3 의 건물이,
3번 인덱스에 높이 2 의 건물이,
5번 인덱스에 높이 4 의 건물이 있다는 뜻입니다.
1번, 2번, 4번 인덱스에는 건물이 없습니다.
그러면 아래의 사진에 따라 총 10 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 10을 리턴하는 거죠.
+++++#
#~~~~#
#~~#~#
#~~#~#
[3,0,0,2,0,4]
이번에는 파라미터 buildings로 [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]가 들어왔다고 합시다. 그러면 아래의 사진에 따라 총 6 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 6을 리턴하는 거죠
+++++++#++++
+++#~~~##~#+
+#~##~######
"""


def trapping_rain(buildings: list[int]) -> int:
    # 총 담기는 빗물의 양을 변수에 저장
    total_height: int = 0

    # 리스트의 각 인덱스를 돌면서 해당 칸에 담기는 빗물의 양을 구한다.
    # 0번 인덱스와 마지막 인덱스를 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left: int = max(buildings[:i])
        max_rigth: int = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound: int = min(max_left, max_rigth)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])
    return total_height


# 내 풀이
# def trapping_rain(buildings: list[int]) -> int:
#     start_building = 0
#     total_water = 0
#     temp_water = 0
#     for building in buildings:
#         # 0인 경우
#         if building <= 0 and start_building == 0:
#             pass
#         # 0이 아닌 경우
#         else:
#             # 시작하는 경우
#             if start_building == 0:
#                 start_building = building
#             # 시작한 경우
#             else:
#                 # 시작 빌딩보다 크거나 같은 경우
#                 if start_building <= building:
#                     total_water += temp_water
#                     start_building = building
#                 # 작은 경우
#                 else:
#                     temp_water += start_building - building
#     return total_water


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
