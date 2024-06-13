def count_char_quantity(string: str) -> dict[str, int]:
    result: dict[str, int] = {}
    for char in string:
        if char in result:
            result[char] += 1
            continue

        result[char] = 1

    return result
