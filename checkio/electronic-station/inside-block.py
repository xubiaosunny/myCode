"""
When it comes to city planning it's important to understand the borders of various city structures. Parks, lakes or living blocks can be represented as closed polygon and can be described using cartesian coordinates on a map. We need a functionality to determine if a point (a building or a tree) lies inside the structure.

For the purpose of this mission, a city structure may be considered a polygon represented as a sequence of vertex coordinates on a plane or map. The vertices are connected sequentially with the last vertex in the list connecting to the first. We are given the coordinates of the point which we need to check. If the point of impact lies on the edge of the polygon then it should be considered inside of it. For this mission, you need to determine whether the given point lies inside the polygon.


For example, on the left image you see a polygon which is described by ((2,1),(1,5),(5,7),(7,7),(7,2)) and the point at (2,7). The result is False.
For the right image the point lies on the edge and gets counted as inside the polygon, making the result True.

!()[https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/e43019c3516e4f5aac990d5f47f1aacb/example.svg]

Input: Two arguments. Polygon coordinates as a tuple of tuples with two integers each. A checking point coordinates as a tuple of two integers.

Output: Whatever the point inside the polygon or not as a boolean.

Example:
is_inside(((1,1),(1,3),(3,3),(3,1)), (2,2)) == True
is_inside(((1,1),(1,3),(3,3),(3,1)), (4,2)) == False

How it is used: This concept is using for image recognizing. But as we said early it can be useful for topographical software and city planning.

Precondition:
all(x ≥ 0 and y ≥ 0 for x, y in polygon)
point[0] ≥ 0 and point[1] ≥ 0
"""

from typing import Tuple



def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    """
    http://erich.realtimerendering.com/ptinpoly/
    射线法
    """
    flag = False  # 是否在线段上标志
    num = 0
    def is_intersect(start, end):
        nonlocal flag
        min_y = min(start[1], end[1])
        max_y = max(start[1], end[1])
        min_x = min(start[0], end[0])
        max_x = max(start[0], end[0])
        if start[1] == end[1]:  # 平行线
            if point[1] == start[1] and min_x <= point[0] <= max_x:  # 在线段上
                flag = True
            return False
        if min_y <= point[1] < max_y: # 可能相交, 除去临界值
            if start[0] == end[0]:  ## 垂直
                if point[0] == end[0]:  # 在线段上
                    flag = True
                return point[0] <= min_x
            point_x = abs((end[1] - point[1]) * ((end[0] - start[0]) / (end[1] - start[1]))) + min_x
            if point_x == point[0]:  # 在线段上
                flag = True
            return  point_x > point[0]
        return False
    for i in range(len(polygon)):
        if i != len(polygon) - 1:
            if is_intersect(polygon[i], polygon[i + 1]):
                num += 1
        else:
            if is_intersect(polygon[i], polygon[0]):
                num += 1
        if flag:
            return True
    return num % 2 == 1



if __name__ == '__main__':
    # assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
    #                  (2, 2)) is True, "First"
    # assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
    #                  (4, 2)) is False, "Second"
    # assert is_inside(((1, 1), (4, 1), (2, 3)),
    #                  (3, 2)) is True, "Third"
    # assert is_inside(((1, 1), (4, 1), (1, 3)),
    #                  (3, 3)) is False, "Fourth"
    # assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
    #                  (4, 3)) is True, "Fifth"
    # assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
    #                  (4, 3)) is False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) is True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) is False, "Eighth"
    print("All done! Let's check now")
