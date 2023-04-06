import pandas as pd
import numpy as np


chat_id = 451121038 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Рассчитать среднюю скорость
    v_avg = np.mean(x)
    а = v_avg / 10
    return a.mean() # Ваш ответ
