from random import randint

# p and g are aggreed before the exchange
p = 997
g = 7

# ka, kb and kc randomly chosen by Alice, Bob and Charles
print ('Private keys')
ka = randint(10, 1000)
kb = randint(10, 1000)
kc = randint(10, 1000)
print(f'ka = {ka}')
print(f'kb = {kb}')
print(f'kc = {kc}')

# kA, kB and kC computed by Alice, Bob and Charles
print ('Public keys')
kA = (g**ka) % p
kB = (g**kb) % p
kC = (g**kc) % p
print(f'kA = {kA}')
print(f'kB = {kB}')
print(f'kC = {kC}')

# kab, kba, kac, kca, kbc and kcb computed by Alice, Bob and Charles are pairwise secret keys
print ('Pairwise session keys')
kab = (kB**ka) % p
kba = (kA**kb) % p
kac = (kC**ka) % p
kca = (kA**kc) % p
kbc = (kC**kb) % p
kcb = (kB**kc) % p
print(f'kab = {kab}')
print(f'kba = {kba}')
print(f'kac = {kac}')
print(f'kca = {kca}')
print(f'kbc = {kbc}')
print(f'kcb = {kcb}')

# kabc, kbca and kcab computed by Alice, Bob and Charles are multipartite secret keys
print ('Three partite session keys, first attempt')
kabc1 = (kB**ka * kC**ka) % p
kbca1 = (kA**kb * kC**kb) % p
kcab1 = (kA**kc * kB**kc) % p
print(f'kabc1 = {kabc1}')
print(f'kbca1 = {kbca1}')
print(f'kcab1 = {kcab1}')

print ('Three partite session keys, second attempt')
kabc2 = ((kB+kC)**ka) % p
kbca2 = ((kA+kC)**kb) % p
kcab2 = ((kA+kB)**kc) % p
print(f'kabc2 = {kabc2}')
print(f'kbca2 = {kbca2}')
print(f'kcab2 = {kcab2}')

print ('Three partite session keys, third attempt')
kabc3 = ((kB*kC)**ka) % p
kbca3 = ((kA*kC)**kb) % p
kcab3 = ((kA*kB)**kc) % p
print(f'kabc3 = {kabc3}')
print(f'kbca3 = {kbca3}')
print(f'kcab3 = {kcab3}')

print ('Three partite session keys, fourth attempt')
kabc4 = (kB**ka + kC**ka) % p
kbca4 = (kA**kb + kC**kb) % p
kcab4 = (kA**kc + kB**kc) % p
print(f'kabc4 = {kabc4}')
print(f'kbca4 = {kbca4}')
print(f'kcab4 = {kcab4}')

