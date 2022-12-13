from typing import List, Callable


class Monkey:
    def __init__(
        self, id: int, items: List[int], ops: Callable, test: Callable
    ) -> None:
        self.id = id
        self.items = items
        self.ops = ops
        self.test = test
        self.inspections = 0

    def inspect_items(self):
        result = list()
        for i in self.items:
            self.inspections += 1
            new_worry_level = self.ops(i)
            throw_to = self.test(new_worry_level)
            result.append((new_worry_level, throw_to))
        return result


class Keep_Away:
    def __init__(self, monkeys: List[Monkey]) -> None:
        self.monkeys = monkeys

    def give_item(self, thrown_item, to_monkey, from_monkey):
        new_monkey = list(filter(lambda x: x.id == to_monkey, self.monkeys))
        new_monkey[0].items.append(thrown_item)
        from_monkey.items.pop(0)

    def play(self, rounds):
        for r in range(rounds):
            for m in self.monkeys:
                exchange = m.inspect_items()
                # print(m.id, exchange)
                for t in exchange:
                    self.give_item(*t, m)

        # [print(x.id, x.items) for x in self.monkeys]


import operator

if __name__ == "__main__":

    monkeys = [
        Monkey(0, [79, 98], lambda x: x * 19 // 3, lambda x: 2 if x % 23 == 0 else 3),
        Monkey(
            1,
            [54, 65, 75, 74],
            lambda x: (x + 6) // 3,
            lambda x: 2 if x % 19 == 0 else 0,
        ),
        Monkey(
            2,
            [79, 60, 97],
            lambda x: (x * x) // 3,
            lambda x: 1 if x % 13 == 0 else 3,
        ),
        Monkey(3, [74], lambda x: (x + 3) // 3, lambda x: 0 if x % 17 == 0 else 1),
    ]

    game = Keep_Away(monkeys)
    game.play(20)

    assert operator.mul(*(sorted(map(lambda x: x.inspections, monkeys))[-2:])) == 10605

    # Part 1
    monkeys = [
        Monkey(
            0,
            [98, 97, 98, 55, 56, 72],
            lambda x: x * 13 // 3,
            lambda x: 4 if x % 11 == 0 else 7,
        ),
        Monkey(
            1,
            [73, 99, 55, 54, 88, 50, 55],
            lambda x: (x + 4) // 3,
            lambda x: 2 if x % 17 == 0 else 6,
        ),
        Monkey(
            2,
            [67, 98],
            lambda x: (x * 11) // 3,
            lambda x: 6 if x % 5 == 0 else 5,
        ),
        Monkey(
            3,
            [82, 91, 92, 53, 99],
            lambda x: (x + 8) // 3,
            lambda x: 1 if x % 13 == 0 else 2,
        ),
        Monkey(
            4,
            [52, 62, 94, 96, 52, 87, 53, 60],
            lambda x: (x * x) // 3,
            lambda x: 3 if x % 19 == 0 else 1,
        ),
        Monkey(
            5,
            [94, 80, 84, 79],
            lambda x: (x + 5) // 3,
            lambda x: 7 if x % 2 == 0 else 0,
        ),
        Monkey(6, [89], lambda x: (x + 1) // 3, lambda x: 0 if x % 3 == 0 else 5),
        Monkey(
            7,
            [70, 59, 63],
            lambda x: (x + 3) // 3,
            lambda x: 4 if x % 7 == 0 else 3,
        ),
    ]

    game = Keep_Away(monkeys)
    game.play(20)

    print(operator.mul(*(sorted(map(lambda x: x.inspections, monkeys))[-2:])))

    # Part 2 - Based on reddit, I think you need to apply "mod (11*17*5*13*19*2*3*7) to the ops parameter" to run this with 10000 rounds
    monkeys = [
        Monkey(
            0,
            [98, 97, 98, 55, 56, 72],
            lambda x: (x * 13) // 1,
            lambda x: 4 if x % 11 == 0 else 7,
        ),
        Monkey(
            1,
            [73, 99, 55, 54, 88, 50, 55],
            lambda x: (x + 4) // 1,
            lambda x: 2 if x % 17 == 0 else 6,
        ),
        Monkey(
            2,
            [67, 98],
            lambda x: (x * 11) // 1,
            lambda x: 6 if x % 5 == 0 else 5,
        ),
        Monkey(
            3,
            [82, 91, 92, 53, 99],
            lambda x: (x + 8) // 1,
            lambda x: 1 if x % 13 == 0 else 2,
        ),
        Monkey(
            4,
            [52, 62, 94, 96, 52, 87, 53, 60],
            lambda x: (x * x) // 1,
            lambda x: 3 if x % 19 == 0 else 1,
        ),
        Monkey(
            5,
            [94, 80, 84, 79],
            lambda x: (x + 5) // 1,
            lambda x: 7 if x % 2 == 0 else 0,
        ),
        Monkey(6, [89], lambda x: (x + 1) // 1, lambda x: 0 if x % 3 == 0 else 5),
        Monkey(
            7,
            [70, 59, 63],
            lambda x: (x + 3) // 1,
            lambda x: 4 if x % 7 == 0 else 3,
        ),
    ]
    game = Keep_Away(monkeys)
    game.play(10)

    print(operator.mul(*(sorted(map(lambda x: x.inspections, monkeys))[-2:])))
