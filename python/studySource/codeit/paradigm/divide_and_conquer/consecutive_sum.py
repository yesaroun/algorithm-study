# 1부터 n까지의 합을 Divide and conquer 방식으로


def consecutive_sum(start: int, end: int) -> int:
    if end == start:
        return start
    mid = (start + end) // 2
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)


# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
