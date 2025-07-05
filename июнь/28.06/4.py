def safe_div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    

print(safe_div(10,2))
print(safe_div(10,0))