def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    return s[0].isnumeric() + s[1].isnumeric() + s[2].isnumeric() + s[3].isnumeric() + s[4].isnumeric()


print(main("32x3z"))
