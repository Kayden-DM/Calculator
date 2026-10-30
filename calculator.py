import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def calculate():
    while True:
        expr = input("Enter calculation or 'quit': ").strip()
        if expr.lower() == "quit":
            break
        try:
            a, op, b = expr.split()
            result = ops[op](float(a), float(b))
            print(f"= {result}\n")
        except ZeroDivisionError:
            print("Error: can't divide by zero\n")
        except Exception:
            print("Error: use format 'number operator number'\n")

calculate()