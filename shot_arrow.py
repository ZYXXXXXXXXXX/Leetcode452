# 452
def findMinArrowShots(points):
    if len(points) == 0:
        return 0
    arrow = 1
    sort_arr = sorted(points, key=lambda x: x[1])
    my_target = sort_arr[0][1]
    for items in sort_arr:
        if items[0] > my_target:
            my_target = items[1]
            arrow += 1
    return arrow

if __name__ == '__main__':
    points = [[10,16],[2,8],[1,6],[7,12]]
    print(findMinArrowShots(points))