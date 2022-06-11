# CaesarCLI
A CLI to encode or decode messages using a Caesar Cipher
```
usage: caesar.py [-h] [-e | -d] [-f FILE | -t TEXT [TEXT ...]] [-k 1,2,3... 25] [-o OUTFILE] [-p]

Encode or decode a message using a Caesar cipher.

optional arguments:
  -h, --help            show this help message and exit
  -e, --encode
  -d, --decode
  -f FILE, --file FILE  Read text input from FILE
  -t TEXT [TEXT ...], --text TEXT [TEXT ...]
                        The direct text input
  -k 1,2,3... 25, --key 1,2,3... 25
                        A number as an encoding key. Values between 1 and 25
  -o OUTFILE, --outfile OUTFILE
                        If present, results are written to the specified file
  -p, --print           Display result in the console. If the input comes from text typed in the console, this is the default behaviour.

If arguments are missing or none is given, the application will fill the gaps by running in interactive mode.
```
