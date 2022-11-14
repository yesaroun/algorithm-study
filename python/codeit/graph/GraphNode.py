# 지하철 역 노드를 만들겠다
class StationNode:
    """지하철 역 노드를 나타내는 클래스"""
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits

# 지하철 역 노드 인스턴스 생성
station_0 = StationNode("교대역", 14)
station_1 = StationNode("사당역", 14)
station_2 = StationNode("종로3가역", 16)
station_3 = StationNode("서울역", 16)

# 1. 노드들을 파이썬 리스트에 저장
# stations = [station_0, station_1, station_2, station_3]

# 2. 지하철 역 노드들을 파이썬 딕셔너리에 저장한다.
stations = {
    "교대역":station_0,
    "사당역":station_1,
    "종로3가역":station_2,
    "서울역":station_3
}
# 단 이 경우 겹치는 key가 있으면 안된다.
