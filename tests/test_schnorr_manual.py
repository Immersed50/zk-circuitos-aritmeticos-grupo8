def test_schnorr_manual():
    p, q, g, x = 23, 11, 4, 6
    assert pow(g, q, p) == 1          # g tiene orden q
    y = pow(g, x, p)
    r, c = 7, 4
    t = pow(g, r, p)
    s = (r + c * x) % q
    assert y == 2 and t == 8 and s == 9
    assert pow(g, s, p) == (t * pow(y, c, p)) % p