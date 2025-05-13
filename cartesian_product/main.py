from itertools import product, permutations

dataset = [('Lester', 'Roches', 'Nallu'), ('@', '_'), ('07', '12', '23')]

# First, get all Cartesian products in the given order
raw_combinations = product(*dataset)
final_passwords = set()

# Add the individual elements themselves to the final password set
for tup in dataset:
    final_passwords.update(tup)

# Now permutate them and add the unique passwords
for combination in raw_combinations:
    for permutation in permutations(combination):
        final_passwords.add(''.join(permutation))

# Generate Cartesian products for all 2-tuple combinations
for i in range(len(dataset)):
    for j in range(i + 1, len(dataset)):
        pair_combinations = product(dataset[i], dataset[j])
        for combination in pair_combinations:
            final_passwords.add(''.join(combination))

# Print all final passwords
for pw in final_passwords:
    print(pw)

