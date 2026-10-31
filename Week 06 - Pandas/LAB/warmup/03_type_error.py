# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})
# value is a list of strings, use astype to convert to a float
df["percent"] = (df["value"].astype(float) / df["limit"]) * 100
