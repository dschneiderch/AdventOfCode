# %%
import itertools
import re
from pathlib import Path
from typing import Sequence

# %%

input_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
# %%
input_data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
# %%
instruction_map = dict(L=0, R=1)


def parse_input(input_data):
    lines = input_data.strip().split("\n")
    instructions = lines[0]
    nodes = {
        loc: (L, R)
        for loc, L, R in [re.findall("[A-Z0-9]{3}", line) for line in lines[2:]]
    }
    return instructions, nodes


# %% Part 1
def move(instructions, nodes):
    location = "AAA"
    step_num = 0
    while location != "ZZZ":
        for direction in instructions:
            step_num += 1
            # print("step num: ", step_num)
            # print("current location: ", location)
            # print(i, direction)
            location = nodes[location][instruction_map[direction]]
            # print("new location: ", location)
            if location == "ZZZ":
                print("steps to reach ZZZ: ", step_num)
                break


instructions, nodes = parse_input(
    Path(__file__).parent.joinpath("input.txt").read_text()
)
move(instructions, nodes)


# %% Part 2
input_data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def detect_end(locations: Sequence[str]) -> bool:
    return all([loc.endswith("Z") for loc in locations])


# def move(initial_locations: Sequence[str], instructions: str, nodes: dict) -> None:
#     locations = initial_locations
#     step_num = 0
#     while not detect_end(locations):
#         for direction in instructions:
#             step_num += 1
#             # print("step num: ", step_num)
#             # print("current location: ", locations)
#             # print(direction)
#             locations = [nodes[x][instruction_map[direction]] for x in locations]

#             # print("new locations: ", locations)
#             # print(detect_end(locations))
#             if detect_end(locations):
#                 print("steps to reach end: ", step_num)
#                 break


# # initial_locations = ["AAA"]
# instructions, nodes = parse_input(
#     Path(__file__).parent.joinpath("input.txt").read_text()
# )
# nstructions, nodes = parse_input(input_data)

# initial_locations = [k for k in nodes.keys() if k.endswith("A")]
# move(initial_locations=initial_locations, instructions=instructions, nodes=nodes)


# %% Part 2 with LCM (Thanks Reddit)
def get_cycle_steps(
    initial_locations: Sequence[str], instructions: str, nodes: dict
) -> None:
    locations = initial_locations
    step_num = 0

    for location in locations:
        print("start: ", location)
        initial_location = location
        step_num = 0
        while not location.endswith("Z"):
            for direction in instructions:
                step_num += 1
                # print("step num: ", step_num)
                # print("current location: ", locations)
                # print(direction)
                location = nodes[location][instruction_map[direction]]
                if location.endswith("Z"):
                    start_end_locs[initial_location][location] += 1
                    print("end: ", location)
                    print("--- ", step_num)
                    break
                # if location.endswith("A"):
                #     start_end_locs[initial_location][location] += 1
    return start_end_locs


instructions, nodes = parse_input(
    Path(__file__).parent.joinpath("input.txt").read_text()
)
initial_locations = [k for k in nodes.keys() if k.endswith("A")]
final_locations = [k for k in nodes.keys() if k.endswith("Z")]
# start_locs = {k: 0 for k in initial_locations}

start_end_locs = {}
# loop that makes it work
for s, e in itertools.product(initial_locations, final_locations):
    start_end_locs.setdefault(s, {})[e] = 0
start_end_locs
start_end_locs = get_cycle_steps(
    initial_locations=initial_locations, instructions=instructions, nodes=nodes
)
# in 1e9 iterations, all start points always end at the same place each
# {'QXA': {'HLZ': 79, 'PXZ': 0, 'VJZ': 0, 'NBZ': 0, 'XBZ': 0, 'ZZZ': 0},
#  'PDA': {'HLZ': 0, 'PXZ': 0, 'VJZ': 0, 'NBZ': 0, 'XBZ': 70, 'ZZZ': 0},
#  'TDA': {'HLZ': 0, 'PXZ': 0, 'VJZ': 63, 'NBZ': 0, 'XBZ': 0, 'ZZZ': 0},
#  'QQA': {'HLZ': 0, 'PXZ': 55, 'VJZ': 0, 'NBZ': 0, 'XBZ': 0, 'ZZZ': 0},
#  'PPA': {'HLZ': 0, 'PXZ': 0, 'VJZ': 0, 'NBZ': 50, 'XBZ': 0, 'ZZZ': 0},
#  'AAA': {'HLZ': 0, 'PXZ': 0, 'VJZ': 0, 'NBZ': 0, 'XBZ': 0, 'ZZZ': 60}}
# curiously they never hit the starting point again
#
# cycle counts
# start:  QXA
# end:  HLZ
# ---  12643
# start:  PDA
# end:  XBZ
# ---  14257
# start:  TDA
# end:  VJZ
# ---  15871
# start:  QQA
# end:  PXZ
# ---  18023
# start:  PPA
# end:  NBZ
# ---  19637
# start:  AAA
# end:  ZZZ
# ---  16409
# %%
steps_until_first_Z = [12643, 14257, 15871, 18023, 19637, 16409]
import math

math.lcm(*steps_until_first_Z)
