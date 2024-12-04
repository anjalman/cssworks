def roman_to_int(roman):

    roman_number={
        'I': 1, 'V': 5, 'X': 10, 'L':50, 'c':100, 'D': 500, 'M': 1000
    }

    decimal=0

    prev_value=0

    for char in reversed(roman):

        current_value=roman_number[char]

        if current_value < prev_value:

            decimal-=current_value

        else:

            decimal+=current_value

        prev_value=current_value

    return decimal

print(roman_to_int("DDVIIXX"))