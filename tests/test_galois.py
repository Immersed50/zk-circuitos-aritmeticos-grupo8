import galois


def test_galois_instalacion_y_aritmetica():
    GF = galois.GF(97)
    x = GF(3)
    assert x * x * x + x + GF(5) == GF(35)


def test_galois_coincide_con_campo_finito_propio():
    from src.campo_finito import Fp
    GF = galois.GF(97)
    F = Fp(97)
    for a in range(1, 97):
        assert int(GF(a) ** -1) == F.inverso(a)