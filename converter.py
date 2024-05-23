import sys

def decimal_to_other_base(quotient, divisor):
    result = ''
    while quotient > 0:
        quotient, remainder = divmod(quotient, divisor)
        result = str(remainder) + result
    return result

def other_base_to_decimal(initial_number, number_base):
     initial_number_clean = str(initial_number)
    # Reverse to start from the least significant digit on the next line
     digits = [int(char) for char in initial_number_clean[::-1]] 
     powers = range(len(digits)) 
     decimal_value = 0
     for digit, power in zip(digits, powers):
         decimal_value += digit * (number_base ** power)
     return decimal_value
     

def number_base_converter(initial_number, number_base, conversion_number_base):
    quotient = int(initial_number)
    number_base = int(number_base)
    divisor = int(conversion_number_base)
    if number_base == 10 and divisor != 10:
        result = decimal_to_other_base(quotient, divisor)
        return result
        print('Result:', result)
    elif number_base != 10 and divisor == 10:
        return other_base_to_decimal(quotient, number_base)
    else:
        decimal_value = other_base_to_decimal(quotient, number_base)
        return decimal_to_other_base(decimal_value, divisor)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python base_converter.py initial_number number_base conversion_number_base")
        sys.exit(1)
    
    initial_number = sys.argv[1]
    number_base = sys.argv[2]
    conversion_number_base = sys.argv[3]

    result = number_base_converter(initial_number, number_base, conversion_number_base)
    print('Result:', result)