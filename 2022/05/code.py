#%%
inputfile = open("2022/05/input.txt", "r")
input = inputfile.read().splitlines()
# %%
for i,j in enumerate(input):
    if j[1].isdigit():
        break
stack_rows = input[0:i]
t_stack_rows = list(zip(*stack_rows))
print(t_stack_rows)

# print(len(t_stack_rows))
stacks = [t_stack_rows[1 + i] for i in range(0, len(t_stack_rows) + 1, 4)]
stacks = list(map(lambda x: [e for e in x if e.isalpha()], stacks))
stacks = dict((k + 1, list(reversed(v))) for k, v in enumerate(stacks))
stacks
# %%
import re

instructions = list(map(lambda x: re.findall(r"\d+", x), input[10:]))
instructions
#%% Part 1 Answer

for move in instructions:
    print(f"move: {move}")
    num_crates = int(move[0])
    print(f"num_crates: {num_crates}")
    from_stack = stacks[int(move[1])]
    to_stack = stacks[int(move[2])]
    index = len(from_stack) - num_crates
    crates_to_move = from_stack[index:]

    print(f"crates_to_move: {crates_to_move}")
    to_stack.extend(reversed(crates_to_move))
    from_stack[index:] = []
    print(stacks)


#%% Part 2 Answer

for move in instructions:
    print(f"move: {move}")
    num_crates = int(move[0])
    print(f"num_crates: {num_crates}")
    from_stack = stacks[int(move[1])]
    to_stack = stacks[int(move[2])]
    index = len(from_stack) - num_crates
    crates_to_move = from_stack[index:]

    print(f"crates_to_move: {crates_to_move}")
    to_stack.extend(crates_to_move)
    from_stack[index:] = []
    print(stacks)

# %%
