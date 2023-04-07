import pandas as pd
import numpy as np


chat_id = 451121038 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:

    return np.add(x/10, np.random.exponential(1, x.shape[0]) - 39)
