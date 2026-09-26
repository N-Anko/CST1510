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



dataset_name = input("Enter the dataset name: ")     # : replace with an input() call
rows_loaded = float(input("Enter the rows loaded: "))     # : replace with an input() call, converted
rows_expected = float(input("Enter the rows expected: "))    # : replace with an input() call, converted


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


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
