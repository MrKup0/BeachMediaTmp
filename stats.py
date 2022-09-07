import statistics
import dataCollection from generic

def mean(data: dataCollection, val: str) -> float:
    if data.getType() is None:
        return 0

    tmp: float = 0

    for i in range(0, data.getMax(), 1):
        tmp = tmp + data.getSpecific(val, i)

    return tmp / data.getMax()

def stDev(data: dataCollection, val: str) -> float:
    m = mean(data, val)
    n = data.getMax()
    tmp = 0
    if m == 0:
        return 0
    for i in range(0, n, 1):
        tmp = tmp + ((data.getSpecific(val, i) - m)^^2/n)

    return tmp ^^ (1/2)
