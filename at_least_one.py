import itertools

# TODO: Why does this error in my local vs code? Probably an issue with root folders?
from product_rule import product_rule


def at_least_one(*args: float) -> float:
    """
    Given a series of probabilities as input, this function will return the probability that
    *at least one* of these input events occurs.
    """

    output_probabilities = []

    for nth_length in range(1, len(args) + 1):
        modifier = -1 if nth_length % 2 == 0 else 1
        for event in itertools.combinations(args, nth_length):
            output_probabilities.append(modifier * product_rule(event))

    # TODO: how to dynamically avoid rounding issues (e.g. 0.6975999999999999 instead of 0.6976)
    return sum(output_probabilities)
