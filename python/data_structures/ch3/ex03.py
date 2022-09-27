# list에는 2부터 255까지 정수가 출현한다고 정하기

def solution(lst):
    freq = [0] * 256
    for i in lst:
        freq[i] += 1

    ret = [i for i in range(len(freq)) if freq[i] == max(freq)]
    if len(lst) == len(ret):
        return []

    return ret

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]