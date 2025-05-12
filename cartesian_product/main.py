# importing cartesian product
from itertools import product, permutations


# have to typecast the numbers to strings or it doesnt work
dataset = [('Lester', 'Roches', 'Nallu', 'Vincent', 'Yogibear'), ('@', '_'), ('007','23')]

# first, get all cartesial products in the given order
raw_combinations = product(*dataset)
final_passwords = set()

for combination in raw_combinations:
    # now permutate them
    for permutation in permutations(combination):
        final_passwords.add(''.join(permutation))

for pw in final_passwords: print(pw)
