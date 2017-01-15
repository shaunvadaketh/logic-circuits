class AND(object):
    
    def __init__(self, pinA, pinB):
        
        self.pinA = pinA
        self.pinB = pinB
        
    def gateFunction(self):
        #import pdb; pdb.set_trace()
        if self.pinA == self.pinB == "1":
            return 1
        else:
            return 0
            
    def output(self):
         
        self.output = self.gateFunction()
        return self.output

class OR(object):
    
    def __init__(self, pinA, pinB):
        
        self.pinA = pinA
        self.pinB = pinB
    
    def gateFunction(self):
        
        if self.pinA == "1":
            return 1
        elif self.pinB == "1":
            return 1
        else:
            return 0
    
    def output(self):
         
        self.output = self.gateFunction()
        return self.output

class NOT(object):
    
    def __init__(self, pinA):
        
        self.pinA = pinA
    
    def gateFunction(self):
        
        if self.pinA == "1":
            return 0
        else:
            return 1
    
    def output(self):
         
        self.output = self.gateFunction()
        return self.output
        