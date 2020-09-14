def matrixArray(rowa, rowb, rowc):

    det = rowa[0] *((rowb[1]* rowc[2]) -(rowb[2]*rowc[1])) -rowa[1]*((rowb[0]* rowc[2]) - (rowb[2]*rowc[0]))+ rowa[2]*((rowb[0]* rowc[1]) - (rowb[1]*rowc[0]))

    print('Your determinant:' , rowa, ',', rowb, 'and' , rowc, '===',det)

matrixArray(
    [1,2,3],
    [4,5,6],
    [7,8,9]
    )
