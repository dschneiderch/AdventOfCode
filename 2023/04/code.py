# %%

# %%
input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# %% part 1
total_score = 0
# input_file = open("04/input.txt", "r")
# input = input_file.read()
for line in input.strip().split("\n"):
    _, game = line.split(": ")
    winning_nums, my_nums = game.split("|")
    winning_nums = winning_nums.split()
    my_nums = my_nums.split()
    # print(winning_nums)
    # print(my_nums)
    i = 1
    score = 0
    for n in my_nums:
        # print(n)
        if n in winning_nums and i == 1:
            score = 1
            i += 1
        elif n in winning_nums:
            score *= 2
    total_score += score
    # print("score", score)

print(total_score)


# %% part 2
def add_cards_to_hand(original_card, num_matches):
    for n in range(num_matches):
        new_card_number = original_card + n + 1
        if new_card_number > len(initial_card_matches) - 1:
            return cards_in_hand
        cards_in_hand[new_card_number] += 1
        matches_in_new_card = initial_card_matches[new_card_number]
        if matches_in_new_card > 0:
            add_cards_to_hand(
                original_card=new_card_number, num_matches=matches_in_new_card
            )

    return cards_in_hand


def get_num_matches(my_nums, winning_nums):
    winning_numbers = [n for n in my_nums if n in winning_nums]
    return len(winning_numbers)


total_score = 0
initial_card_matches = []
cards_in_hand = [1 for _ in enumerate(input.strip().split("\n"))]

input_file = open("04/input.txt", "r")
input = input_file.read()
for i, line in enumerate(input.strip().split("\n")):
    _, game = line.split(": ")
    winning_nums, my_nums = game.split("|")
    winning_nums = winning_nums.split()
    my_nums = my_nums.split()

    initial_card_matches.append(get_num_matches(my_nums, winning_nums))
# print(initial_card_matches)

for i, num_matches in enumerate(initial_card_matches):
    cards_in_hand = add_cards_to_hand(i, num_matches=num_matches)

    # print(cards_in_hand)

print(sum(cards_in_hand))

# %%
