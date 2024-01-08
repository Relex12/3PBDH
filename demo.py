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

# kabc, kbca and kcab computed by Alice, Bob and Charles are multipartite secret keys
kabc1 = (B**a * C**a) % p
kbca1 = (A**b * C**b) % p
kcab1 = (A**c * B**c) % p

print ('Three partite session keys, first attempt')
print(f'kabc1 = {kabc1}')
print(f'kbca1 = {kbca1}')
print(f'kcab1 = {kcab1}')


kabc2 = ((B+C)**a) % p
kbca2 = ((A+C)**b) % p
kcab2 = ((A+B)**c) % p

print ('Three partite session keys, second attempt')
print(f'kabc2 = {kabc2}')
print(f'kbca2 = {kbca2}')
print(f'kcab2 = {kcab2}')


kabc3 = ((B*C)**a) % p
kbca3 = ((A*C)**b) % p
kcab3 = ((A*B)**c) % p

print ('Three partite session keys, third attempt')
print(f'kabc3 = {kabc3}')
print(f'kbca3 = {kbca3}')
print(f'kcab3 = {kcab3}')


kabc4 = (B**a + C**a) % p
kbca4 = (A**b + C**b) % p
kcab4 = (A**c + B**c) % p

print ('Three partite session keys, fourth attempt')
print(f'kabc4 = {kabc4}')
print(f'kbca4 = {kbca4}')
print(f'kcab4 = {kcab4}')

