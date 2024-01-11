#!/usr/bin/python3
number = 98
print(f"{number} Battery street") if isinstance(number, int) \
    else print(f"ValueError: Unknown format code 'd' for"\
    " object of type '{type(number).__name__}'")
