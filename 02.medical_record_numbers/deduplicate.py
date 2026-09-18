import secrets
arr = [] # empty array
nlines = 0
with open("mrn.txt", "r") as f:
    for line in f:
        nlines += 1
        # remove end of line (use \r\n in Windows)
        line = line.rstrip("\n")
        line = line.split(",") # this reads them as strings 
        line = [int(i) for i in line] # cast as int
        arr.append(set(line))
while True:
    condition = False
    for i, it in enumerate(arr[:-1]):
        for j, jt in enumerate(arr[i+1:], start=i+1):
            intersec = it &jt 
            if (len(intersec) > 0):
                new = it | jt
                del arr[j] # delete the largest first or j will change!
                del arr[i]
                arr.append(new)
                condition = True
                break
        if condition:
            break
    if not condition:
        break

print(f"Out of {nlines} lines, there are just {len(arr)} unique patients")
used_IDs = set()
with open("mrn_unique.txt", "w") as f:
    for x in arr:
        while True:
            ID = secrets.randbits(64)
            if ID not in used_IDs:
                used_IDs.add(ID)
                break
        f.write(f"{ID}," + ",".join(str(y) for y in x) + "\n")

    



