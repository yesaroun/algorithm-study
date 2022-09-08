# list에는 2부터 255까지 정수가 출현한다고 정하기

def solution(lst):
    freq = {x:lst.count(x) for x in set(lst)}
    if len(freq) == 1 or len(freq) == len(lst):
        return []
    else:
        return [x for x in freq.keys() if freq[x] == max(freq.values())]

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]