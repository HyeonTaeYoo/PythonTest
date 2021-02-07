
location = input()

col = int(ord(location[0]))-96
row = int(location[1])


result = 0
steps = [(-1, -2), (1, -2), (-1, 2), (1, 2),
         (-2, -1), (-2, 1), (2, -1), (2, 1)]

for step in steps:
    next_col = col + step[0]
    next_row = row + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)
