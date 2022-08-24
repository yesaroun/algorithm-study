# 사용자로부터 정수를 입력받아서 소수를 판별하는 함수 is_prime()을 작성해보자.
# 소수면 True, 소수가 아니면 False 출력하도록 만든다.

def is_prime(num):
    for i in range(2, num):
        temp = True
        if (num % i) == 0:
            temp = False
        else:
            temp = True
        return temp

prime = int(input("int : "))

# 함수 호출
print(is_prime(prime))
#--==>>
'''
int : 8
False
'''