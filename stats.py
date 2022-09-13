import numpy as np
from collections import DataCollection
from collections import ArticleCollection
from collections import TweetCollection


def varMean(data: DataCollection, var: str):
    if not isinstance(data.getSpecific(var, 0), float):
        return None


    for i in range(0, data.getMax(), 1):
