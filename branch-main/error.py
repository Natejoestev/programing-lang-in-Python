

class ERROR:
    def __init__(self, type_, context, desc):
        self.type_ = type_
        self.context = context
        self.desc = desc
    
    def __repr__(self):
        return f"{self.type_}: {self.context}: {self.desc}"