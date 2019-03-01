from pprint import pprint

elevations = [
    [100, 105, 97, 101, 87],
    [90, 105, 99, 102, 86],
    [105, 98, 110, 103, 85],
    [78, 102, 87, 104, 84],
    [100, 103, 88, 105, 83],
]

cur_x = 0
cur_y = 2

pprint(elevations)
print("cur_x", cur_x)
print("cur_y", cur_y)

while cur_x < len(elevations[0]) - 1:
    print("---")
    possible_ys = [cur_y]
    if cur_y - 1 >= 0:
        possible_ys.append(cur_y - 1)
    if cur_y + 1 < len(elevations):
        possible_ys.append(cur_y + 1)

    diffs = [
        abs(elevations[poss_y][cur_x + 1] - elevations[cur_y][cur_x])
        for poss_y in possible_ys
    ]

    min_diff = min(diffs)
    min_diff_index = diffs.index(min_diff)
    next_y = possible_ys[min_diff_index]

    cur_x += 1
    cur_y = next_y

    print("cur_x", cur_x)
    print("cur_y", cur_y)
