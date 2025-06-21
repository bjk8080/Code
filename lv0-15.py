def solution(num_list):
    x=0
    y=0
    for num in num_list:
        if num%2==0:
            x += 1
        elif num%2!=0:
            y += 1
    answer=[x,y]
    return answer