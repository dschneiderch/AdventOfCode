# %%
from pathlib import Path

import numpy as np

# %%
input_data = Path(__file__).parent.joinpath("input.txt").read_text()
input_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

lines = input_data.strip().splitlines()

# %%

A = np.array([[1, 1, 1], [2, 4, 8], [3, 9, 27]])
# print(A)
b3 = np.array([3, 6, 11])
b2 = np.array([2, 5, 9])
b1 = np.array([3, 6, 9])
print(np.linalg.solve(A, b1))
print(np.linalg.solve(A, b2))
print(np.linalg.solve(A, b3))

# %%
matrix_size = max(len(line.split()) for line in lines) - 1

A = np.ones(matrix_size, dtype=np.int64)
for i in np.arange(2, matrix_size + 1):
    # print(i)
    # print(np.arange(matrix_size))
    A = np.vstack((A, np.power(i, np.arange(1, matrix_size + 1), dtype=np.int64)))

print("A", A)
history = []
for line in lines:
    nums = line.split()
    # print(nums)
    intercept = int(nums[0])
    print("intercept", intercept)
    # print(intercept)
    # print(nums[1:])
    b_list = [int(n) - intercept for n in nums[1:]]
    b = np.array(b_list)
    print("b: ", b)
    coefs = np.linalg.solve(A, b)
    coefs[abs(coefs) < 1e-12] = 0
    print("coefs", coefs)
    x = np.power(len(nums), np.arange(1, matrix_size + 1), dtype=np.int64)
    print("x", x)
    y_new = sum(coefs * x) + intercept
    print(round(y_new))
    history.append(round(y_new))

sum(history)


# %% credit to gilippheissler on reddit for showing the symbolic algebra solution. I didn't actually know this was a thing.
from pathlib import Path

import numpy as np
import pandas as pd
import sympy

input_file = Path(__file__).parent.joinpath("input.txt")
arr = np.array(pd.read_csv(input_file, sep=" ", index_col=None, header=None))
(N, L), X, values_out = arr.shape, np.arange(arr.shape[1]), []
for coeffs in arr:
    poly = sympy.polys.specialpolys.interpolating_poly(L, sympy.symbols("x"), X, coeffs)
    values_out.append((poly.subs("x", L), poly.subs("x", -1)))
list(np.array(values_out).sum(axis=0))

# %%

# %%
