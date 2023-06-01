from random import randint

# p and g are aggreed before the exchange
p = 997
g = 7

# a, b and c randomly chosen by Alice, Bob and Charles
a = randint(10, 1000)
b = randint(10, 1000)
c = randint(10, 1000)

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

# A, B and C computed by Alice, Bob and Charles
A = (g**a) % p
B = (g**b) % p
C = (g**c) % p

print(f'A = {A}')
print(f'B = {B}')
print(f'C = {C}')

# kab, kba, kac, kca, kbc and kcb computed by Alice, Bob and Charles are pairwise secret keys
kab = (B**a) % p
kba = (A**b) % p
kac = (C**a) % p
kca = (A**c) % p
kbc = (C**b) % p
kcb = (B**c) % p

print(f'kab = {kab}')
print(f'kba = {kba}')
print(f'kac = {kac}')
print(f'kca = {kca}')
print(f'kbc = {kbc}')
print(f'kcb = {kcb}')

# kabc, kbac and kcab computed by Alice, Bob and Charles are multipartite secret keys
kabc = (B**a * C**a) % p
kbac = (A**b * C**b) % p
kcac = (A**c * B**c) % p

print(f'kabc = {kabc}')
print(f'kbac = {kbac}')
print(f'kcac = {kcac}')
