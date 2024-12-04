array = [0, 2,3, 4, 5, 7,8]
start = array[0]
n = array[0]
ranges = []

for i in range(1,len(array)):
    if array[i] == n+1:
        n = array[i]
    else:
        if start==n:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{n}")
        start = array[i]
        n = array[i]
if start==n:
        ranges.append(str(start))
else:
        ranges.append(f"{start}->{n}")
print(ranges)