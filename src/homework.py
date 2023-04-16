def cool_piecewise_function(x: float) -> int | float | None:
    """
    Уривчаста і кусково-задана математична функція
    :param x: аргумент функції
    :return: значення функції
    """
    if x < -6:
        return 25
    elif -5 < x < 2:
        return x ** 2
    elif x >= 2:
        return -5 * (x - 2) + 4
    if -6 < x < -5:
        return None
