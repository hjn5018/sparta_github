def solution(keyinput, board):
    position = [0,0]
    for i in keyinput:
        if i == 'up' and position[1] < board[1]//2:
            position[1] += 1
        elif i == 'down' and -(board[1]//2) < position[1]:
            position[1] -= 1
        elif i == 'right' and position[0] < board[0]//2:
            position[0] += 1
        elif i == 'left' and -(board[0]//2) < position[0]:
            position[0] -= 1
    
    return position