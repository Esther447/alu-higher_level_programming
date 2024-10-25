def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        value = roman_numerals[roman_string[i]]
        # Check if the next numeral exists and is greater than the current numeral
        if i + 1 < length and roman_numerals[roman_string[i + 1]] > value:
            total -= value  # Subtract if the next numeral is greater
        else:
            total += value  # Add otherwise

    return total
