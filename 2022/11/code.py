
from typing import List, Callable


class Monkey:
    def __init__(
        self, id: int, items: List[int], ops: Callable, test: Callable
    ) -> None:
        self.id = id
        self.items = items
        self.ops = ops
        self.test = test


monkeys = [
    Monkey(0, [79, 98], lambda x: x * 19 // 3, lambda x: 2 if x % 23 == 0 else 3),
    Monkey(
        1, [54, 65, 75, 74], lambda x: (x + 6) // 3, lambda x: 2 if x % 19 == 0 else 0
    ),
    Monkey(2, [79, 60, 97], lambda x: (x * x) // 3, lambda x: 1 if x % 13 == 0 else 3),
    Monkey(3, [74], lambda x: (x + 3) // 3, lambda x: 0 if x % 17 == 0 else 1),
]


class Keep_Away:
    def __init__(self, monkeys: List[Monkey]) -> None:
        self.monkeys = monkeys

    def give_item(self, thrown_item, from_monkey, to_monkey):
        # monkey_id = [x for x in self.monkeys if x.id == to_monkey]
        # monkey_id[0].items.append(item)
        new_monkey = list(filter(lambda x: x.id==to_monkey, self.monkeys))
        new_monkey[0].items.append(thrown_item)
        from_monkey.items.pop(0)

    def play(self, rounds):
        for r in range(rounds):
            for m in self.monkeys:
                for i in m.items:
                    self.give_item(i, m, m.test(m.ops(i)))

        [print(x.id, x.items) for x in self.monkeys]

if __name__ == "__main__":

    game = Keep_Away(monkeys)
    game.play(1)