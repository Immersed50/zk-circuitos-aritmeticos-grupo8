from src.r1cs import verificar_r1cs, verificar_con_publico

P = 97
A = [[0,1,0,0,0,0], [0,0,1,0,0,0], [0,1,0,1,0,0], [5,0,0,0,1,0]]
B = [[0,1,0,0,0,0], [0,1,0,0,0,0], [1,0,0,0,0,0], [1,0,0,0,0,0]]
C = [[0,0,1,0,0,0], [0,0,0,1,0,0], [0,0,0,0,1,0], [0,0,0,0,0,1]]


def test_testigo_valido():
    z = [1, 3, 9, 27, 30, 35]
    assert verificar_r1cs(A, B, C, z, P)
    assert verificar_con_publico(A, B, C, z, P, 5, 35)


def test_testigo_inconsistente_se_rechaza():
    z = [1, 3, 9, 27, 30, 36]  # out alterado
    assert not verificar_r1cs(A, B, C, z, P)


def test_testigo_x4_cumple_r1cs_pero_no_el_valor_publico():
    z = [1, 4, 16, 64, 68, 73]  # consistente, pero out = 73
    assert verificar_r1cs(A, B, C, z, P)
    assert not verificar_con_publico(A, B, C, z, P, 5, 35)