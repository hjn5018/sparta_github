def solution(my_string, alp):
    my_string_u = ''
    for char in my_string:
        if alp == char.lower():
            my_string_u += char.upper()
        else:
            my_string_u += char.lower()
            
    return my_string_u
