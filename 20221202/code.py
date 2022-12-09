import numpy as np

fin = open("20221202/input.txt", "r")
raw_input = fin.readlines()
input = [i.strip("\n") for i in raw_input]

translator = dict(A="Rock", B="Paper", C="Scissors", X="Rock", Y="Paper", Z="Scissors")
rtranslator = dict(zip(translator.values(), translator.keys()))


def _translate(x: str):
    return translator.get(x)


def _decode(hands: str) -> str:
    if _translate(hands[0]) == "Rock" and hands[-1] == "X":
        return rtranslator["Scissors"]
    if _translate(hands[0]) == "Rock" and hands[-1] == "Y":
        return rtranslator["Rock"]
    if _translate(hands[0]) == "Rock" and hands[-1] == "Z":
        return rtranslator["Paper"]
    if _translate(hands[0]) == "Paper" and hands[-1] == "X":
        return rtranslator["Rock"]
    if _translate(hands[0]) == "Paper" and hands[-1] == "Y":
        return rtranslator["Paper"]
    if _translate(hands[0]) == "Paper" and hands[-1] == "Z":
        return rtranslator["Scissors"]
    if _translate(hands[0]) == "Scissors" and hands[-1] == "X":
        return rtranslator["Paper"]
    if _translate(hands[0]) == "Scissors" and hands[-1] == "Y":
        return rtranslator["Scissors"]
    if _translate(hands[0]) == "Scissors" and hands[-1] == "Z":
        return rtranslator["Rock"]


def _pts_outcome(hands):
    if _translate(hands[0]) == "Rock" and _translate(hands[-1]) == "Rock":
        pts = 3
    elif _translate(hands[0]) == "Rock" and _translate(hands[-1]) == "Paper":
        pts = 6
    elif _translate(hands[0]) == "Rock" and _translate(hands[-1]) == "Scissors":
        pts = 0
    elif _translate(hands[0]) == "Paper" and _translate(hands[-1]) == "Rock":
        pts = 0
    elif _translate(hands[0]) == "Paper" and _translate(hands[-1]) == "Paper":
        pts = 3
    elif _translate(hands[0]) == "Paper" and _translate(hands[-1]) == "Scissors":
        pts = 6
    elif _translate(hands[0]) == "Scissors" and _translate(hands[-1]) == "Rock":
        pts = 6
    elif _translate(hands[0]) == "Scissors" and _translate(hands[-1]) == "Paper":
        pts = 0
    elif _translate(hands[0]) == "Scissors" and _translate(hands[-1]) == "Scissors":
        pts = 3
    return pts


def _pts_hand(hands):
    if _translate(hands[-1]) == "Rock":
        pts = 1
    if _translate(hands[-1]) == "Paper":
        pts = 2
    if _translate(hands[-1]) == "Scissors":
        pts = 3
    return pts


def get_points(x: str) -> int:
    new_hand = [x[0], _decode(x)]
    # print(new_hand)
    return _pts_outcome(new_hand) + _pts_hand(new_hand)


def main():
    print(sum(map(get_points, input)))
    print("done")


if __name__ == "__main__":
    main()
