"""
RECORD CHECK  -  my version
===========================

Name  :  Neel Ankolekar
Lane  :  AI 
Date  :  21/10/2026

Run it:   MiniProject5.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    over_limit_count = 0
    def __init__(self,label,value,limit):
        """Initializes attributes."""
        self.label = label
        self.value = value
        self.limit = limit
    def status(self):
        """Returns the status based of the value and limit."""
        p = (self.value/self.limit)*100 # p is percent
        if p >=100:
            return "OVER LIMIT"
        elif p >=90:
            return "WARNING"
        else:
            return "OK"
records = []  
def load_records(path):
    """Reads lines from a text file and converts them to records, which is then added to a list."""
    with open(path,"r") as f:
        for line in f:
            label,value,limit = line.strip("").split(",")
            value,limit = float(value),float(limit)
            records.append(Record(label,value,limit))
    return records
Records = load_records("LAB/records_test.txt")
OverLimitCounter = 0
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Rows loaded   : {record.value:>10.2f}")
    print(f"  Rows Expected : {record.limit:>10.2f}")
    print(f"  Difference    : {record.limit-record.value:>10.2f}")
    print(f"  Percent       : {record.value/record.limit *100:>10.2f}")
    stat = record.status()
    if stat == "OVER LIMIT":
        OverLimitCounter+=1
    print(f"  Status        : {stat:>10}")
    print("=" * 34)
print(f"{OverLimitCounter} of {len(Records)} were over limit")
