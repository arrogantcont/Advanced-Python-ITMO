import sys

total_lines, total_words, total_bytes = 0, 0, 0

for filename in sys.argv[1:]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        lines = data.count("\n")
        words = len(data.split())
        bytes_ = len(data.encode("utf-8"))
        total_lines += lines
        total_words += words
        total_bytes += bytes_
        print(
            f"in {filename}:\ntotal_lines: {total_lines} total_words: {total_words} total_bytes: {total_bytes} \n"
        )
    except Exception as e:
        print(f"Error reading {filename}: {e}", file=sys.stderr)

if len(sys.argv) > 2:
    print(
        f"total_lines: {total_lines} total_words: {total_words} total_bytes: {total_bytes} total"
    )
elif len(sys.argv) == 1:
    try:
        data = sys.stdin.read()
        lines = data.count("\n")
        words = len(data.split())
        bytes_ = len(data.encode("utf-8"))
        print(
            f"\ntotal_lines: {total_lines} total_words: {total_words} total_bytes: {total_bytes} total"
        )
    except EOFError:
        pass
