from ssl import OP_NO_RENEGOTIATION
from tracemalloc import start
from turtle import end_fill


class Rute():
    start       = []
    end         = []
    kmDisatnce  = int
    timeAprox   = int
    payAprox    = float
    
    def __init__(self, start, end, kmDistance, timeAprox, payAprox):
        self.start          = start
        self.end            = end
        self.kmDisatnce     = kmDistance
        self.timeAprox      = timeAprox
        self.payAprox       = payAprox