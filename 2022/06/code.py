#%%
inputfile = open("2022/06/input.txt", "r")
input = inputfile.read()
# input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
# %% Answer Part 1
def find_unique(signal, num):
    for i in range(len(signal)):
        mark = signal[i : i + num]
        if len(set(mark)) == len(mark):
            return i + num


find_unique(input, 4)
# %% Start Part 2
find_unique(input, 14)


# %%
