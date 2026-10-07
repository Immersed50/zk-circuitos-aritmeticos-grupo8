def producto_punto(fila, z, p):
    return sum(a * b for a, b in zip(fila, z)) % p


def verificar_r1cs(A, B, C, z, p):
    """Comprueba (A_i . z)(B_i . z) = C_i . z (mod p) para toda restriccion i."""
    for a, b, c in zip(A, B, C):
        izq = (producto_punto(a, z, p) * producto_punto(b, z, p)) % p
        if izq != producto_punto(c, z, p):
            return False
    return True


def verificar_con_publico(A, B, C, z, p, indice_salida, salida_publica):
    """R1CS satisfecho Y la salida del vector z coincide con el valor publico."""
    return verificar_r1cs(A, B, C, z, p) and z[indice_salida] % p == salida_publica % p