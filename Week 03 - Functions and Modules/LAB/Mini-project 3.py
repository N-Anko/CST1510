"""
RECORD CHECK  -  my version
===========================

Name  : Neel Umesh Ankolekar
Lane  :  AI 
Date  : 7/10/2026

Run it:   python template.py

"""

def status_of(percent):
    """Returns a Status warning based of the percent given."""
    if percent>=100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
def check(value,limit):
    """Returns the difference and percent of the value and limit given."""
    difference = value-limit
    percentage = (value/limit) *100
    return difference,percentage
def print_report(label,value,limit,difference,percent,status):
    """Outputs the Record data."""
    print(f"Rows loaded   : {value:>10}")
    print(f"Rows expected : {limit:>10}")
    print(f"Rows missing  : {limit-value:>10}")
    print(f"Difference    : {difference:>10.2f}")
    print(f"Percent       : {percent:>10.2f} %")
    print(f"Status        : {status:>10}")
count = 0
while True:
    dataset_name = input("Enter the Dataset name: ")   
    if dataset_name == "quit": 
        break
    Rows_loaded = float(input("Enter the rows loaded: "))
    Rows_expected= float(input("Enter the rows expected: "))     

    difference,percent = check(Rows_loaded,Rows_expected)    
    status =  status_of(percent)        # replace with your code

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {dataset_name}")
    print("=" * 34)
    print_report(dataset_name, Rows_loaded,Rows_expected,difference,percent,status)
    print("=" * 34)
    count +=1
print(f"You have reached OVER LIMIT status {count} times.")
