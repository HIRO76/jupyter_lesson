import sys
import csv

print(sys.argv)

# for i, arg in enumerate(sys.argv):
#     print(f"{i}: {arg}")
    

# print(f"total: {sum([int(a) for a in sys.argv[1:]])}")


with open(sys.argv[1], "r")as f:
    data = csv.reader(f)
    res = [i for j in data for i in j]
    print(res)