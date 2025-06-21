def solution(n):
    if int(n**0.5)**2==n:
        answer=1
    elif int(n**0.5)**2!=n:
        answer=2
    
    return answer