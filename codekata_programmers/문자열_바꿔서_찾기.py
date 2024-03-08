def solution(myString, pat):
    new_string = ''
    for char in myString:
        if char == 'A':
            new_string += 'B'
        else:
            new_string += 'A'
            
    if pat in new_string:
        return 1
    else:
        return 0