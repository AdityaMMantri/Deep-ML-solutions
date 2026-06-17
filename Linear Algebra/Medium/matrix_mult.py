def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

            rows_a=len(a)
            rows_b=len(b)
            col_a=len(a[0])
            col_b=len(b[0])

            if col_a!=rows_b:
                return -1
            result=[]

            for i in range(rows_a):
                new_row=[]
                for j in range(col_b):
                    total=0
                    for k in range(col_a):
                        total+=a[i][k]*b[k][j]
                    new_row.append(total)
                result.append(new_row)                    
            return result