import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Encode or decode a message using a Caesar cipher")

    group_direction = parser.add_mutually_exclusive_group(required=True)
    group_direction.add_argument("-e", "--encode", action="store_true")
    group_direction.add_argument("-d", "--decode", action="store_true")

    group_input = parser.add_mutually_exclusive_group()
    group_input.add_argument("-f", "--file", help="Read text input from FILE",
                             type=argparse.FileType('r', encoding="UTF-8"))
    group_input.add_argument("-t", "--text", help="The direct text input")

    parser.add_argument("shift", help="The number to shift each letter", type=int)
    parser.add_argument("-o", "--output", help="If present, results are written to the specified output file",
                        type=argparse.FileType('w', encoding="UTF-8"))

    args = parser.parse_args()

    if args.file:
        with args.file as f_object:
            for line in f_object:
                print(line, end="")

    if args.encode:
        print(args.encode)

    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 4:
        pass
    elif len(sys.argv) == 5 or len(sys.argv) == 6:
        pass
    else:
        pass


def print_usage():
    print('''
    Usage: caesar.py 
       or: caesar.py [-e | -d] [-f input_file | text] shift  [output_file]
        ''')


if __name__ == "__main__":
    main()
