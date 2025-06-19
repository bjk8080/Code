def solution(n, k):
    if 9<n:
        answer=(12000*n+2000*(k-(n//10)))
    elif n<10:
        answer=(12000*n+2000*k)
    return answer