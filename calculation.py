import math

class TrussData:
    def __init__(self, adLen, dcLen, bdLen, bdLbs):
        self.adLen = adLen
        self.dcLen = dcLen
        self.bdLen = bdLen
        self.bdLbs = bdLbs

    def WholeCalc(self):
        cyLbs = self.bdLbs * self.adLen / (self.dcLen + self.adLen)
        ayLbs = self.bdLbs - cyLbs
        axLbs = 0

        aAng = math.atan(self.bdLen / self.adLen)
        cAng = math.atan(self.bdLen / self.dcLen)

        
        
