import sys
import argparse
from caesar_cipher import cipher


def main():
    args = parse_args()

    # Check that a direction is given
    if not args.encode and not args.decode:
        direction = get_direction(args)

        args.encode = direction == "e"
        args.decode = direction == "d"

    # Check that there is some input
    if not args.file and not args.text:
        get_message(args)

    # Validate there is a key value
    if not args.key:
        get_encoding_key(args)

    direction = "e" if args.encode else "d"
    if args.file:
        if not args.outfile:
            args.outfile = open("output.txt", "w", encoding='UTF-8')
        if args.print:
            prefix = "en" if args.encode else "de"
            print(f"The {prefix}coded text is:")
        with args.file as reader, args.outfile as writer:
            for line in reader:
                writer.write(cipher(line, args.key, direction))
                if args.print:
                    print(cipher(line, args.key, direction), end="")
            if args.print:
                print("\n------------------")
        print(f"Outfile: {args.outfile.name}")

    if args.text:
        # args.text is a list of strings if it comes from command line arguments, string otherwise
        text = " ".join(args.text) if type(args.text) is list else args.text
        print(cipher(text, args.key, direction))
        if args.outfile:
            with args.outfile as writer:
                writer.write(cipher(text, args.key, direction))
            print("------------------")
            print(f"Outfile: {args.outfile.name}")


def get_encoding_key(args):
    while True:
        key = int(input("Type the key number:\n"))
        if key % 26 == 0:
            print("Multiples of 26 don't make great ciphers! Try again.")
        else:
            break
    args.key = key


def get_message(args):
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
        while True:
            write_to_file = input("Write result to a .txt file? yes/no ").lower()
            if write_to_file in ["yes", "y", "no", "n"]:
                write_to_file = True if write_to_file in ["yes", "y"] else False
                break
            else:
                print("Sorry, I didn't get that.")
        if write_to_file:
            while True:
                file_name = input("Enter the name of the output file without extension or press <Enter> to use "
                                  "default name: ")
                if "." not in file_name and " " not in file_name or file_name == "":
                    break
                else:
                    print("Invalid file name, please try again or press ctrl+c to quit the program.")
            if not file_name:
                args.outfile = open("output.txt", "w", encoding='UTF-8')
            else:
                file_name += ".txt"
                args.outfile = open(file_name, "w", encoding='UTF-8')

        args.text = input("Type your message:\n")


def get_direction(args):
    while True:
        direction = input(
            "Enter 'e' to encrypt, 'd' to decrypt or 'quit' to cancel:\n").lower()
        if direction == 'e' or direction == 'd':
            break
        elif direction in ["quit", "q"]:
            if args.file:
                args.file.close()
            if args.outfile:
                args.outfile.close()
            sys.exit("Operation cancelled.")
        else:
            print(f"'{direction}' is not a valid input.")
    return direction


def parse_args():
    parser = argparse.ArgumentParser(description="Encode or decode a message using a Caesar cipher.",
                                     epilog="If arguments are missing or none is given, the application "
                                            "will fill the gaps by running in interactive mode.")

    group_direction = parser.add_mutually_exclusive_group()
    group_direction.add_argument("-e", "--encode", action="store_true")
    group_direction.add_argument("-d", "--decode", action="store_true")

    group_input = parser.add_mutually_exclusive_group()
    group_input.add_argument("-f", "--file", help="Read text input from FILE",
                             type=argparse.FileType('r', encoding="UTF-8"))
    group_input.add_argument("-t", "--text", help="The direct text input", nargs="+")

    parser.add_argument("-k", "--key", help="A number as an encoding key. Values between 1 and 25",
                        type=int, choices=range(1, 26), metavar="1,2,3... 25")

    parser.add_argument("-o", "--outfile", help="If present, results are written to the specified file",
                        type=argparse.FileType('w', encoding="UTF-8"))
    parser.add_argument("-p", "--print", action="store_true", help="Display result in the console. If the input comes "
                                                                   "from text typed in the console, this is the "
                                                                   "default behaviour.")
    # parser.add_argument("-b", "--bar", nargs='+', type=int, choices=range(1, 26), metavar="1,2,3... 25")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
