from itertools import product, permutations, combinations

dataset = [('aryan', 'pravin', 'karekar'), ('@', '_'), ('10', '04', '06')]

final_passwords = set()

# 1. Add individual elements
for tup in dataset:
    final_passwords.update(tup)

# 2. Add intratuple combinations (e.g. aryan+pravin)
for tup in dataset:
    for r in range(2, len(tup) + 1):
        for comb in combinations(tup, r):
            for perm in permutations(comb):
                final_passwords.add(''.join(perm))

# 3. Add full Cartesian product permutations
for combination in product(*dataset):
    for perm in permutations(combination):
        final_passwords.add(''.join(perm))

# 4. Add 2-tuple Cartesian products
for i in range(len(dataset)):
    for j in range(i + 1, len(dataset)):
        for combination in product(dataset[i], dataset[j]):
            final_passwords.add(''.join(combination))

# 5. Add multi-tuple (r >= 2) combinations and permuted products
for r in range(2, len(dataset) + 1):
    for selected in combinations(dataset, r):
        for prod in product(*selected):
            for perm in permutations(prod):
                final_passwords.add(''.join(perm))

# Output
for pw in final_passwords:
    print(pw)

