import os
os.system('cls')
from itertools import permutations

def is_prime(num) :
    if num < 2 :
        return False
    for i in range(2, num) :
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    result = set()

    for i in range(1, len(numbers)+1) :
        for per in permutations(numbers,i) :
            result.add(int(''.join(per)))
            
    for num in result :
        if is_prime(num) :
            answer += 1

    return answer

#print(solution("17"))
print(solution("011"))