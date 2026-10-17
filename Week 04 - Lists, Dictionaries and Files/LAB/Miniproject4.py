"""
RECORD CHECK  -  my version
===========================

Name  : Neel Ankolekar
Lane  :  AI 
Date  : 14/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.
def check_record(value,limit):
    """Returns the difference and percent of the value and limit given and the status."""
    difference = value-limit
    percentage = (value/limit) *100
    if percentage>=100:
        status ="OVER LIMIT"
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference,percentage,status
def print_report(label,value,limit,difference,percent,status): 
    """Outputs the Record data."""
    print(f"Dataset Name  : {label:>10}")
    print(f"Rows loaded   : {value:>10}")
    print(f"Rows expected : {limit:>10}")
    print(f"Rows missing  : {limit-value:>10}")
    print(f"Difference    : {difference:>10.2f}")
    print(f"Percent       : {percent:>10.2f} %")
    print(f"Status        : {status:>10}")
    print()
def load_records(path,printOutput = True): 
    """Returns a list of dictionaries read from the file inputted."""
    try:
        list_of_dicts = []
        with open(path,"r") as f:
            for line in f:
                label,value,limit = line.strip().split(",")
                value,limit = float(value),float(limit)
                list_of_dicts.append({"label":label,"value":value,"limit":limit})
            for record in list_of_dicts:
                status = ""
                if record["value"] > record["limit"]:
                    status = "OVER LIMIT"
                else:
                    status = "OK"
                record["status"] = status
                if printOutput:
                    print(f"{record['label']}: {status}")
        return list_of_dicts
    except FileNotFoundError:
        print(f"{path} does not exist")
        return list_of_dicts
Records = load_records("LAB/records_sample.txt",False)
with open("results.txt","w") as f:
    for record in Records:
        label = record["label"]
        status = record["status"]
        f.write(f"{label},{status}\n")
with open("results.txt","r") as f:
    print(f.read())

OverLimitCount = 0
for record in Records:
    diff,per,stat = check_record(record["value"],record["limit"])
    print_report(record["label"],record["value"],record["limit"],diff,per,stat)
    if stat == "OVER LIMIT":
        OverLimitCount+=1
word = "are"
if OverLimitCount ==1:
    word = "is"
print(f"{OverLimitCount} {word} over the limit")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
