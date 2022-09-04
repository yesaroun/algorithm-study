# 문제 : 아래와 같이 두 개의 세트가 있다. 두 개의 세트에 있는 사람 이름 중에
# 2개의 파티에 모두 참석한 사람은 누구인가를 출력하시오.
# partyA에 속하는 사람은 "shin", "kim", "son", "chul"이 있다.
# partyB에 속하는 사람은 choi, ki, son, ahn 이 있다.
# 출력결과
# 2개의 파티에 모두 참석한 사람은 아래와 같습니다.
# {'son'}

partyA = {"shin", "kim", "son", "chul"}
partyB = {"choi", "ki", "son", "ahn"}

print("2개의 파티에 모두 참석한 사람은 아래와 같습니다.")
print(partyB.intersection(partyA))