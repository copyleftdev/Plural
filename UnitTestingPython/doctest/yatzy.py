
def small_straight(dice):
    """Score the given roll in the 'Small Straight' Yatsy Category.

    Args:
        dice: a sorted list of 5 integers indicating the dice rolled

    Returns:
        an integer score

    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,4,4])
    0
    >>> small_straight({1,2,3,4,5})
    0
    >>> small_straight([1,2,3,4])
    0
    >>> small_straight([5,4,3,2,1])
    0

    """
    if dice == [1, 2, 3, 4, 5]:
        return sum(dice)
    else:
        return 0
