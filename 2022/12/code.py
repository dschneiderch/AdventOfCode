#%%
import numpy as np
#%%
inputfile = open("2022/12/example.txt")
input = inputfile.read().splitlines()

# %%
input2=[[*n] for n in input]

#%%
for i,row in enumerate(input2):
    for j,l in enumerate(row):
        match l:
            case "S":
                start_point = (i, j)
                input2[i][j]="a"
            case "E":
                end_point = (i, j)
                input2[i][j]="z"

input2

#%%

def toarray(s):
    return np.array([int(n,36) for n in s])

data = np.array(list(map(toarray, input2)))
data
# %%

class Path():
    def __init__(self, prev_x, prev_y, next_x, next_y):
        self.prev_x = prev_x
        self.prev_y = prev_y
        self.next_x = next_x
        self.next_y = next_y


# %%
