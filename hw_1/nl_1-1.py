import sys

line_number = 1

if len(sys.argv) == 2:
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                print(f"{line_number}\t{line}", end="")
                line_number += 1
    except:
        print("Please provide valid path to text files")

elif len(sys.argv) > 2:
    try:
        for i in range(1, len(sys.argv)):
            with open(sys.argv[i], "r") as file:
                print(f"Lines from {sys.argv[i]}")
                for line in file:
                    print(f"{line_number}\t{line}", end="")
                    line_number += 1
                print("\n")
    except:
        print("Please provide valid path to correct text files")

else:
    for line in sys.stdin:
        print(f"{line_number}\t{line}", end="")
        line_number += 1
