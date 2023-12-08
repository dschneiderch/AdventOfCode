# %%
from collections import Counter
from collections.abc import Sequence
from pathlib import Path

# %%
input_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


# %%
hands = ["5K", "4K", "FH", "3K", "2P", "1P", "HC"]
hand_values = list(reversed(range(len(hands))))
hand_map = {h: hv for h, hv in zip(hands, hand_values)}
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_values = list(reversed(range(len(cards))))
card_map = {c: cv for c, cv in zip(cards, card_values)}


def identify_hand(cards_in_hand: str) -> str:
    card_count = []
    for c in cards:
        card_count.append(cards_in_hand.count(c))

    def _find_digit_occurence(lst, digit):
        all_matches = [val for val in lst if val == digit]
        return len(all_matches)

    if 5 in card_count:
        kind = "5K"
    elif 4 in card_count:
        kind = "4K"
    elif 3 in card_count and 2 in card_count:
        kind = "FH"
    elif 3 in card_count:
        kind = "3K"
    elif _find_digit_occurence(card_count, 2) == 2:
        kind = "2P"
    elif 2 in card_count:
        kind = "1P"
    else:
        kind = "HC"

    return kind


# %%
def rank_hand1(hand: str) -> int:
    return hand_map[identify_hand(hand)]


def rank_cards1(cards_in_hand: str) -> Sequence[int]:
    return [card_map[c] for c in cards_in_hand]


def _sort_key1(h):
    return (rank_hand1(h), rank_cards1(h))


# %%
# input_file = open("07/input.txt", "r")
# input_data = input_file.read()
lines = input_data.strip().split()
cards_in_hand = [hand for hand in lines[::2]]
bids = [int(bid) for bid in lines[1::2]]
bid_map = {h: b for h, b in zip(cards_in_hand, bids)}

hands_sorted = sorted(cards_in_hand, key=_sort_key1, reverse=False)
bids_sorted = []
for h in hands_sorted:
    bids_sorted.append(bid_map[h])

winnings = 0
for i, b in enumerate(bids_sorted):
    winnings += b * (i + 1)

print(winnings)


# %% Part 2
hands = ["5K", "4K", "FH", "3K", "2P", "1P", "HC"]
hand_values = list(reversed(range(len(hands))))
hand_map = {h: hv for h, hv in zip(hands, hand_values)}
cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
card_values = list(reversed(range(len(cards))))
card_map = {c: cv for c, cv in zip(cards, card_values)}


def identify_hand_with_joker(cards_in_hand: str) -> str:
    def _upgrade_kind(cards_in_hand: str) -> str:
        cards_with_count = Counter(cards_in_hand)
        _ = cards_with_count.pop("J")
        primary_card = max(cards_with_count, key=cards_with_count.get)

        virtual_cards = cards_in_hand.replace("J", primary_card)
        # print("virtual cards", virtual_cards)
        return virtual_cards

    def _find_number_of_occurences(lst, digit):
        all_matches = [val for val in lst if val == digit]
        return len(all_matches)

    def _get_kind(cards_in_hand: str):
        card_count = []
        for c in cards:
            card_count.append(cards_in_hand.count(c))

        if 5 in card_count:
            kind = "5K"
        elif 4 in card_count:
            kind = "4K"
        elif 3 in card_count and 2 in card_count:
            kind = "FH"
        elif 3 in card_count:
            kind = "3K"
        elif _find_number_of_occurences(card_count, 2) == 2:
            kind = "2P"
        elif 2 in card_count:
            kind = "1P"
        else:
            kind = "HC"

        return kind

    # print(cards_in_hand)

    if "J" not in cards_in_hand or cards_in_hand.count("J") == 5:
        kind = _get_kind(cards_in_hand)
    else:
        virtual_cards = _upgrade_kind(cards_in_hand)
        kind = _get_kind(virtual_cards)
        # print("kind", kind)

    return kind


def rank_hand2(hand: str) -> int:
    return hand_map[identify_hand_with_joker(hand)]


def rank_cards2(cards_in_hand: str) -> Sequence[int]:
    return [card_map[c] for c in cards_in_hand]


def _sort_key2(hb):
    h, b = hb
    return (rank_hand2(h), rank_cards2(h))


# %%
input_data = Path(__file__).parent.joinpath("input.txt").read_text()

lines = input_data.strip().split()
cards_in_hand = [hand for hand in lines[::2]]
bids = [int(bid) for bid in lines[1::2]]
bid_map = {h: b for h, b in zip(cards_in_hand, bids)}

hands_sorted = sorted(list(zip(cards_in_hand, bids)), key=_sort_key2, reverse=False)

winnings = 0
for i, (h, b) in enumerate(hands_sorted):
    winnings += b * (i + 1)

print(winnings)

# %%
