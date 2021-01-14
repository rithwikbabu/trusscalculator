class TrussData:
    def __init__(self, ad, dc, bd):
        self.ad = ad
        self.dc = dc 
        self.bd = bd

    def RFcalc(self):
        B = truss.bd * truss.ad / (truss.dc + truss.ad)
        A = truss.bd - B

        return A, B

truss = TrussData(8, 6, 450)
print(truss.RFcalc())