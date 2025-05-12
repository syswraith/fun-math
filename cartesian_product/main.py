from itertools import product
# importing cartesian product


dataset = [('Lester', 'Roches', 'Nallu', 'Vincent', 'Yogibear'), ('@', '_'), ('007','23')]
# have to typecast the numbers to strings or it doesnt work

passlist = list(product(*dataset))
for pass_tuple in passlist: print(''.join(pass_tuple))
