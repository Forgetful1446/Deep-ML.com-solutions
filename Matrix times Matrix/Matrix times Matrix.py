def matrixmul(a: list[list[int|float]], b: list[list[int|float]]) -> list[list[int|float]]:
    
    if len(a[0]) != len(b):
        return -1

    rows = len(a)
    cols = len(b[0])
    inner = len(b)

    c = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):

            s = 0

            for k in range(inner):
                s += a[row][k] * b[k][col]

            c[row][col] = s

    return c
