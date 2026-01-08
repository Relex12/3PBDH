#!/usr/bin/env python3

# TODO: this script must still be investigated to understand the underlying behavior

"""
demo_3p_nike.py
Démonstrateur pédagogique : 3-party Non-Interactive Key Exchange (Joux 2004)
avec un couplage bilinéaire SIMULÉ (pour prouver mathématiquement la propriété).
ATTENTION : SIMULATION didactique — NON SÉCURISÉ pour usage réel.
"""

from random import randint
from argparse import ArgumentParser

# ---- Paramètres simples ----
# r est l'ordre (on travaille modulo r pour les exposants)
# Choisir un r suffisamment grand pour la démonstration (ici 2^31-1 est bon pour test rapide)
DEFAULT_R = 2**31 - 1

class SimulatedGroupElement:
    """
    Représentation pédagogique d'un élément du groupe G = <g>.
    On conserve explicitement l'exposant 'exp' tel que l'élément = g^exp.
    L'opération de groupe est la somme des exposants modulo r.
    """
    def __init__(self, exp: int, r: int):
        self.exp = exp % r
        self.r = r

    def __mul__(self, other):
        # multiplication dans le groupe correspond à addition des exposants modulo r
        if not isinstance(other, SimulatedGroupElement):
            raise TypeError("other must be SimulatedGroupElement")
        if self.r != other.r:
            raise ValueError("different moduli")
        return SimulatedGroupElement((self.exp + other.exp) % self.r, self.r)

    def __pow__(self, n: int):
        # exponentiation: (g^exp)^n = g^{exp * n}
        return SimulatedGroupElement((self.exp * n) % self.r, self.r)

    def __eq__(self, other):
        return isinstance(other, SimulatedGroupElement) and self.exp == other.exp and self.r == other.r

    def __repr__(self):
        return f"<g^{self.exp} mod r={self.r}>"

class SimulatedPairing:
    """
    Couplage bilinéaire simulé e: G1 x G2 -> GT
    Si P corresponds à exposant p_exp dans G1/G2 et Q à q_exp, alors:
      e(P,Q) est représenté par exposant (p_exp * q_exp) mod r dans GT.
    GT est représenté par même type SimulatedGroupElement (exposant modulo r).
    """
    def __init__(self, r: int):
        self.r = r

    def pair(self, P: SimulatedGroupElement, Q: SimulatedGroupElement):
        if P.r != self.r or Q.r != self.r:
            raise ValueError("mismatched modulus r")
        return SimulatedGroupElement((P.exp * Q.exp) % self.r, self.r)

# ---- Protocole Joux 3-party (simulation) ----
def trois_parties_nike_simulation(ka, kb, kc, r):
    """
    ka,kb,kc : clefs privées (entiers)
    r : ordre modulo (entier)
    Retourne la clé partagée (SimulatedGroupElement) calculée par chaque partie.
    """
    # Base point P (on le représente par exposant 1 : P = g^1)
    P = SimulatedGroupElement(1, r)

    # Génération des clés publiques : kA = ka * P = g^{ka}
    kA = P ** ka
    kB = P ** kb
    kC = P ** kc

    pairing = SimulatedPairing(r)

    # Joux 3-party : chaque participant calcule e(k_j, k_k)^{k_i}
    # Alice computes e(kB, kC)^{ka} = e(P,P)^{ka*kb*kc}
    e_BC = pairing.pair(kB, kC)          # e(kB, kC) => exponent kb*kc
    K_A = e_BC ** ka                     # raise to ka => exponent ka*kb*kc

    # Bob computes e(kC, kA)^{kb}
    e_CA = pairing.pair(kC, kA)
    K_B = e_CA ** kb

    # Charlie computes e(kA, kB)^{kc}
    e_AB = pairing.pair(kA, kB)
    K_C = e_AB ** kc

    return {
        "P": P,
        "kA": kA, "kB": kB, "kC": kC,
        "KA": K_A, "KB": K_B, "KC": K_C
    }

def main():
    parser = ArgumentParser(description="Démonstration 3P-NIKE (simulation pairing).")
    parser.add_argument("-r", "--order", type=int, default=DEFAULT_R, help="ordre r (modulo pour exposants)")
    parser.add_argument("-m", "--max-key", type=int, default=10**6, help="valeur max pour les clés privées (aléatoires)")
    parser.add_argument("--ka", type=int, help="clé privée Alice (optionnelle)")
    parser.add_argument("--kb", type=int, help="clé privée Bob (optionnelle)")
    parser.add_argument("--kc", type=int, help="clé privée Charlie (optionnelle)")
    args = parser.parse_args()

    r = args.order
    if args.ka is None:
        ka = randint(1, args.max_key)
    else:
        ka = args.ka
    if args.kb is None:
        kb = randint(1, args.max_key)
    else:
        kb = args.kb
    if args.kc is None:
        kc = randint(1, args.max_key)
    else:
        kc = args.kc

    print("Paramètres (simulation) :")
    print(f"  ordre r = {r}")
    print(f"  clés privées : ka={ka}, kb={kb}, kc={kc}")

    res = trois_parties_nike_simulation(ka, kb, kc, r)

    print("\nPoints et clés publiques (représentés par exposants) :")
    print(f"  P = {res['P']}")
    print(f"  kA = {res['kA']}")
    print(f"  kB = {res['kB']}")
    print(f"  kC = {res['kC']}")

    print("\nChaque participant calcule la clé partagée (exposant) :")
    print(f"  Alice K_A = {res['KA']} (exposant = {res['KA'].exp})")
    print(f"  Bob   K_B = {res['KB']} (exposant = {res['KB'].exp})")
    print(f"  Charlie K_C= {res['KC']} (exposant = {res['KC'].exp})")

    equal = (res['KA'] == res['KB'] == res['KC'])
    print(f"\nToutes les clés sont égales ? {'OUI' if equal else 'NON'}")
    if equal:
        print("Clé partagée (exposant) =", res['KA'].exp)
        print("-> valeur simulée : g^{exposant} (abstrait)")
    else:
        print("ERREUR : les clés diffèrent, ce qui ne devrait pas arriver dans cette démonstration.")

if __name__ == "__main__":
    main()
