array = ["flight","flow","flash"]
small = min(array)
large = max(array)

for i,char in enumerate(small):
    if char != large[i]:
        print(small[:i])
        break