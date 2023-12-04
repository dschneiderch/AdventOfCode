# %%
import re
from collections.abc import Sequence

# %%
input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


# %%
def get_digit_position(string):
    matches = []
    for match in re.finditer(r"\d+", string):
        matches.append((int(match.group()), [match.start(), match.end()]))
    return matches


def get_special_position(string) -> Sequence[int]:
    pos = []
    for i, c in enumerate(string):
        if not c.isalnum() and c != ".":
            pos.append(i)
    return pos


def is_part(num: Sequence[int], special_characters: Sequence[Sequence[int]]) -> bool:
    start = num[0]
    end = num[1] - 1
    is_adjacent = []
    # print("start ", start)
    # print("end ", end)
    # print(special_characters)
    for character_pos in special_characters:
        for c in character_pos:
            # print("character_pos", c)
            part_condition = c >= start - 1 and c <= end + 1
            # print("part condition:", part_condition)
            is_adjacent.append(part_condition)
    # print(is_adjacent)
    return any(is_adjacent)


# %% part 1
schematic = [""]
special_pos = []
part_sum = 0
# input_file = open("03/input.txt", "r")
# input = input_file.read()
for i, line in enumerate(input.split("\n")):
    print("i ---------------------------- ", i)
    if i == 0:
        schematic.append(line)
        # print("schematic ", schematic)
        continue
    elif i == 1:
        schematic.append(line)
    else:
        special_pos = []
        schematic[0] = schematic[1]
        schematic[1] = schematic[2]
        schematic[2] = line

    # print("schematic:")
    # for s in schematic:
    #     print(f"{s}\n")

    for s in schematic:
        special_pos.append(get_special_position(s))

    digits = get_digit_position(schematic[1])

    for num, pos in digits:
        # print("checking num:", num)
        # print("...is_part", is_part(pos, special_pos))
        if is_part(pos, special_pos):
            part_sum += num

print("i ---------------------------- last row")
last_special_pos = get_special_position(schematic[1])
last_digits = get_digit_position(schematic[2])
for num, pos in last_digits:
    print("checking num:", num)
    if is_part(pos, [last_special_pos]):
        print(num)
        part_sum += num

print(part_sum)

# %%
