from gyrovectors import Array


def mob_add(u: Array, v: Array, s: float, back) -> Array:
    _dot = back.dot(u, v)
    _norm_square_u = back.sum(back.square(u), axis=-1)
    _norm_square_v = back.sum(back.square(v), axis=-1)

    _numerator = (1 + (2 * _dot + _norm_square_v) / s**2) * u
    _numerator += (1 - _norm_square_u / s**2) * v

    _denominator = 1 + (2 * _dot + _norm_square_u * _norm_square_v / s**2) / s**2

    return _numerator / _denominator


def mob_multiply(r: float, v: Array, s: float, back) -> Array:
    _norm_v = back.sqrt(back.sum(back.square(v), axis=-1))
    _ratio = _norm_v / s

    _numerator = s * ((1 + _ratio) ** r - (1 - _ratio) ** r) * v
    _denominator = ((1 + _ratio) ** r + (1 - _ratio) ** r) * _norm_v

    return _numerator / _denominator


def mob_coadd(u: Array, v: Array, s: float, back) -> Array:
    _gamma_u = gamma(u, s, back)
    _gamma_v = gamma(v, s, back)

    _numerator = _gamma_u**2 * u + _gamma_v**2 * v
    _denominator = _gamma_u**2 + _gamma_v**2 - 1

    return _numerator / _denominator


def gamma(u: Array, s: float, back) -> float:
    _norm_square_u = back.sum(back.square(u), axis=-1)
    _ratio = _norm_square_u / s**2
    return 1 / back.sqrt(1 - _ratio)
