def is_palindrome(word):
    result = True
    for i in range(len(word) // 2):
        if word[i] == word[len(word) - i - 1]:
            result = True
        else:
            result = False
            break

    return result

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))