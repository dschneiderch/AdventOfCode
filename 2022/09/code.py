#%%
inputfile = open("2022/09/example.txt")
input = inputfile.read().splitlines()
data = [[x[0], int(x[1])] for x in [i.split(" ") for i in input]]
# %%
data
# %%
def move_head(head_pos, d, s):
    match d:
        case "R":
            head_pos[0] += s
        case "U":
            head_pos[1] += s
        case "D":
            head_pos[1] -= s
        case "L":
            head_pos[0] -= s
    return head_pos


def move_tail(head_pos:list, tail_pos:list[list])->list:
    last_tail_pos = tail_pos[-1]
    x_diff = head_pos[0] - last_tail_pos[0]
    y_diff = head_pos[1] - last_tail_pos[1]
    # print("x diff",x_diff)
    # print("y diff",y_diff)
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        # move diagonal
        if abs(x_diff) > 1 and abs(y_diff == 1):
            return tail_pos + [[last_tail_pos[0] + x_diff // 2, last_tail_pos[1]+1]]
        elif abs(y_diff) > 1 and abs(x_diff == 1):
            return tail_pos + [[last_tail_pos[0]+1, last_tail_pos[1] + y_diff // 2]]
        # move lateral
        elif abs(x_diff) > 1:
            new_tail_pos = [last_tail_pos[0] + x_diff // 2, last_tail_pos[1]]
            return tail_pos + [new_tail_pos]
        # move longitudinal
        elif abs(y_diff) > 1:
            new_tail_pos = [last_tail_pos[0], last_tail_pos[1] + y_diff // 2]
            return tail_pos + [new_tail_pos]
    else:
        return tail_pos


head_pos = [0, 0]
tail_pos = [[0, 0]]

for d, s in data:
    print("\nstart:", head_pos, tail_pos[-1])
    print("moving:", d, s)
    i = 1
    while i <= s:
        head_pos = move_head(head_pos, d, 1)
        print(head_pos, tail_pos)
        tail_pos = move_tail(head_pos, tail_pos)
        print("tail: ", tail_pos)
        # print("moved head:", head_pos, tail_pos[-1])
        # print("follow tail:", head_pos, tail_pos[-1])
        i += 1
    print("end: ", head_pos, tail_pos)


print("\n",tail_pos)
len(set(tuple(i) for i in tail_pos))

# %%
