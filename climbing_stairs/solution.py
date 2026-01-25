memo = {}
def climb_stairs(steps: int):
    """
    >> climb_stairs(5)
    """
    if steps in memo:
        return memo[steps]
    if steps == 0:
        return 0
    if steps == 1:
        return 1
    memo[steps] = climb_statirs(steps - 2) + climb_stairs(steps - 1)
    return memo[steps]
