import pytest
from src.campo_finito import Fp


def test_reduccion_modular():
    F = Fp(97)
    assert F.sumar(90, 10) == 3
    assert F.mult(10, 10) == 3
    assert F.restar(3, 5) == 95


def test_inverso():
    F = Fp(97)
    for a in range(1, 97):
        assert F.mult(a, F.inverso(a)) == 1


def test_inverso_de_cero():
    with pytest.raises(ZeroDivisionError):
        Fp(97).inverso(0)


def test_p_no_primo():
    with pytest.raises(ValueError):
        Fp(15)