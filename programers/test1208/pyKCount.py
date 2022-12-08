def solution(i, j, k):
    answer = 0

    for num in range(i, j+1):
        num = str(num)
        for num2 in range(len(num)):
            if num[num2] == str(k):
                answer += 1

    return answer


print(solution(1, 13, 1))
print(solution(10, 50, 5))
