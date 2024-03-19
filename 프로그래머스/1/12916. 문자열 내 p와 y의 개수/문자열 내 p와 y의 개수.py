def solution(s):
    answer = True
    s = s.lower()
    p_num = s.count('p') 
    y_num = s.count('y')
    
    if(p_num != y_num) :
        answer = False
    
    return answer