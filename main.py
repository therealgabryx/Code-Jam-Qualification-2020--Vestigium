def getTrace(mat, size):
    trace = 0
    for i in range(size):
        for j in range(size):
            if (i == j):
                trace += mat[i][j]
    return trace

t = int(input()) #testcases

def getRows(mat, size):
    rep_rows = 0
    for i in range(size):
        row = {'def'}
        for j in range(size):
            if (mat[i][j] in row):
                rep_rows += 1
                break
            else:
                row.add(mat[i][j])
    return rep_rows

def getCols(mat, size):
    rep_cols = 0
    for i in range(size):
        col = {'def'}
        for j in range(size):
            if (mat[j][i] in col):
                rep_cols += 1
                break
            else:
                col.add(mat[j][i])
    return rep_cols

for i in range(t):
    size = int(input()) 
    # matrix creation v
    mat = []
    while not mat or len(mat) < len(mat[0]):
        mat.append(list(map(int, input().split())))
    # matrix created ^
    trace = getTrace(mat, size) # calc. mat trace
    rows = getRows(mat, size) 
    cols = getCols(mat, size) 
    print ("Case #" + (str) (i+1) + ": " + (str) (trace) + " " + (str) (rows) + " " + (str) (cols)) 

    