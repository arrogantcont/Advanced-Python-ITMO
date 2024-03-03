import sys

try:
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "r") as f:
                lines = f.readlines()[-10:]
            if len(sys.argv) > 2:
                print(f"==> {filename} <==")
            print("".join(lines), end="\n\n")
    else:
        try:
            lines = sys.stdin.readlines()[-17:]
            print("".join(lines), end="")
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            print("".join(lines), end="")


except FileNotFoundError:
    print("Please provide path to valid text files")
