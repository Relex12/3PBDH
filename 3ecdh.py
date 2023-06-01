from random import randint

# p and g are aggreed before the exchange
p = 997
g = 7

# # a and b randomly chosen by Alice and Bob
# a = randint(10, 1000)
# b = randint(10, 1000)

# print(f'a = {a}')
# print(f'b = {b}')

# # A and B computed by Alice and Bob
# A = (g**a) % p
# B = (g**b) % p

# print(f'A = {A}')
# print(f'B = {B}')

# # ka and kb computed by Alice and Bob using each other's B and A
# ka = (B**a) % p
# kb = (A**b) % p

# print(f'ka = {ka}')
# print(f'kb = {kb}')

# print('###################')

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

# ka, kb and kc computed by Alice, Bob and Charles using each other's C, B and A
ka = (B**a * C**a) % p
kb = (A**b * C**b) % p
kc = (A**c * B**c) % p

print(f'ka = {ka}')
print(f'kb = {kb}')
print(f'kc = {kc}')
