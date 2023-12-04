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


def get_gear_indicator_position(string) -> Sequence[int]:
    pos = []
    for i, c in enumerate(string):
        if c == "*":
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


def get_gear_ratio(
    gear_pos: int, schematic_digits: Sequence[Sequence[Sequence]]
) -> int:
    # print("gear pos", gear_pos)
    # print("schematic digits", schematic_digits)
    is_adjacent = []
    # print("end ", end)
    # print(special_characters)
    for sd in schematic_digits:
        for d in sd:
            num, (start, end) = d
            end = end - 1
            print(start, end, gear_pos)
            part_condition = gear_pos >= start - 1 and gear_pos <= end + 1
            if part_condition:
                print(num)
                is_adjacent.append(num)
    print(is_adjacent)
    if len(is_adjacent) == 2:
        product = 1
        for a in is_adjacent:
            product *= a
        return product
    else:
        return 0


# %% part 1 & part 2
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

schematic = [""]
special_pos = []
gear_digits = []
part_sum = 0
gear_ratio_sum = 0
input_file = open("03/input.txt", "r")
input = input_file.read()
input = input + """\n """
for i, line in enumerate(input.split("\n")):
    print("i ---------------------------- ", i)
    if i == 0:
        schematic.append(line)
        continue
    elif i == 1:
        schematic.append(line)
    else:
        special_pos = []
        gear_digits = []
        schematic[0] = schematic[1]
        schematic[1] = schematic[2]
        schematic[2] = line

    # print("schematic:")
    # for s in schematic:
    #     print(f"{s}\n")

    for s in schematic:
        special_pos.append(get_special_position(s))  # for part 1
        gear_digits.append(get_digit_position(s))  # for part 2

    digits = get_digit_position(schematic[1])  # for part 1
    gear_pos = get_gear_indicator_position(schematic[1])  # for part 2

    # part 1
    for num, pos in digits:
        if is_part(pos, special_pos):
            part_sum += num
    # part 2
    for pos in gear_pos:
        gear_ratio = get_gear_ratio(pos, gear_digits)
        gear_ratio_sum += gear_ratio


print("part sum: ", part_sum)
print("gear ratio sum: ", gear_ratio_sum)
# %%
