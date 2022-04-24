import sys
import argparse
from caesar_cipher import cipher


def main():
    args = parse_args()
    print(args)
    # Namespace(
    # encode=False, decode=True,
    # file= < _io.TextIOWrapper name = 'sample.txt' mode = 'r' encoding = 'UTF-8' >,
    # text = None,
    # shift = 2,
    # output = None)

    # Check that a direction is given
    if not args.encode and not args.decode:
        while True:
            direction = input(
                "Enter 'e' to encrypt, 'd' to decrypt or 'quit' to cancel:\n").lower()
            if direction == 'e' or direction == 'd':
                break
            elif direction == "quit":
                if args.file:
                    args.file.close()
                if args.output:
                    args.output.close()
                sys.exit("Operation cancelled.")
            else:
                print(f"'{direction}' is not a valid input.")

        args.encode = direction == "e"
        args.decode = direction == "d"

    # Check that there is some input
    if not args.file or not args.text:
        # Ask if input is from a file or direct input typed in the console
        while True:
            read_from_file = input("Use a .txt file as input? yes/no ").lower()
            if read_from_file in ["yes", "y", "no", "n"]:
                read_from_file = True if read_from_file in ["yes", "y"] else False
                break
            else:
                print("Sorry, I didn't get that.")

        # If from file get a file handle and store it in args.file
        if read_from_file:
            file_name = input("File name: ")
            try:
                args.file = open(file_name, 'r', encoding='UTF-8')
            except IOError as error:
                sys.exit(error.strerror)
        # Otherwise, get the input from the console
        else:
            args.text = input("Type your message:\n").lower()  # Modify to preserve casing

    # Validate there is a shift value
    if not args.shift:
        while True:
            shift = int(input("Type the shift number:\n"))
            if shift % 26 == 0:
                print("Multiples of 26 don't make great ciphers! Try again.")
            else:
                break
        args.shift = shift

    if args.file:
        direction = "e" if args.encode else "d"
        if not args.output:
            args.output = open("output.txt", "w", encoding='UTF-8')
        with args.file as reader, args.output as writer:
            for line in reader:
                writer.write(cipher(line, args.shift, direction))
        print(args.output.closed)


def parse_args():
    parser = argparse.ArgumentParser(description="Encode or decode a message using a Caesar cipher.If arguments are "
                                                 "missing or none is given, the application will run in interactive "
                                                 "mode.")

    group_direction = parser.add_mutually_exclusive_group()
    group_direction.add_argument("-e", "--encode", action="store_true")
    group_direction.add_argument("-d", "--decode", action="store_true")

    group_input = parser.add_mutually_exclusive_group()
    group_input.add_argument("-f", "--file", help="Read text input from FILE",
                             type=argparse.FileType('r', encoding="UTF-8"))
    group_input.add_argument("-t", "--text", help="The direct text input")

    parser.add_argument("-s", "--shift", help="The number to shift each letter", type=int)
    parser.add_argument("-o", "--output", help="If present, results are written to the specified output file",
                        type=argparse.FileType('w', encoding="UTF-8"))

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
