#%%
import numpy as np

#%%
inputfile = open("2022/08/example.txt", 'r')
input = inputfile.read().splitlines()

def toarray(s):
    return np.array([int(n) for n in [*s]])

data = np.array(list(map(toarray, input)))
data
#%% Part 1
print(data)
visible_trees = data.shape[0]*2 + data.shape[1]*2 - 4
for i in range(1, data.shape[0]-1):
    for j in range(1, data.shape[1]-1):
        if all(data[i,j] > data[i,j+1:]) or all(data[i,j] > data[i,:j]) or all(data[i,j] > data[i+1:,j]) or all(data[i,j] > data[:i,j]):
            visible_trees += 1

print(visible_trees)
# %% Part 2
i=1
j=1
data[i,j]

north=np.zeros_like(data)
south=np.zeros_like(data)
east=np.zeros_like(data)
west=np.zeros_like(data)
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if i!=0:
            north[i,j]=data[i,j] >= data[i-1,j]
        if i!=4:
            south[i,j]=data[i,j] >= data[i+1,j]
        if j!=4:
            east[i,j]=data[i,j] >= data[i,j+1]
        if j!=0:
            west[i,j]=data[i,j] >= data[i, j-1]


# %%
def pos_neg_counts(a):
    mask = a>0
    idx = np.flatnonzero(mask[1:] != mask[:-1])
    count = np.concatenate(( [idx[0]+1], idx[1:] - idx[:-1], [a.size-1-idx[-1]] ))
    if a[0]<0:
        return count[1::2], count[::2] # pos, neg counts
    else:
        return count[::2], count[1::2] # pos, neg counts

pos_neg_counts(data-5)
# %%
def split_app(my_array):
    negative_index = my_array<0
    splits = np.split(negative_index, np.where(np.diff(negative_index))[0]+1)
    len_list = [len(i) for i in splits]
    return len_list

split_app(data-5)
# %%
