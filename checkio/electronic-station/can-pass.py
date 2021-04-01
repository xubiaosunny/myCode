"""
If you have solved the "How to find friends" mission, then you already know how to check for the existence of a path in graphs. Let's try to add something more to that problem.

You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value. The matrix consists of digits. You may move to neighbouring cells either horizontally or vertically provided the values of the origin and destination cells are equal. You should determine if a path exists between two given cells.

A matrix is represented as a tuple of tuples with digits. Coordinates are represented as a tuple with two numbers: row and column. The result should be any value which can be converted into a boolean. If a path exists, then return True. Return False if there is none.

!()[https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/c8d77120f3cb4374888fb221840087e8/can-jump-through.svg]
Input: Three arguments. A matrix as a tuple of tuples with integers, first and second cell coordinates as tuples of two integers.

Output: The existence of a path between two given cells as a boolean or a value that can be converted to boolean.

Example:
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 2), (0, 5)) == True, 'First example'
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 3), (6, 0)) == False,

How it is used: Sometimes we don't need the full pathfinding algorithms implementation and can use simplified realisation of these algorithms. It can be an useful skill to find a simple ways.

Precondition:
1 < len(matrix) ≤ 10
all(1 < len(row) ≤ 10 for row in matrix)
all(all(0 ≤ x < 10 for x in row) for row in matrix)
matrix[first[0]][first[1]] == matrix[second[0]][second[1]]
first != second
"""

def can_pass(matrix, first, second):
    size = (len(matrix), len(matrix[0]))
    def go_next(routes):
        next_list = []
        if (x := routes[-1][0] - 1) >= 0:
            next_list.append((x, routes[-1][1]))
        if (x := routes[-1][0] + 1) < size[0]:
            next_list.append((x, routes[-1][1]))
        if (y := routes[-1][1] - 1) >= 0:
            next_list.append((routes[-1][0], y))
        if (y := routes[-1][1] + 1) < size[1]:
            next_list.append((routes[-1][0], y))
        next_list = [n for n in next_list if n not in routes and matrix[n[0]][n[1]] == matrix[first[0]][first[1]]]

        # print(routes, next_list)
        if not next_list:
            return False
        for n in next_list:
            if n == second:
                return True
            r = go_next([*routes, n])
            if r:
                return r
        return False
    # if first[0] >= size[0] or second[0] >= size[0] or first[1] >= size[1] or second[1] >= size[1]:
    #     return False
    return go_next([first])


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
