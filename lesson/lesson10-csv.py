import csv 

f = open("sample.csv", "r")

rd = csv.reader(f)

for row in rd:
    for col in row:
        print(col, end=",")
    print()

f.close()

# with open("sample.csv", "w") as f:
#     w = csv.writer(f)
#     w.writerow(["横浜", "みなとみらい"])
#     w.writerows([["中華街","中華マン"],["赤煉瓦倉庫","カフェ"]])
