def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if(len(a[0]) != len(b)):
        return -1
    else:
        result = []
        for i in range(len(a)):
            sum = 0
            for j in range(len(b)):
                sum += a[i][j] * b[j]
            result.append(sum)
    return result
