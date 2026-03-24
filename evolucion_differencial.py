import numpy as np
import sympy as sym
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

def pob_inicial(N = 30, d = 2,  LB = None, UB = None):

    """Genera una población inicial.

    Parameters
    ----------
    N : int
        Tamaño de la población
    d : int
        Dimensión del problema
    LB : float, vector de dimensión d
        Límite inferior de cada una de las variables del problema
    UB : float, vector de dimensión d
        Límite superior de cada una de las variables del problema

    Returns
    -------
    float
        Matriz de dimensión N (filas) por d (columnas)
    """
    if LB is None:
      LB = - np.ones(d)
    if UB is None:
      UB = np.ones(d)

    Pob_ini = np.random.rand(N, d)


    # Normalización
    Pob_ini = Pob_ini * (UB - LB)  + LB

    return Pob_ini


def mutacion(Pob, id_mutantes = None, F = 1, LB = None, UB = None):

  """Genera los individuos mutantes

  Parámetros
  ----------

  Pob: float, matriz
      Cada elemento de la matriz Pob es un individuo que mutará.
  id_mutantes: int, vector
      Índices de los individuos que mutarán. Su dimensión es el número de filas
      de Pob.

  """

  Pob = Pob.copy() # Para no afectar la matriz de entrada.

  (n_row, n_col) = Pob.shape

  if id_mutantes is None:
    id_mutantes = range(n_row)

  if LB is None:
    LB = Pob.min(0)

  if UB is None:
    UB = Pob.max(0)

  mutacion = []

  for i in id_mutantes:

    indices = list(range(n_row))
    indices.remove(i)
    a, b, c = np.random.choice(indices, size=3, replace=False)
    X_mutacion = Pob[a] + F*(Pob[b] - Pob[c])
    X_mutacion = np.clip(X_mutacion, LB, UB)
    mutacion.append(X_mutacion)


  return np.array(mutacion)

def cruzamente(Pob, mutacion, CR = 0.8):
    (n_row, n_col) = Pob.shape
    Pob = Pob.copy()

    j_rand = np.random.randint(0, n_col, size=n_row) #necesitamos una dimension que cambiar por individu

    for i in range(n_row):
      
      for j in range(n_col):

        s = np.random.rand()

        if s < CR or j == j_rand:
          Pob[i][j] = mutacion[i][j]
    
    return Pob
        
      
  