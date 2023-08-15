def min_product(left_list: list, right_list: list) -> int:
    min_result = float("inf")
    for left in left_list:
        for right in right_list:
            current_result = left * right
            min_result = min(min_result, current_result)
    return min_result


# 테스트 코드
if __name__ == "__main__":
    print(min_product([1, 3, 4], [3, 4, 5]))    # 3
    print(min_product([-3, 4, -9], [3, -2, 1])) # -27
