#%%
inputfile = open("2022/07/input.txt", "r")
input = inputfile.read().splitlines()
input
# %%
def iscd(s):
    return s[0:4] == "$ cd"


def isls(s):
    return s == "$ ls"


def isdir(s):
    return s[0:3] == "dir"


fs = {"/": dict(_sum=0)}
current_dir = list()
for line in input:
    print(f"{line} ....... {current_dir}")
    if iscd(line):
        if line[-2:] == "..":
            current_dir = current_dir[:-1]
        else:
            _, _, new_dir = line.split(" ")
            current_dir.append(new_dir)

        subdir = fs
        for k in current_dir:
            subdir = subdir[k]
        continue

    elif isls(line):
        continue

    elif isdir(line):
        _, dir_name = line.split(" ")
        if subdir.get(dir_name) is None:
            subdir[dir_name] = dict(_sum=0)
        continue

    else:
        size, name = line.split(" ")
        subdir[name] = int(size)
        parentpath = fs
        for sd in current_dir:
            parentpath = parentpath[sd]
            parentpath["_sum"] += int(size)

fs

# %% Answer Part 1


def calc_final_sum(d, final_sum):
    for k, v in d.items():
        if k == "_sum" and v <= 100000:
            final_sum += v
        elif type(v) == dict:
            final_sum = calc_final_sum(v, final_sum)
    return final_sum


calc_final_sum(fs, 0)

# %% Part 2
space_needed = 30000000
total_space = 70000000
used_space = fs["/"].get("_sum")
free_space = total_space - used_space
free_space
additional_space_needed = space_needed - free_space
print(additional_space_needed)


def get_smallest_dir(
    d, smallest_dir_name, parent_dir, additional_space_needed, additional_space
):
    # print(d)
    for k, v in d.items():
        print(f"parent dir: {parent_dir}")
        print(f"....{k}")
        if k == "_sum" and v >= additional_space_needed and v < additional_space:
            additional_space = v
            smallest_dir_name = parent_dir
            print(f"{smallest_dir_name}: {additional_space}")
        elif type(v) == dict:
            parent_dir.append(k)
            smallest_dir_name = get_smallest_dir(
                v,
                smallest_dir_name,
                parent_dir,
                additional_space_needed,
                additional_space,
            )
            parent_dir = parent_dir[:-1]
    return smallest_dir_name


smallest_path = get_smallest_dir(fs["/"], "/", list("/"), additional_space_needed, used_space)
print(smallest_path)
path_delete=fs
for p in smallest_path:
    path_delete = path_delete[p]
print(path_delete)
# %%
