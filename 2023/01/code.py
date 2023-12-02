# %%
import re

# %% example
input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

# %%
# %%
cal = 0
for line in input.splitlines():
    print(line)
    matches = re.findall("\d", line)
    print(matches)
    cal += int(matches[0]) * 10
    cal += int(matches[-1])
    # cal_vals.append(matches[0])
    # cal_vals.append(matches[-1])

cal
# %% part 1
input_file = open("01/input.txt", "r")
input = input_file.readlines()
cal = 0
for line in input:
    print(line)
    matches = re.findall("\d", line)
    print(matches)
    cal += int(matches[0]) * 10
    cal += int(matches[-1])

cal

# %% part 2
import regex

input_file = open("01/input.txt", "r")
input = input_file.readlines()
cal = 0
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for line in input:
    matches = regex.findall(
        "\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True
    )
    print(matches)
    first = matches[0]
    last = matches[-1]
    if first.isdigit():
        cal += int(first) * 10
    else:
        cal += numbers[first] * 10
    if last.isdigit():
        cal += int(last)
    else:
        cal += numbers[last]

cal
# %%
