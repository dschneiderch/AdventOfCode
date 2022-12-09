#%%
inputfile = open('input.txt','r')
inputstring = inputfile.read()
input=inputstring.splitlines()
input

# %%
def split_string(s):

    assert len(s)%2 == 0
    # print(len(s)/2)
    s1=s[0:(len(s)//2)]
    s2=s[(len(s)//2):]
    return [s1,s2]
        
# %%
compartments = list(map(split_string,input))
# %%
set(compartments[-1][0]).intersection(compartments[-1][1])

#%%
intersect = list(map(lambda x: set(x[0]).intersection(x[1]), compartments))
# %%
# %%
import string
# %%
valuedict=dict(zip(string.ascii_lowercase+string.ascii_uppercase,range(1,53)))
valuedict

# %% Answer Part 1
sum(map(lambda x: valuedict[list(x)[0]], intersect))

# %% Start Part 2
n=3
out = [input[k:k+n] for k in range(0, len(input), n)]

# %%
set(out[-1][0]).intersection(out[-1][1]).intersection(out[-1][2])
def myintersection(x):
    num_parts = len(x)
    common=set(x[0]).intersection(x[1])
    if num_parts > 2:
        for i in range(2,num_parts):
            common=common.intersection(x[i])
    return common    

i3 = list(map(myintersection, out))
intersect3 = list(map(lambda x: set(x[0]).intersection(x[1]).intersection(x[2]), out))


# %% Answer Part 2
sum(map(lambda x: valuedict[list(x)[0]], i3))
# %%
