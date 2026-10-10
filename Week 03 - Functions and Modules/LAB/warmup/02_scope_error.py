# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status # status was not being returned

status = check(87, 100)

print(status) # status is not defined globally only locally
