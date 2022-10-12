from gyrovectors import Array
from gyrovectors.operations import mob_add, mob_multiply


def get_gyroline_value(u: Array, v: Array, t: float, s: float, back) -> Array:
    """Returns the corresponding point on the gyroline

    Args:
        u (Array): starting point of the gyroline
        v (Array): end point of the gyroline
        t (float): in [0, 1], position on the gyroline

    Returns:
        The corresponding point on the gyroline (Array)
    """
    return mob_add(u, mob_multiply(t, mob_add(-u, v, s, back), s, back), s, back)
