import math

class TrussData:
    def __init__(self, adLen, dcLen, bdLen, bdLbs):
        self.adLen = adLen
        self.dcLen = dcLen
        self.bdLen = bdLen
        self.bdLbs = bdLbs

    def WholeCalc(self):
        cyLbs = round(self.bdLbs * self.adLen / (self.dcLen + self.adLen))
        ayLbs = round(self.bdLbs - cyLbs)
        axLbs = 0

        aAng = math.atan(self.bdLen / self.adLen)
        cAng = math.atan(self.bdLen / self.dcLen)

        abLbs = round(ayLbs / math.sin(aAng) * -1)
        adLbs = round(abLbs * math.cos(aAng) * -1)

        bcLbs = round(cyLbs / math.sin(cAng) * -1)
        dcLbs = round(bcLbs * math.cos(cAng))

        aAng = round(aAng / math.pi * 180)
        cAng = round(cAng / math.pi * 180)

        bdLbs = self.bdLbs*-1

        print(cyLbs, ayLbs, axLbs, aAng, cAng, abLbs, adLbs, bcLbs, dcLbs, bdLbs)

