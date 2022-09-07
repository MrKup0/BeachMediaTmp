import statistics
import dataCollection from generic

def mean(data: DataCollection, val: str) -> float:
    tmpData: list = []
    n = data.getMax()

    for i in range(0, n, 1):
        tmpData.append(data.getSpecific(val, i))
        
    return statistics.mean(tmpData)
