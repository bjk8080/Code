def solution(sides):
    sides.sort()
    if sides[2]>(sides[0]+sides[1]):
        n= 2
    elif sides[2]<(sides[0]+sides[1]):
        n=1
    elif sides[2]==(sides[0]+sides[1]):
        n=2
    answer=n
    return answer