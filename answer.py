# import csv
# import sys

# if len(sys.argv) < 2:
#     print("csvファイルを指定してください")
#     sys.exit()
# try: 
#     with open(sys.argv[1], 'r')as f:
#         data = csv.reader(f)
#         answer = [i for j in data for i in j]        
# except FileNotFoundError as e:
#     print("ファイルが見つかりません")
#     print(e)
# else:
#      # 空の辞書を用意
#     results = { }

#     # 辞書resultsに地域と数格納する
#     for region in answer:
#         if region in results:
#             results[region] += 1
#         else:
#             results[region] = 1

#     # 結果をソートして表示する
#     for region in sorted(results.items(), key=lambda c:c[1], reverse=True):
#         print(region[0],":",region[1])

import csv 
import sys

if len(sys.argv) < 2:
    print("csvファイルを指定してください")
    sys.exit()
try: 
    with open(sys.argv[1], "r")as f:
        data = csv.reader(f)
        answer = [i for j in data for i in j]
except FileNotFoundError as e:
    print("ファイルが見つかりません")
    print(e)
else:
    results = {}
    for key in answer:
        if key not in results:
            results[key] = 1
        else:
            results[key] += 1
    for k,v in sorted(results.items(), key=lambda x:x[1], reverse=True):
        print(f"{k} : {v}")