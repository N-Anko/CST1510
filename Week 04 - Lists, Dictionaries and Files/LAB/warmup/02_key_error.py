# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}
try:
    print(record["status"]) # "status" is not a key in the dictionary record.
except KeyError:
    print("There exists no key with that name")
