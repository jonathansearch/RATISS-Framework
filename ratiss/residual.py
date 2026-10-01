"""L'instrument du reste — R8 : on ne mesure que ce qui déborde du script.

Un montage expérimental impose une partie du signal (le « meuble »). Mesurer le
signal total revient à boulonner le thermomètre sur le radiateur : on retrouve ce
qu'on a imposé. R8 exige de mesurer uniquement la part que le montage n'impose
pas, et de la valider par un témoin sans perturbation (plancher ≈ 0).

Origine : campagne NAVIER MISSION 3D (01/10/2026) — ζ valait 1,0 sans poussière
(signal fabriqué par le meuble) ; la part hors-meuble valait 0,00 % sans poussière
et 0,11 → 0,19 % avec, croissante au raffinement. Stdlib uniquement.
"""
from __future__ import annotations

from typing import Iterable, Sequence


def part_du_reste(vecteurs: Iterable[Sequence[float]], composantes_imposees: Sequence[int],
                  poids: Iterable[float] | None = None) -> float:
    """Fraction (pondérée) de Σ|v|² portée par les composantes NON imposées par le montage.

    >>> part_du_reste([(0.0, 3.0, 0.0)], composantes_imposees=[1])
    0.0
    >>> round(part_du_reste([(1.0, 3.0, 0.0)], composantes_imposees=[1]), 3)
    0.1
    """
    imp = set(composantes_imposees)
    vecteurs = list(vecteurs)
    w = list(poids) if poids is not None else [1.0] * len(vecteurs)
    if len(w) != len(vecteurs):
        raise ValueError("poids et vecteurs de longueurs différentes")
    tot = reste = 0.0
    for v, p in zip(vecteurs, w):
        for k, x in enumerate(v):
            e = p * x * x
            tot += e
            if k not in imp:
                reste += e
    return reste / tot if tot > 0 else 0.0


def plancher_valide(part_temoin: float, part_signal: float, facteur: float = 10.0) -> bool:
    """R8 : le témoin sans perturbation doit être au moins `facteur` fois sous le signal."""
    return part_signal > 0 and part_temoin * facteur <= part_signal
