from functools import reduce


def rule_of_sum(event_space):
    """
    Calculates the chance of n independent events (n_1 AND n_2 AND ... n_i) occurring.
    """
    return reduce((lambda x, y: x + y), event_space)
