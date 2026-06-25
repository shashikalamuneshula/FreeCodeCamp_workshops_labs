def number_pattern(n):
        if not isinstance(n,int):
            return 'Argument must be an integer value.'
        if n<1:
            return 'Argument must be an integer greater than 0.'
        result=[]
        for i in range(1,n+1):
            result.append(str(i))
        return " ".join(result)
print(number_pattern(4))
print(number_pattern(12))
print(number_pattern('str'))
print(number_pattern(0))

