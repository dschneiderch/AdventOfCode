#%%
datafile = open('2022/04/input.txt','r')
input = datafile.read().splitlines()

import re
input1 = list(map(lambda x: re.split('[,-]',x), input))
input2 = list(map(lambda l: [int(x) for x in l], input1 ))
# %%
def func(x):
    if x[0]>=x[2] and x[1]<=x[3]:
        return 1
    elif x[0]<=x[2] and x[1]>=x[3]:
        return 1
    else:
        return 0


def func(x):
    range1 = range(x[0],x[1]+1)
    len1 = len(range1)
    range2 = range(x[2],x[3]+1)
    len2 = len(range2)
    intersect = set(range1).intersection(range2)
    if len(intersect) == len1 or len(intersect) == len2:
        return 1
    else:
        return 0
# %% Answer part 1
sum(map(func, input2))

# %% Start part 2
def func(x):
    intersect = set(range(x[0],x[1]+1)).intersection(range(x[2],x[3]+1))
    # print(intersect)
    if len(intersect):
        return 1
    else:
        return 0


# %% answer 2
sum(list(map(func, input2)))
# %%
