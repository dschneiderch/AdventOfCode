# %%


# %%
input_data = """Time:      7  15   30
Distance:  9  40  200"""

# %% part 1
input_file = open("06/input.txt", "r")
input_data = input_file.read()

time_line, dist_line = input_data.strip().split("\n")
times = time_line.split()
times = [int(t) for t in times[1:]]

race_results = {}
for t in times:
    race_distances = []
    for h in range(t):
        hold_time = h
        speed = h
        moving_time = t - h
        distance = speed * moving_time
        race_distances.append(distance)
    race_results[str(t)] = race_distances

dist_records = dist_line.split()
dist_records = [int(d) for d in dist_records[1:]]

win_product = 1
for t, d in zip(times, dist_records):
    wins = [rd for rd in race_results[str(t)] if rd > d]
    print(t, len(wins))
    win_product *= len(wins)

print(win_product)


# %% part 2
input_data = """Time:      7  15   30
Distance:  9  40  200"""

# %%
input_file = open("06/input.txt", "r")
input_data = input_file.read()

time_line, dist_line = input_data.strip().split("\n")
times = time_line.split()
times = [int("".join(times[1:]))]

race_results = {}
for t in times:
    race_distances = []
    for h in range(t):
        hold_time = h
        speed = h
        moving_time = t - h
        distance = speed * moving_time
        race_distances.append(distance)
    race_results[str(t)] = race_distances

dist_records = dist_line.split()
dist_records = [int("".join(dist_records[1:]))]


win_product = 1
for t, d in zip(times, dist_records):
    wins = [rd for rd in race_results[str(t)] if rd > d]
    print(t, len(wins))
    win_product *= len(wins)

print(win_product)
# %%
