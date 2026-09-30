"""
RECORD CHECK  -  my version
===========================

Name  : Neel Umesh Ankolekar
Lane  :  AI 
Date  : 23/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

dataset_name = input("Enter the dataset name: ")     
rows_loaded = float(input("Enter the rows loaded: "))     
rows_expected = float(input("Enter the rows expected: "))    


difference = rows_loaded - rows_expected  
percent = (rows_loaded / rows_expected) * 100  


print()
print("=" * 34)
print(f"  Dataset Name : {dataset_name:>10}")
print("=" * 34)
print(f"  Rows Loaded  : {rows_loaded:>10.2f}")
print(f"  Rows Expected: {rows_expected:>10.2f}")
print(f"  Difference   : {difference:>+10.2f}")
print(f"  Percent      : {percent:>10.2f}%")
print("=" * 34)



