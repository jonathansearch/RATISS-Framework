from ratiss.residual import part_du_reste, plancher_valide


def test_meuble_seul_donne_zero():
    assert part_du_reste([(0.0, 2.0, 0.0), (0.0, -1.0, 0.0)], [1]) == 0.0


def test_reste_pondere():
    assert abs(part_du_reste([(1.0, 3.0, 0.0)], [1]) - 0.1) < 1e-12
    assert abs(part_du_reste([(1.0, 0.0, 0.0), (0.0, 1.0, 0.0)], [1], poids=[3.0, 1.0]) - 0.75) < 1e-12


def test_plancher():
    assert plancher_valide(0.0, 0.0019)
    assert not plancher_valide(0.001, 0.0019)
    assert not plancher_valide(0.0, 0.0)
