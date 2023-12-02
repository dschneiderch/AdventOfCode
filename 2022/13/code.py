#%%
from typing import List
import itertools

#%%
example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

# %%
Packet = List[List | int]


class Packet:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.in_order = None

    def compare_values(self, left, right) -> bool:
        if left <= right:
            return True
        else:
            return False

    def get_integer_integer(self, left, right):

        match left, right:
            case int(), int():
                print("comparing", left, "--", right)
                return left, right
            case list(), int():
                if len(left) != 0:
                    return self.get_integer_integer(left[0], right)
                else:
                    return 0, 1
            case int(), list():
                if len(right) != 0:
                    return self.get_integer_integer(left, right[0])
                else:
                    return 1, 0
            case list(), list():
                if len(right) != 0 and len(left) != 0:
                    return self.get_integer_integer(left[0], right[0])
                elif len(left) == 0:
                    return 0, 1
                elif len(right) == 0:
                    return 1, 0

    def compare_pair(self):
        print(self.left)
        print(self.right)
        left = self.left
        right = self.right
        # print(list(itertools.zip_longest(left, right)))
        while True:
            print(left, right)

            left, right = self.get_integer_integer(left, right)
            in_order = self.compare_values(left, right)
            if in_order is False:
                return False

        return True

    @staticmethod
    def parse_pairs(s: str) -> List[Packet]:
        string_pairs = [x.split() for x in s.split("\n\n")]
        msg = list()
        for l in string_pairs:
            # print(l)
            left = eval(l[0])
            right = eval(l[1])
            pairs = Packet(left, right)
            msg.append(pairs)
        return msg


class Message:
    def __init__(self, packets: List[Packet]):
        self.packets = packets

    def analyze_message(self):
        for i, pair in enumerate(self.packets):
            pair.in_order = pair.compare_pair()
            print(f"pair {i} in order: {pair.in_order}")
        return self


# %%
message = Packet.parse_pairs(example)
results = Message(message).analyze_message()

# %%
#
