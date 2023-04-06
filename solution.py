import pandas as pd
import numpy as np


chat_id = 451121038 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Рассчитать среднюю скорость
    v_avg = np.mean(x)

    # Рассчитайте начальную скорость, вычитая среднюю ошибку
    v_i = v_avg - np.exp(1) - (-39)

    # Рассчитать коэффициент ускорения
    а = (v_avg - v_i) / 10
    return x.mean() # Ваш ответ
