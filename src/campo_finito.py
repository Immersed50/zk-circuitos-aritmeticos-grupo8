def es_primo(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


class Fp:
    """Cuerpo finito F_p con p primo (uso educativo)."""

    def __init__(self, p: int):
        if not es_primo(p):
            raise ValueError(f"{p} no es primo")
        self.p = p

    def sumar(self, a, b):
        return (a + b) % self.p

    def restar(self, a, b):
        return (a - b) % self.p

    def mult(self, a, b):
        return (a * b) % self.p

    def inverso(self, a):
        if a % self.p == 0:
            raise ZeroDivisionError("0 no tiene inverso")
        return pow(a, -1, self.p)

    def potencia(self, a, e):
        return pow(a, e, self.p)