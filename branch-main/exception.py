

class EXEPTION_MGER:
    def __init__(self, shellQuiter):
        self.shellQuiter = shellQuiter
        
        self.expts = []
    
    def register(self, expt):
        self.expts.append(expt)
    
    def load_expts(self):
        for expt in self.expts:
            print(f"EXEPTION: {expt.type_}: {expt.desc}")
            self.exeption(expt)
        self.expts = []
    
    def exeption(self, expt):
        if expt.type_ == "exit":
            if input("exit? ") == "1":
                self.shellQuiter()

class EXEPTION:
    def __init__(self, type_, desc, mger):
        self.type_ = type_
        self.desc  = desc
        self.mger  = mger
    
    def Raise(self):
        self.mger.register(self)
