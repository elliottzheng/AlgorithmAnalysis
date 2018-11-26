# 贪心算法实现马踏棋盘问题

import numpy as np

board = np.zeros((8, 8)).astype(np.int8)

possible_move = np.array([
    [-1, 2],
    [2, -1],
    [-2, 1],
    [1, -2],
    [1, 2],
    [2, 1],
    [-2, -1],
    [-1, -2],
])

def countNext(target):
    next = np.zeros(8) - 1
    for i, action in enumerate(possible_move):
        next_target = target + action
        if next_target.max() > 7 or next_target.min() < 0:
            continue
        elif board[next_target[0], next_target[1]] > 0:
            continue
        else:
            next[i] += 1
        for action in possible_move:
            next_next_target = next_target + action
            if next_next_target.max() > 7 or next_next_target.min() < 0:
                continue
            elif board[next_next_target[0], next_next_target[1]] > 0:
                continue
            else:
                next[i] += 1
    next_arg = np.argsort(next)
    valid_sorted_idx = filter(lambda x: next[x] >= 0, next_arg)
    return valid_sorted_idx

all_count=0
def move(board, target, count):
    global all_count
    r, c = target
    board[r, c] = count
    if count >= 64:
        print(board)
        #all_count+=1
        board[r, c] = 0
        return
    sorted_valid_idx= countNext(target)
    for idx in sorted_valid_idx:
        new_target = target + possible_move[idx]
        move(board, new_target, count + 1)
    board[r, c] = 0


move(board, np.array([1, 2]), 1)
print(all_count)
