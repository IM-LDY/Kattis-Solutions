import math
three_coordinates = [input().split(' ') for i in range(3)]


def calc_area(coor_a, coor_b):

    x_a = int(coor_a[0])
    x_b = int(coor_b[0])
    y_a = int(coor_a[1])
    y_b = int(coor_b[1])
    return (math.sqrt((x_a-x_b)**2+(y_a-y_b)**2))


area_one = calc_area(three_coordinates[0], three_coordinates[1])
area_two = calc_area(three_coordinates[1], three_coordinates[2])
area_three = calc_area(three_coordinates[0], three_coordinates[2])
det = ([area_one, area_two, area_three].index(
    max([area_one, area_two, area_three])))
center_point = []
left_point = []
if det == 0:
    mid_x = (int(three_coordinates[0][0])+int(three_coordinates[1][0]))/2
    mid_y = (int(three_coordinates[0][1])+int(three_coordinates[1][1]))/2
    left_x = int(three_coordinates[2][0])
    left_y = int(three_coordinates[2][1])
    center_point.append(mid_x)
    center_point.append(mid_y)
    left_point.append(left_x)
    left_point.append(left_y)
elif det == 1:
    mid_x = (int(three_coordinates[1][0])+int(three_coordinates[2][0]))/2
    mid_y = (int(three_coordinates[1][1])+int(three_coordinates[2][1]))/2
    left_x = int(three_coordinates[0][0])
    left_y = int(three_coordinates[0][1])
    left_point.append(left_x)
    left_point.append(left_y)
    center_point.append(mid_x)
    center_point.append(mid_y)
else:
    mid_x = (int(three_coordinates[0][0])+int(three_coordinates[2][0]))/2
    mid_y = (int(three_coordinates[0][1])+int(three_coordinates[2][1]))/2
    left_x = int(three_coordinates[1][0])
    left_y = int(three_coordinates[1][1])
    left_point.append(left_x)
    left_point.append(left_y)
    center_point.append(mid_x)
    center_point.append(mid_y)


def calc():
    center_x = center_point[0]
    center_y = center_point[1]
    left_x = left_point[0]
    left_y = left_point[1]
    print(*[int((center_x*2)-left_x), int((center_y)*2-left_y)])


calc()
