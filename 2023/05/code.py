# %%
# %%
input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# %% part 1
# input_file = open("05/input.txt", "r")
# input = input_file.read()

maps = input.strip().split("\n\n")

_, seeds = maps[0].split("seeds: ")
seeds = [int(s) for s in seeds.split()]


def src2dest(source_num, resource_map):
    lines = resource_map.split("\n")
    src_name, dest_name = lines[0].strip(" map:").split("-to-")
    dest_num = source_num
    for line in lines[1:]:
        map_values = [int(s) for s in line.split()]
        # find source
        if source_num >= map_values[1] and source_num < map_values[1] + map_values[2]:
            diff = source_num - map_values[1]
            dest_num = map_values[0] + diff

    return (src_name, dest_name), dest_num


location = []
for seed in seeds:
    source_num = seed
    print(seed)
    for resource_map in maps[1:]:
        # print(resource_map)
        (src_name, dest_name), dest_num = src2dest(source_num, resource_map)
        print(f"{src_name} {source_num} -> {dest_name} {dest_num}")
        source_num = dest_num

    location.append(dest_num)

min(location)
# %% part 2
# input_file = open("05/input.txt", "r")
# input = input_file.read()


maps = input.strip().split("\n\n")

_, seeds = maps[0].split("seeds: ")
seeds = [int(s) for s in seeds.split()]
seed_pairs = zip(seeds[0::2], seeds[1::2])


def src2dest(source_pair, resource_map):
    source_num = source_pair[0]
    source_length = source_pair[1]
    # print(resource_map)
    lines = resource_map.split("\n")
    src_name, dest_name = lines[0].strip(" map:").split("-to-")
    dest_pair = source_pair

    for line in lines[1:]:
        map_values = [int(s) for s in line.split()]
        # print(source_num, source_length, map_values)
        dest_map_value = map_values[0]
        source_map_value = map_values[1]
        range_value = map_values[2]

        #### ----- This works for the example but not for the input. Mostly luck for the example. This
        # approach drops numbers between source_num and source_map_value. I think you need to preprocess the source_pair
        # outside this loop to match the breaks in the source_map_values and then iterate and combine mulitple dest pairs :(
        if (
            source_num < source_map_value
            and source_map_value < source_num + source_length - 1
        ):
            source_pair = (
                source_map_value,
                min(source_length - (source_map_value - source_num) - 1, range_value),
            )
            source_num = source_pair[0]
            source_length = source_pair[1]
        #### -------------------
        if (
            source_num >= source_map_value
            and source_num < source_map_value + range_value
        ):
            diff = source_num - source_map_value
            dest_num = dest_map_value + diff
            matched_dest = min(range_value - diff, source_length)
            dest_pair = (dest_num, matched_dest)

    return (src_name, dest_name), dest_pair


location = []
for seed in seed_pairs:
    print(seed)
    source_pair = seed
    for resource_map in maps[1:]:
        print(resource_map)
        (src_name, dest_name), dest_pair = src2dest(source_pair, resource_map)
        print(f"{src_name} {source_pair} -> {dest_name} {dest_pair}")
        source_pair = dest_pair

    location.append(dest_pair)

min([a for a, b in location])

# %%
