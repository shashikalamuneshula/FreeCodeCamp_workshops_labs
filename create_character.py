def create_character(name, str_val, int_val, cha_val):
    # 1. Check if name is a string
    if not isinstance(name, str):
        return "The character name should be a string"

    # 2. Check if name is empty
    if name == '':
        return "The character should have a name"

    # 3. Check if name length is more than 10 characters
    if len(name) > 10:
        return "The character name is too long"
    # 4. Check if name contains spaces
    if ' ' in name:
        return "The character name should not contain spaces"

    # 5. Check if all stats are integers
    if type(str_val) is not int or type(int_val) is not int or type(cha_val) is not int:
        return "All stats should be integers"

    # 6. Check if any stat is less than 1
    if str_val < 1 or int_val < 1 or cha_val < 1:
        return "All stats should be no less than 1"

    # 7. Check if any stat is more than 4
    if str_val > 4 or int_val > 4 or cha_val > 4:
        return "All stats should be no more than 4"

    # 8. Check if stats sum up to exactly 7
    if str_val + int_val + cha_val != 7:
        return "The character should start with 7 points"

    # 9. Format and return the visual character stats profile
    def make_stars(score):
        return '●' * score + '○' * (10 - score)

    return f"{name}\nSTR {make_stars(str_val)}\nINT {make_stars(int_val)}\nCHA {make_stars(cha_val)}"


# Calling the function and printing the output
print(create_character('ren', 4, 2, 1))
