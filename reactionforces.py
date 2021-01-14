class TrussData:
    def __init__(self, ab, bc, db):
        self.ab = ab
        self.bc = bc 
        self.db = db

truss = TrussData(8, 6, 450)

def RFcalc():
    B = truss.db * truss.ab / (truss.bc + truss.ab)
    A = truss.db - B

    return A, B
    