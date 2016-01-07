#!/usr/bin/env python
import string


def parse_int(number):
    """
    returns an integer if the string input is an int, otherwise throws and exception
    :param number: String that represents an integer
    :return an integer corresponding to the string input,
    """
    digit_set = set(list(string.digits))
    total = 0
    integer_multiplier = 1
    for i in range(len(number) - 1, -1, -1):
        if number[i] in digit_set:
            total += int(number[i]) * integer_multiplier
            integer_multiplier *= 10
        else:
            raise ValueError("not an integer parameter")
    return total

def parse_double(number):
    comps = number.split(".")
    comps_len = len(comps)
    if comps_len == 2:  # if it is a legitimate double
        try:
            integer = parse_int(comps[0])
            decimal = parse_int(comps[1])
        except:
            raise ValueError("not a valid decimal parameter")
        decimal /= 10 ** len(comps[1])
        return decimal + integer
    elif comps_len == 1:
        try:
            integer = parse_int(number)
        except:
            raise ValueError("not a valid decimal parameter")
        return float(integer)
    else:
        raise ValueError("not a valid decimal parameter")

print("number: ", parse_double(input("enter number: ")))
