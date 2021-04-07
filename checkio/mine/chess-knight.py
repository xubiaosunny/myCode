"""
Your friend loves chess very much, but he's not a strong player. You can help him by using your programming skills.
If this mission is too simple for you, try another one from this set - The shortest Knight's path.

Your task is to write a function that can find all of the chessboard cells to which the Knight can move. The input data will consist of a start cell and the amount of moves that the Knight will make. There is only one figure on the board - your Knight.
If the same cell appears more than once - do not add it again. You should return the list of all of the possible cells and sort them as follows: in alphabetical order (from 'a' to 'h') and in ascending order (from 'a1' to 'a8' and so on).

!()[https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/09e01bf232574185a670ffa39e02eb45/knight.png]

Input: A start cell, the number of moves.

Output: A list of all of the possible cells.

Example:

chess_knight('a1', 1) == ['b3', 'c2']
chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']

How it is used: For game analysis and bot (game AI) development.

Precondition:
1 <= the number of moves <= 2
"""
from functools import reduce

def can_move(start):
    start_0 = ord(start[0])
    start_1 = int(start[1])
    x = [(start_0 + 1, start_1 + 2), (start_0 + 2, start_1 + 1), (start_0 + 1, start_1 - 2), (start_0 + 2, start_1 - 1),
         (start_0 - 1, start_1 + 2), (start_0 - 2, start_1 + 1), (start_0 - 1, start_1 - 2), (start_0 - 2, start_1 - 1)]
    return [chr(i) + str(j) for i, j in x if 'a' <= chr(i) <= 'h' and 1 <= j <= 8]
    

def chess_knight(start, moves):
    move_list = can_move(start)
    if moves == 1:
        return sorted(list(set(move_list)))
    return sorted(list(set(reduce(lambda x, y: x + y, [can_move(x) for x in move_list], move_list))))

if __name__ == '__main__':
    print("Example:")
    print(chess_knight('h8', 2))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")