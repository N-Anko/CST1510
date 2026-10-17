# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

try:
    with open("records.txt") as f: # no file directory would exist normally with that name.
        print(f.read())
except FileNotFoundError:
    print("file not found")
