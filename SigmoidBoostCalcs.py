# Fetches User Parameters
# ---------------------------------------
from SigmoidBoostUserParameters import *

# Main Function
# ---------------------------------------
def userBoost(Days: float):
    if Days >= MxD:
        return B
    elif Days > (MxD - FL):
        return lastSigmoidBoost + (lastLinearSlope * (Days - (MxD - FL)))
    elif Days > IL:
        return calcSigmoidBoost(Days)
    elif Days > 0:
        return firstLinearSlope * Days
    else:
        return 0

# Helper Functions
# ---------------------------------------

def stdAlgebraSigmoid(X: float):
    return 1 + (X / (((X ** 2) + 1) ** 0.5))

def adjDaysToSigmoidX(Days: float):
    return ((Days * SigmoidSliceRange) / NonLinearRange) - SigmoidSliceRange / 2

def calcSigmoidBoost(Days: float):
    return stdAlgebraSigmoid(adjDaysToSigmoidX(Days)) * (B / 2)

# Calculated parameters used elsewhere
# ---------------------------------------
SigmoidSliceRange = US - LS # Range of the Sigmoid Slice We're Taking
NonLinearRange = (MxD - FL) - (IL - MnD) # Range of the days we want to be non-linear(IE in our Sigmoid)
firstSigmoidBoost = calcSigmoidBoost(IL) # Sigmoid Boost @ IL
firstLinearSlope = firstSigmoidBoost / IL # Linear slope from 0 -> IL
lastSigmoidBoost = calcSigmoidBoost(MxD - FL) # Sigmoid Boost @ MxD - FL
lastLinearSlope = (B - lastSigmoidBoost) / FL # Linear slope from (MxD - FL) -> MxD
