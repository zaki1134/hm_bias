from scipy.special import erf
import numpy as np


def bellcurve(length: float, div: int, intensity: float) -> np.ndarray:
    if div < 1:
        print("div must be greater than 0")
        return np.array([])
    if intensity == 0.0:
        print("intensity must not be 0")
        return np.array([])

    s = np.arange(div + 1) / div  # [0, 1]
    sqrt_r = np.sqrt(np.abs(intensity))
    term1 = erf(0.5 * sqrt_r)
    term2 = erf(sqrt_r * (0.5 - s))
    x = (term1 - term2) / (2.0 * term1)
    if intensity > 0.0:
        coords = x * length
        res = np.diff(coords)
    else:
        coords = (1.0 - x) * length
        res = np.diff(coords)
        res = res + np.abs(res).max() + np.abs(res).min()

    return res


def exponential(length: float, div: int, intensity: float) -> np.ndarray:
    if div < 1:
        print("div must be greater than 0")
        return np.array([])
    if intensity == 0.0:
        print("intensity must not be 0")
        return np.array([])

    s = np.arange(div + 1) / div  # [0, 1]
    c = 1.0 + 0.1 * np.abs(intensity)
    x = (np.power(c, div * s) - 1.0) / (np.power(c, div) - 1.0)
    if intensity > 0.0:
        coords = x * length
    else:
        coords = x * length
        coords = 1.0 - coords[::-1]

    return np.diff(coords)


def linear(length: float, div: int, intensity: float) -> np.ndarray:
    if div < 1:
        print("div must be greater than 0")
        return np.array([])
    if intensity == 0.0:
        print("intensity must not be 0")
        return np.arange(div + 1) / div  # [0, 1]

    s = np.arange(div + 1) / div  # [0, 1]
    b = 1.5
    x = s * (np.abs(intensity) * s + 2.0 * b) / (np.abs(intensity) + 2.0 * b)
    if intensity > 0.0:
        coords = x * length
    else:
        coords = x * length
        coords = 1.0 - coords[::-1]

    return np.diff(coords)
