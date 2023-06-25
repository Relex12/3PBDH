from random import randint

# p and g are aggreed before the exchange
p = 997
g = 7

# a, b and c randomly chosen by Alice, Bob and Charles
a = randint(10, 1000)
b = randint(10, 1000)
c = randint(10, 1000)

print ('Private keys')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

# A, B and C computed by Alice, Bob and Charles
A = (g**a) % p
B = (g**b) % p
C = (g**c) % p

print ('Public keys')
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

print ('Pairwise session keys')
print(f'kab = {kab}')
print(f'kba = {kba}')
print(f'kac = {kac}')
print(f'kca = {kca}')
print(f'kbc = {kbc}')
print(f'kcb = {kcb}')

# kabc, kbac and kcab computed by Alice, Bob and Charles are multipartite secret keys
kabc1 = (B**a * C**a) % p
kbac1 = (A**b * C**b) % p
kcac1 = (A**c * B**c) % p

print ('Three partite session keys, first attempt')
print(f'kabc1 = {kabc1}')
print(f'kbac1 = {kbac1}')
print(f'kcac1 = {kcac1}')


kabc2 = ((B+C)**a) % p
kbac2 = ((A+C)**b) % p
kcac2 = ((A+B)**c) % p

print ('Three partite session keys, second attempt')
print(f'kabc2 = {kabc2}')
print(f'kbac2 = {kbac2}')
print(f'kcac2 = {kcac2}')


kabc3 = ((B*C)**a) % p
kbac3 = ((A*C)**b) % p
kcac3 = ((A*B)**c) % p

print ('Three partite session keys, third attempt')
print(f'kabc3 = {kabc3}')
print(f'kbac3 = {kbac3}')
print(f'kcac3 = {kcac3}')


kabc4 = (B**a + C**a) % p
kbac4 = (A**b + C**b) % p
kcac4 = (A**c + B**c) % p

print ('Three partite session keys, fourth attempt')
print(f'kabc4 = {kabc4}')
print(f'kbac4 = {kbac4}')
print(f'kcac4 = {kcac4}')

