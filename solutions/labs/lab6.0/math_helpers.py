def smart_divide(numerator, denominator):
    if denominator is None:
        return 0
    elif False == denominator:
        return 0
    elif numerator is None:
        return 0
    elif False == numerator:
        return 0
    return numerator / denominator