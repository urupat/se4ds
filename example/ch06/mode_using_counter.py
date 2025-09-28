from collections import Counter

def mode_using_counter(list_of_numbers: list) -> float:
    c = Counter(list_of_numbers)
    return c.most_common(1)[0][0]

