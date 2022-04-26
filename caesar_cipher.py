import string


def main():
    print(cipher("H", 89, "encode"))


def cipher(message, shift, direction):
    """Return an encrypted or decrypted message using the given shift value as key
        Parameters:
            message (str): the text to decrypt or encrypt
            shift (int): the amount of positions to shift each letter
            direction (str): e for encode, shift forward, d for decode shift backwards

        Returns:
            result (str): the either encrypted or decrypted message
    """
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
