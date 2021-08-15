
class INT_vlu:
    def __init__(self, value):
        self.value = int(value)
        
    def do(self, fnc, args):
        func = getattr(self, fnc)
        ret = func(*args)
        return ret

    def math(self, op, INT):
        if op == "+":
            self.value += INT.value
            return self.value
        elif op == "-":
            self.value -= INT.value
            return self.value
        elif op == "*":
            self.value *= INT.value
            return self.value
        elif op == "/":
            self.value /= INT.value
            return self.value
        else:
            return None

class FLOAT_vlu(INT_vlu):
    def __init__(self, value):
        self.value = float(value)
