from __future__ import annotations

from abc import ABC

from keras.models import Sequential
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import tensorflow as tf
from typing import Union


class DigitClassificationInterface:
    """Base layer interface"""

    def train(self, x: Union[np.ndarray, tf.Tensor], y: np.ndarray) -> DigitClassificationInterface:
        """Training function.

        :param x: either a numpy array or tensor with columns as features and rows as sample points
        :param y: a numpy array, the size of y should be the same as the number of rows of x.
        :return: the instanced class itself for chaining, i.e "return self"
        """
        raise NotImplementedError

    def predict(self, x: Union[np.ndarray, tf.Tensor]) -> int:
        """Prediction function.

        :param x: either a numpy array or tensor with columns as features and rows as sample points
        :return: a predicted class number
        """
        raise NotImplementedError

    def name(self):
        """Print algorithm's name"""
        raise NotImplementedError


class ModelCNN(DigitClassificationInterface, ABC):
    def __init__(self):
        self.model: Sequential() = None

    def predict(self, x: tf.Tensor) -> int:
        assert tuple(x.shape) == (28, 28, 1), "Required input size: (28, 28, 1)"
        return np.argmax(self.model.predict(x=x), axis=1)[0]

    def name(self):
        print('Convolutional Neural Network')


class ModelRFC(DigitClassificationInterface, ABC):
    def __init__(self):
        self.model: RandomForestClassifier() = None

    def predict(self, x: np.ndarray) -> int:
        assert x.shape == (784,), "Required input size: (784,)"
        return int(self.model.predict(X=x)[0])

    def name(self):
        print('Random Forest Classifier')


class ModelRand(DigitClassificationInterface, ABC):
    def __init__(self):
        pass

    def predict(self, x: np.ndarray) -> int:
        assert x.shape == (10, 10), "Required input size: (10, 10)"
        return round(np.random.rand(1)[0]*9)

    def name(self):
        print('Random Classifier')


MODEL_CLASSES = {'cnn': ModelCNN, 'rf': ModelRFC, 'rand': ModelRand}
MODELS = {'cnn': Sequential(), 'rf': RandomForestClassifier(), 'rand': None}


class DigitClassifier(object):

    def __new__(cls, algorithm: str):
        """ Customize the instantiation process according to algorithm's name. """
        cls = MODEL_CLASSES[algorithm]
        cls.model = MODELS[algorithm]
        print(cls)
        return cls.__new__(cls, algorithm)
