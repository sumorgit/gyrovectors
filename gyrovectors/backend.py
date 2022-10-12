from abc import ABC, abstractmethod
from enum import Enum
from typing import Union

from gyrovectors import Array, NumpyArray, Scalar


class AbstractBack(ABC):
    @abstractmethod
    def dot(self, u: Array, v: Array) -> Scalar:
        raise NotImplementedError("dot method is not implemented")

    @abstractmethod
    def square(self, u: Array) -> Array:
        raise NotImplementedError("square method is not implemented")

    @abstractmethod
    def sqrt(self, u: Array) -> Array:
        raise NotImplementedError("sqrt method is not implemented")

    @abstractmethod
    def sum(self, u: Array) -> Union[Array, Scalar]:
        raise NotImplementedError("sum method is not implemented")

    @abstractmethod
    def to_numpy(self, u: Array) -> NumpyArray:
        raise NotImplementedError("to_numpy method is not implemented")


class JaxBack(AbstractBack):
    def __init__(self):
        import jax

        self.jnp = jax.numpy

    def dot(self, u: Array, v: Array) -> Scalar:
        return self.jnp.dot(u, v)

    def square(self, u: Array) -> Array:
        return self.jnp.square(u)

    def sqrt(self, u: Array) -> Array:
        return self.jnp.sqrt(u)

    def sum(self, u: Array, axis: int = -1) -> Union[Array, Scalar]:
        return self.jnp.sum(u, axis=axis)

    def to_numpy(self, u: Array) -> NumpyArray:
        return u


class NumpyBack(AbstractBack):
    def __init__(self):
        import numpy

        self.np = numpy

    def dot(self, u: Array, v: Array) -> Scalar:
        return self.np.dot(u, v)

    def square(self, u: Array) -> Array:
        return self.np.square(u)

    def sqrt(self, u: Array) -> Array:
        return self.np.sqrt(u)

    def sum(self, u: Array, axis: int = -1) -> Union[Array, Scalar]:
        return self.np.sum(u, axis=axis)

    def to_numpy(self, u: Array) -> NumpyArray:
        return u


class Backends(Enum):
    numpy = NumpyBack
    jax = JaxBack


def get_backend(name: str) -> AbstractBack:
    """Returns the backend corresponding to the given name"""
    for back in Backends:
        if name == back.name:
            return back.value()
    raise ValueError(name + " is not valid")
