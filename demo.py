#!/usr/bin/env python3

from random import randint
from math import sqrt
from argparse import ArgumentParser

from classes import *


def solve_ecc(a, b, p=None):
    ret_list = []
    x = 1
    if p != None:
        for i in range (p):
            y = sqrt((x**3 + a*x + b) % p)
            if y.is_integer():
                ret_list.append((x,int(y)))
            x+=1
    else:
        for i in range (10**5):
            y = sqrt(x**3 + a*x + b)
            if y.is_integer():
                ret_list.append((x,int(y)))
            x+=1
    return ret_list


parser = ArgumentParser()
parser.add_argument("-v", "--version", action="version", version='1.0')
parser.add_argument("-p", "--prime", metavar='PRIME', type=int, default=509, help="prime number used for modulo in RSA and Finite fields ECC")
parser.add_argument("-g", "--generator", metavar='NUM', type=int, default=7, help="number used for Diffie-Hellman exchange")
parser.add_argument("-a", metavar='NUM', type=int, default=-2, help="coefficient a of the Weierstrass form")
parser.add_argument("-b", metavar='NUM', type=int, default=4, help="coefficient b of the Weierstrass form")
parser.add_argument("-m", "--max-key", metavar='NUM', type=int, default=1000, help="maximum value for random private key generation")
parser.add_argument("-c", "--continuous", action='store_true', help="run the regular Elliptic Curve take quite a long")
parser.add_argument("-d", "--debug", action='store_true', help="print additionnal information")
parser.add_argument("-P", "--plot", action='store_true', help="plot graph with curve and points")
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
print(f'kab = {(kB**ka) % p}')
print(f'kba = {(kA**kb) % p}')
print(f'kac = {(kC**ka) % p}')
print(f'kca = {(kA**kc) % p}')
print(f'kbc = {(kC**kb) % p}')
print(f'kcb = {(kB**kc) % p}')

# kabc, kbca and kcab computed by Alice, Bob and Charles are multipartite secret keys
print ('Three partite session keys, first attempt')
print(f'kabc1 = {(kB**ka * kC**ka) % p}')
print(f'kbca1 = {(kA**kb * kC**kb) % p}')
print(f'kcab1 = {(kA**kc * kB**kc) % p}')

print ('Three partite session keys, second attempt')
print(f'kabc2 = {((kB+kC)**ka) % p}')
print(f'kbca2 = {((kA+kC)**kb) % p}')
print(f'kcab2 = {((kA+kB)**kc) % p}')

print ('Three partite session keys, third attempt')
print(f'kabc4 = {(kB**ka + kC**ka) % p}')
print(f'kbca4 = {(kA**kb + kC**kb) % p}')
print(f'kcab4 = {(kA**kc + kB**kc) % p}')


if args.continuous:
    print ('Elliptic curve cryptography')
    a = args.a
    b = args.b
    curve = EllipticCurve(a, b)
    if args.debug:
        print(curve)
    if args.plot:
        curve.plot(20)

    solutions = solve_ecc(a, b)
    if solutions == []:
        raise Error(f'Curve {curve} does not seem to have solutions.')
    x, y = solutions[0]
    G = Point(curve, frac(x), frac(y), 'G')
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
    kab = ka*kB
    kba = kb*kA
    kac = ka*kC
    kca = kc*kA
    kbc = kb*kC
    kcb = kc*kB
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

    print ('Three partite session keys, first attempt')
    print ('debug')
    kabc1 = ka*(kB+kC)
    kbca1 = kb*(kC+kA)
    kcab1 = kc*(kA+kB)
    print(f'kabc1 = {kabc1}')
    print(f'kbca1 = {kbca1}')
    print(f'kcab1 = {kcab1}')
    if args.plot:
        kabc1.plot('kabc1')
        kbca1.plot('kbca1')
        kcab1.plot('kcab1')

    if args.plot:
        plt.savefig("graph_continuous.png")


print ('Elliptic curve over finite fileds cryptography')
a = args.a
b = args.b
p = args.prime
curve = FiniteEllipticCurve(a, b, p)
if args.debug:
    print(curve)
if args.plot:
    curve.plot()

solutions = solve_ecc(a, b, p)
if solutions == []:
    raise Error(f'Curve {curve} does not seem to have solutions.')
x, y = solutions[0]
G = FinitePoint(curve, x, y, 'G')
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
kab = ka*kB
kba = kb*kA
kac = ka*kC
kca = kc*kA
kbc = kb*kC
kcb = kc*kB
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

print ('Three partite session keys, first attempt')
print ('debug')
kabc1 = ka*(kB+kC)
kbca1 = kb*(kC+kA)
kcab1 = kc*(kA+kB)
print(f'kabc1 = {kabc1}')
print(f'kbca1 = {kbca1}')
print(f'kcab1 = {kcab1}')
if args.plot:
    kabc1.plot('kabc1')
    kbca1.plot('kbca1')
    kcab1.plot('kcab1')

if args.plot:
    plt.savefig("graph_discrete.png")
