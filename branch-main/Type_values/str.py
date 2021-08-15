
class STR_vlu:
    def __init__(self, value):
        self.value = value
        
    def do(self, fnc, args):
        func = getattr(self, fnc)
        ret = func(*args)
        return ret

    def concat(self, STR):
        return f"{self.value}{STR.value}"