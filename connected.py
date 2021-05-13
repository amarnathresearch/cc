
def connected(i, j, w, h, a):
    if j >= w or j < 0 or i < 0 or i >= h:
        return
    if a[i][j] != 1:
        return
    if a[i][j] == 1:
        a[i][j] = 2
    connected(i, j-1, w, h, a)
    connected(i, j+1, w, h, a)
    connected(i-1, j, w, h, a)
    connected(i+1, j, w, h, a)

    # Traversing toward diagonals
    # connected(i-1, j-1, w, h, a)
    # connected(i+1, j+1, w, h, a)
    # connected(i-1, j+1, w, h, a)
    # connected(i+1, j-1, w, h, a)

a = [[0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,0],[0,1,1,0,0,0,1,0],[0,1,1,0,0,0,1,0],[0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0],[0,1,0,1,1,0,0,0],[0,1,0,0,1,1,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,1,0,1,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,1,1,0]]

a = [[1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,1], [1,0,1,1,1,1,1,0,1], [1,0,1,0,0,0,1,0,1], [1,0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0,1], [1,0,1,0,0,0,1,0,1], [1,0,1,0,0,0,1,0,1], [1,0,1,1,1,1,1,0,1], [1,0,0,0,0,0,0,0,1], [1,1,1,1,1,1,1,1,1]]
h = len(a)
w = len(a[0])

# flag = 0
count = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == 1:
            connected(i, j, w, h, a)
            count += 1

print(a)
print(count)