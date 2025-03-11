import numpy as np
from typing import List, Union, Dict

rowElements = 3
columnElements = 3

def errorMsg(msg: str = "") -> None:
    print(f'[ERROR]: {msg}.')

def infoMsg(msg: str = "") -> None:
    print(f'[INFO]: {msg}.')

def isValidArray(array: np.ndarray) -> bool:
    """Checks if the array has the correct length and contains only valid numeric values."""
    arrayLen = rowElements * columnElements

    if len(array) != arrayLen:
        errorMsg(f'The array has invalid length {len(array)} instead of {arrayLen}')
        return False

    if not np.all(np.isfinite(array)):
        errorMsg('The array contains invalid values (NaN, None, or non-numeric types)')
        return False

    infoMsg('The array is valid.')
    return True

def createArray(rowCount: int, columnCount: int) -> List[int]:
    """ Creates a matrix of size rowCount x columnCount (from 0 to rowCount * columnCount - 1) """
    if rowCount * columnCount != rowCount * columnCount:
        errorMsg(f'Matrix size must be {rowCount}x{columnCount}')
        return []
    return list(range(rowCount * columnCount))

def calculate(lst: List[Union[int, float]]) -> Dict[str, List[Union[List[float], float]]]:
    """ Computes statistical metrics (mean, variance, standard deviation, min, max, sum) for the given list. """
    if len(lst) != rowElements * columnElements:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst).reshape(rowElements, columnElements)

    result = {
        'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().tolist()],
        'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().tolist()],
        'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().tolist()],
        'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().tolist()],
        'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().tolist()],
        'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().tolist()]
    }

    return result

if __name__ == "__main__":
    ls = createArray(rowElements, columnElements)
    print(f'The array looks like: {ls}')
    
    if isValidArray(np.array(ls)):
        result = calculate(ls)
        print("Calculation results:", result)
