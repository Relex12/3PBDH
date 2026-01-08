Définitions des termes utilisés

* on note $\mathbb{F}_p$ le corps fini à $p$ éléments où $p$ est généralement premier, c'est-à-dire $\mathbb{F}_p​=\{0,1,2,...,p−1\}$, les opérations d'addition et de multiplication sur $\mathbb{F}_p$ se font modulo $p$
* on note $E(\mathbb{F}_p)$ une courbe elliptique sur $\mathbb{F}_p$, de la forme $E:y^2=x^3+ax+b$
* on note le cardinal $\#E(\mathbb{F}_p)$ comme le nombre (fini) de points compris de la courbe $E(\mathbb{F}_p)$
* on note $\mathbb{F}_{p^k}$ le corps fini à $p^k$ éléments, par exemple si $k=2$ alors $\mathbb{F}_{p^k}$ est une "grille" à $p^2$ éléments
* on définit $\mathbb{F}^*_{p^k}$ le groupe multiplicatif du corps $\mathbb{F}_{p^k}$ tel que $\mathbb{F}^*_{p^k} = \mathbb{F}_{p^k}\setminus\{0\}$, il contient $p^k-1$ éléments
* on définit l'ordre $r$ de la courbe $E(\mathbb{F}_p)$ le plus grand nombre premier tel que $n = r\cdot h$ où $n=\#E(\mathbb{F}_p)$ et $h$ est un entier
	* si $e$ est un couplage tel que $e:G_1\times G_2 \rightarrow G_T$ avec $G_1\subseteq E(\mathbb{F}_p)$, $G_2\subseteq E(\mathbb{F}_{p^k})$ et $G_T\subseteq \mathbb{F}^*_{p^k}$, alors $r$ est l'ordre du sous-groupe $G_1\subseteq E(\mathbb{F}_p)$
* on définit le degré d'immersion (*embedding degree*) $k$ le plus petit entier positif tel que $r|(p^k-1)$, c'est-à-dire $r$ divise $p^k-1$
	* si $k$ est trop petit, alors le logarithme discret dans $\mathbb{F}_{p^k}$ devient facile à casser
* on note $E'$ une courbe tordue ou twist de $E$ définie sur le même corps $\mathbb{F}_p$ telle que $E'(\mathbb{F}_{p^k})\simeq E'(\mathbb{F}_{p^k})$ mais $E'(\mathbb{F}_p)\not\simeq E'(\mathbb{F}_p)$, c'est-à-dire que $E'$ est isomorphe à $E$ dans $\mathbb{F}_{p^k}$ mais pas dans $\mathbb{F}_p$
	* pour rappel, deux ensembles sont dits isomorphes lorsqu'il existe une application bijective entre eux, il y a donc autant de points dans les deux ensembles

A comprendre $f_P$ (et $f_Q$) : fonction rationnelle en $P$ (et en $Q$)

TODO: poursuivre la compréhension des définitions

---

Pairing-Friendly curves: BN256, BLS12-381

For 128-bit security level:

* BLS12_381
* BN462

For 256-bit security level: BLS48
