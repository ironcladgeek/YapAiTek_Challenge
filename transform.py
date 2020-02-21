import numpy as np
from sklearn.preprocessing import MinMaxScaler

class TargetTransform:
    def __init__(self, data, gamma=1e-3):
        self.data = self.__reshape2d(data)
        self.scaler = MinMaxScaler()
        self.scaler.fit(self.data)
        self.gamma = gamma

    def __reshape2d(self, arr):
        arr = np.asarray(arr)
        if arr.ndim == 1:
            arr = arr.reshape(-1, 1)
        return arr

    def __reshape1d(self, arr):
        arr = np.asarray(arr)
        if arr.ndim == 2:
            arr = arr.reshape(-1)
        return arr


    def transform(self, arr):
        arr = self.__reshape2d(arr)
        arr = np.log(arr + self.gamma)
        return self.__reshape1d(self.scaler.transform(arr))

    def inverse(self, arr):
        arr = self.__reshape2d(arr)
        arr = self.scaler.inverse_transform(arr)
        arr = np.exp(arr)
        return self.__reshape1d(arr - self.gamma)
        
