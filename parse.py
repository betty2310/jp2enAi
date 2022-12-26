def parse(str):
    result = ""
    for character in str:
        if character.isdigit():
            result += "\n" + character
        else:
            result += character
    return result
