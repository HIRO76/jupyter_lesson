# f = open("Sample.txt", "w")
# with open("Sample.txt", "w") as f:
f = open("Sample.txt", "r")

lines = f.readlines()

for line in lines:
    print(line, end="")

#     f.write("こんにちは\n")
#     f.write("さようなら\n")
#     f.write("追記\n")

    
    
f.close()