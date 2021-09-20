def adding_numbers(a,b):
    if not (isinstance(a,int) and isinstance(b,int)):
        return "You must input integer numbers"
    return a +b
print(adding_numbers(7,8))
print(adding_numbers('7',8))
print(adding_numbers(7,8.2))
