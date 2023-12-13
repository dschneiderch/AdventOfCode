#%%
import numpy as np
from pathlib import Path
#%%
input_data ="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

input_data = Path(__file__).parent.joinpath("input.txt").read_text()
 # %%
input_int = input_data.strip().replace("#", "1").replace(".","0")
lines = input_int.strip().splitlines()
lines_list = [list(l) for l in lines]
# %% Expand the universe
arr=np.array(lines_list,dtype=int)
# print(arr.shape)
r = np.all(arr==0, axis=0)
colind=np.where(r)[0]
# print(colind)
arr2 = np.insert(arr, colind, values=0, axis=1)
np.all(arr2==0, axis=0)
r = np.all(arr2==0, axis=1)
colind = np.where(r)[0]
# print(colind)
expanded_arr = np.insert(arr2, colind, values=0, axis=0)

#%% Sum shortest paths
sum_path=0
distance = {}
ones = np.nonzero(expanded_arr)
for s,(si,sj) in enumerate(zip(ones[0],ones[1])):
    print(si,sj)
    point_map = {s:(si,sj)}
    for d,(di,dj) in enumerate(zip(ones[0],ones[1])):
        xmoves = abs(si-di)
        ymoves = abs(sj-dj)
        moves = xmoves+ymoves
        distance[d]=moves
        # print(distance)
    distance = {k:v for k,v in distance.items() if v!=0}
    sum_path+=sum(distance.values())
    print(sum_path)

print(sum_path/2) #am i going to pay for this?
# %% Part 2

