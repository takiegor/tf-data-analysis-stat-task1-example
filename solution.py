import pandas as pd
import numpy as np


chat_id = 451121038 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = x/10
    a = np.add(a, np.random.exponential(1, x.shape[0]) - 39)
    return a.mean() 
