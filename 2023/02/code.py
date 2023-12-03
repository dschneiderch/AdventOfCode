# %%
import re
from collections.abc import Iterable
from dataclasses import dataclass, field

# %%

input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


# %%
@dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0


def compare_cubes(game: Iterable[Round], reference: Round) -> bool:
    return not any(
        [
            rnd.red > reference.red
            or rnd.green > reference.green
            or rnd.blue > reference.blue
            for rnd in game
        ]
    )


def find_cube_power(game: Iterable[Round]) -> int:
    red_cubes = max([r.red for r in game])
    green_cubes = max([r.green for r in game])
    blue_cubes = max([r.blue for r in game])
    return red_cubes * green_cubes * blue_cubes


# %% part 1
config = Round(12, 13, 14)
score = 0
possible = 0
games_possible = []
input_file = open("02/input.txt", "r")
for i, line in enumerate(input_file.readlines()):
    game = re.sub("Game \\d+: ", "", line).replace("\n", "").split("; ")
    print(game)
    print("Game", i + 1)
    set_list = []
    for round in game:
        # print(round)
        colors = round.split(", ")
        cubes = dict()
        # game_list = []
        for c in colors:
            # print(c)
            n, name = c.split(" ")
            cubes[name] = int(n)
            # print(dice)
        result = Round(**cubes)
        print(result)
        set_list.append(result)

    print(set_list)

    if compare_cubes(set_list, config):
        games_possible.append(i + 1)
print(games_possible)
score = sum(games_possible)
print(score)
# %% Part 2

power = 0
input_file = open("02/input.txt", "r")
for i, line in enumerate(input_file.readlines()):
    game = re.sub("Game \\d+: ", "", line).replace("\n", "").split("; ")
    print(game)
    print("Game", i + 1)
    set_list = []
    for round in game:
        # print(round)
        colors = round.split(", ")
        cubes = dict()
        # game_list = []
        for c in colors:
            # print(c)
            n, name = c.split(" ")
            cubes[name] = int(n)
            # print(dice)
        result = Round(**cubes)
        print(result)
        set_list.append(result)

    print(set_list)

    power += find_cube_power(set_list)

print(power)


# %%


@dataclass
class Game:
    record: str
    rounds: Iterable[str] = field(init=False)

    def __post_init__(self):
        self.rounds = (
            re.sub("Game \\d+: ", "", self.record).replace("\n", "").split("; ")
        )

    @staticmethod
    def _parse_round(round) -> Round:
        colors = round.split(", ")
        cube = dict()
        for c in colors:
            n, name = c.split(" ")
            cube[name] = int(n)
        result = Round(**cube)
        return result

    @staticmethod
    def is_possible(game: Iterable[Round], reference: Round) -> bool:
        return not any(
            [
                rnd.red > reference.red
                or rnd.green > reference.green
                or rnd.blue > reference.blue
                for rnd in game
            ]
        )

    def parse_game(self) -> Iterable[Round]:
        return [self._parse_round(round) for round in self.rounds]


# %%

config = Round(12, 13, 14)


for line in input.splitlines():
    game = Game(line).parse_game()
    print(game)
    print(Game.is_possible(game, config))
# %%
