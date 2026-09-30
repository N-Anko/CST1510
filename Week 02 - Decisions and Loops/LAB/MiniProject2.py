"""
RECORD CHECK  -  my version
===========================

Name  : Neel Ankolekar
Lane  :  AI 
Date  : 30/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
Overlimit_count = 0
while True:
    dataset_name = input("Enter the dataset name: ")   
    if dataset_name == "quit":
        break
    rows_loaded = float(input("Enter the rows loaded: "))     
    rows_expected = float(input("Enter the rows expected: "))     

    difference = rows_loaded - rows_expected   
    percent = (difference / rows_expected * 100)       

    if percent >= 100:
        status = "OVER LIMIT"
        Overlimit_count +=1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {dataset_name}")
    print("=" * 34)
    print(f"  Rows loaded   : {rows_loaded:>10,.2f}")
    print(f"  Rows expected : {rows_expected:>10,.2f}")
    print(f"  Difference    : {difference:>10,.2f}")
    print(f"  Percent       : {percent:>10,.2f}%")
    print(f"  Status        : {status:>10}")
    print("=" * 34)
print(f"You have gone OVER LIMIT {Overlimit_count} times")


