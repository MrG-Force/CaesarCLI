import string


def main():
    print(cipher("H", 89, "encode"))


def cipher(message, shift, direction):
    # prefix = "en" if direction == "encode" else "de"
    d = 1 if direction == "e" else -1
    uppers = string.ascii_uppercase
    lowers = string.ascii_lowercase
    result = ""

    for char in message:
        if not char.isalpha():
            result += char
        else:
            alphabet = uppers if char.isupper() else lowers
            index = alphabet.index(char)
            shift_indx = index + shift * d
            if shift_indx >= len(alphabet) or shift_indx < 0:
                shift_indx = shift_indx % len(alphabet)
            result += alphabet[shift_indx]

    return result


if __name__ == "__main__":
    main()
