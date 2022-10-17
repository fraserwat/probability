from functools import reduce


def product_rule(event):
    """
    Calculates the chance of n independent events (n_1 OR n_2 OR ... n_i) occurring.
    """
    return reduce((lambda x, y: x * y), event)
