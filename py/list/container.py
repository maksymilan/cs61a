s = [[1,1],[1,2],[3,3],[2,2]]
count = 0
for x,y in s:
    if x == y:
        count += 1
print(count)