from Type_values import value as VALUE
from Type_values import null as NULL
from Type_values import int as INT
from Type_values import str as STR

class SYNTAX:
    line_starters = ["*","", "var"]
    keywords = ["*", ["=","+=","-=","|="], ("\"","\'"), "null"]
    types = [VALUE.VALUE, [NULL.NULL_vlu, [INT.INT_vlu, INT.FLOAT_vlu], STR.STR_vlu]]
    number = list("0123456789")

    def __init__(self):
        pass
