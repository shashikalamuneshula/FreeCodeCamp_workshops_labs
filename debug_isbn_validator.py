def validate_isbn(isbn, length):
    
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    
    try:
       
        main_digits = isbn[0:length - 1]
        given_check_digit = isbn[length - 1]
        
       
        main_digits_list = [int(digit) for digit in main_digits]
        
        if length == 10:
            if not (given_check_digit.isdigit() or given_check_digit.upper() == 'X'):
                raise ValueError
        else:
            if not given_check_digit.isdigit():
                raise ValueError
                
    except ValueError:
        print('Invalid character was found.')
        return

    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Check if the given check digit matches with the calculated check digit
    if given_check_digit.upper() == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    user_input = input('Enter ISBN and length: ')
    
    # IndexError
    if ',' not in user_input:
        print('Enter comma-separated values.')
        return
        
    values = user_input.split(',')
    isbn = values[0].strip()
    
    # ValueError
    try:
        length = int(values[1].strip())
    except ValueError:
        print('Length must be a number.')
        return

    # IndentationErrors
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')
# main()
