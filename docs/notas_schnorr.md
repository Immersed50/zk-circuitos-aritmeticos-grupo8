# Protocolo de Schnorr: cálculo manual (uso educativo)

Parámetros: p = 23, q = 11, g = 4 (g tiene orden q en F_23). Secreto x = 6.

- Clave pública: y = g^x = 4^6 mod 23 = 2
- Compromiso: r = 7, t = g^r = 4^7 mod 23 = 8
- Desafío: c = 4
- Respuesta: s = r + c·x mod q = 7 + 24 mod 11 = 9
- Verificación: g^s = 4^9 mod 23 = 13 y t·y^c = 8·2^4 = 128 mod 23 = 13. Coinciden, se acepta.

Propiedades:
- Completitud: un probador honesto siempre convence al verificador.
- Solidez: sin conocer x, solo se puede responder bien a un desafío adivinado.
- Conocimiento cero: el verificador no aprende x a partir de (t, c, s).

Fiat–Shamir: se reemplaza el desafío c por un hash de (g, y, t), lo que vuelve el protocolo no interactivo.