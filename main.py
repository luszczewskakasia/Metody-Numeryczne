import numpy as np
def cylinder_area(r:float,h:float):
    area = 2*np.pi*r*r + 2*np.pi*r*h
    if r > 0 and h > 0:
        return area
    else:
        return np.NaN
    
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    return None

def fib(n: int):
    list = np.array([1, 1])
    if n <= 0:
        return None
    
    if isinstance(n, int):
        if n == 1:
            return np.array([1])

        if n == 2:
            return np.array([1, 1])
        if n > 2:
            for x in range(2, n):
                list = np.append(list, [list[x - 1] + list[x - 2]])
            return np.reshape(list, (1, n))
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    return None

def matrix_calculations(a:float):
    M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    Mdet = np.linalg.det(M)
    if Mdet == 0:
        Minv = np.NaN 
    else:
        Minv = np.linalg.inv(M)
    Mt = np.transpose(M)

    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    return Minv, Mt, Mdet

def custom_matrix(m:int, n:int):
    if m <= 0 or n <= 0:
        return None

    if isinstance(m, int) and isinstance(n, int):
        zero_matrix = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                if i > j:
                    zero_matrix[i][j] = i 
                else:
                    zero_matrix[i][j] = j
        return zero_matrix
    else:
        return None
            

    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    return None