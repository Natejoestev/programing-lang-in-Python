
class Context:
    def __init__(self, parCTX):
        self.parCTX = parCTX

        self.values = {}
    
    def setValue(self, key,value):
        self.values[key] = value
        return value
    def setValueGlobaly(self, key,value):
        if self.parCTX != None:
            self.parCTX.setValueGlobaly(key, value)
        else:
            self.values[key] = value
    def getValue(self, key):
        value = None
        if key in self.values.keys():
            value = self.values[key]
        else:
            if self.parCTX != None:
                value = self.parCTX.getValue(key)
        return value
    def removeValue(self, key):
        del self.values[key]