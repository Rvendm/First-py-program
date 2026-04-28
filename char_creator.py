

def create_character(character_name, strength, intelligence, charisma):

    if not isinstance(character_name, str):  # to check if the input is not a string
        return 'The character name should be a string'

    elif character_name == "":  # To check if ung character name is hindi blank
        return 'The character should have a name'

    elif len(character_name) > 10:  # checking if the input will not exceed 10 characters
        return 'The character name is too long'

    elif " " in character_name:  # To check if may space ba ang character name
        return 'The character name should not contain spaces'

    # To check if ung mga attributes is not int data type
    if type(strength) is not int or type(intelligence) is not int or type(charisma) is not int:
        return 'All stats should be integers'

    if strength < 1 or intelligence < 1 or charisma < 1:  # checking if ung mga attributes is less than 1
        return 'All stats should be no less than 1'

    if strength > 4 or intelligence > 4 or charisma > 4:  # Checking if ung mga attrib is greater than 4
        return 'All stats should be no more than 4'

    # to check if ung total ng attributes is not  equal to 7 for 7 points
    if sum([strength, intelligence, charisma]) != 7:
        return 'The character should start with 7 points'

    full_dot = '●'
    empty_dot = '○'

    str_bar = (full_dot * strength) + (empty_dot * (10 - strength))

    int_bar = (full_dot * intelligence) + (empty_dot * (10 - intelligence))

    cha_bar = (full_dot * charisma) + (empty_dot * (10 - charisma))

    # mag ouput ng variable values including ung escape na new line
    return f"{character_name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"


# Mag print ng return value sa parameters
print(create_character('ren', 4, 2, 1))
