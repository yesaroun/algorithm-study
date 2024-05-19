def max_product(left_cards: list, right_cards: list) -> int:
    max = left_cards[0] * right_cards[0]
    for left_card in left_cards:
        for right_card in right_cards:
            current_result = left_card * right_card
            if max < (current_result):
                max = current_result
    return max 


# 테스트 코드
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
