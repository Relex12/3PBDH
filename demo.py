from random import randint
from math import sqrt
from argparse import ArgumentParser

from classes import *

parser = ArgumentParser()
parser.add_argument("-v", "--version", action="version", version='1.0')
parser.add_argument("-p", "--prime", metavar='PRIME', type=int, default=37, help="")    # 997, 509, 37
parser.add_argument("-g", "--generator", metavar='NUM', type=int, default=7, help="")
parser.add_argument("-a", metavar='NUM', type=int, default=-2, help="")
parser.add_argument("-b", metavar='NUM', type=int, default=4, help="")
parser.add_argument("-m", "--max-key", metavar='NUM', type=int, default=1000, help="")
parser.add_argument("-c", "--continuous", action='store_true', help="")
parser.add_argument("-d", "--debug", action='store_true', help="")
parser.add_argument("-P", "--plot", action='store_true', help="")
args = parser.parse_args()


# ka, kb and kc randomly chosen by Alice, Bob and Charles
print ('Private keys')
ka = randint(1, args.max_key)
kb = randint(1, args.max_key)
kc = randint(1, args.max_key)
print(f'ka = {ka}')
print(f'kb = {kb}')
print(f'kc = {kc}')

print ('RSA cryptography')
# p and g are aggreed before the exchange
p = args.prime
g = args.generator
if args.debug:
    print (f'p = {p}, g = {g}')

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


if args.continuous:
    print ('Elliptic curve cryptography')
    a = -2 # args.a
    b = 4  # args.b
    curve = EllipticCurve(a, b)
    if args.debug:
        print(curve)
    if args.plot:
        curve.plot(20)

    G = Point(curve, frac(3), frac(5), 'G')
    if args.debug:
        print(f'G = {G}')
    if args.plot:
        G.plot()

    print ('Public keys')
    kA = (ka*G)
    kB = (kb*G)
    kC = (kc*G)
    print(f'kA = {kA}')
    print(f'kB = {kB}')
    print(f'kC = {kC}')
    if args.plot:
        kA.plot('kA')
        kB.plot('kB')
        kC.plot('kC')

    print ('Pairwise session keys')
    kab = ka*kb*G
    kba = kb*ka*G
    kac = ka*kc*G
    kca = kc*ka*G
    kbc = kb*kc*G
    kcb = kc*kb*G
    print(f'kab = {kab}')
    print(f'kba = {kba}')
    print(f'kac = {kac}')
    print(f'kca = {kca}')
    print(f'kbc = {kbc}')
    print(f'kcb = {kcb}')
    if args.plot:
        kab.plot('kab')
        kac.plot('kac')
        kbc.plot('kbc')

    print ('Three partite session keys, expected result')
    kabc1 = ka*kb*kc*G
    kbca1 = kb*kc*ka*G
    kcab1 = kc*ka*kb*G
    print(f'kabc1 = {kabc1}')
    print(f'kbca1 = {kbca1}')
    print(f'kcab1 = {kcab1}')
    if args.plot:
        kabc1.plot('kabc1')

    if args.plot:
        plt.savefig("graph_continuous.png")


print ('Elliptic curve over finite fileds cryptography')
a = -5 # args.a
b = 8  # args.b
p = 509 # args.p, no need to redefine
curve = FiniteEllipticCurve(a, b, p)
if args.debug:
    print(curve)
if args.plot:
    curve.plot()

G = FinitePoint(curve, 1, 507, 'G')
if args.debug:
    print(f'G = {G}')
if args.plot:
    G.plot()

print ('Public keys')
kA = (ka*G)
kB = (kb*G)
kC = (kc*G)
print(f'kA = {kA}')
print(f'kB = {kB}')
print(f'kC = {kC}')
if args.plot:
    kA.plot('kA')
    kB.plot('kB')
    kC.plot('kC')

print ('Pairwise session keys')
kab = ka*kb*G
kba = kb*ka*G
kac = ka*kc*G
kca = kc*ka*G
kbc = kb*kc*G
kcb = kc*kb*G
print(f'kab = {kab}')
print(f'kba = {kba}')
print(f'kac = {kac}')
print(f'kca = {kca}')
print(f'kbc = {kbc}')
print(f'kcb = {kcb}')
if args.plot:
    kab.plot('kab')
    kac.plot('kac')
    kbc.plot('kbc')

print ('Three partite session keys, expected result')
kabc1 = ka*kb*kc*G
kbca1 = kb*kc*ka*G
kcab1 = kc*ka*kb*G
print(f'kabc1 = {kabc1}')
print(f'kbca1 = {kbca1}')
print(f'kcab1 = {kcab1}')
if args.plot:
    kabc1.plot('kabc1')

if args.plot:
    plt.savefig("graph_finite.png")
