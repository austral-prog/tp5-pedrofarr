def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    return x if x > y else y


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    return max_of_two(x, max_of_two(y, z))