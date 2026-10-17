# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

labels = ["R-001", "R-002", "R-003"]
try:
    print(labels[3]) # index out of range error, index starts at 0 not 1.
except IndexError:
    print("Index is out of range")