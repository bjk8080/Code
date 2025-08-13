def solution(dot):
    x, y = dot  # dot 배열에서 x, y 값 꺼내기

    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4