def solution(order):
    answer = 0
    order = str(order)
    
    for i in range(len(order)):
        check_num = order[i]
        if check_num in ["3", "6", "9"]:
            answer = answer + 1

    return answer

print(solution(3))
print(solution(29423))
