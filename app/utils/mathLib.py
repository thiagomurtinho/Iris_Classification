import numpy as np
import scipy.linalg as la

def constructor_matrix(M):
  return np.matrix(M).transpose()

def least_squares(X, Y, plot=None):
  media_X = np.mean(X)
  media_Y = np.mean(Y)
  erro_x = X-media_X
  erro_y = Y-media_Y
  soma_erro_xy = np.sum(erro_x*erro_y)
  erro_x_quadratico = (X-media_X)**2.0
  soma_erro_x_quadratico = np.sum(erro_x_quadratico)
  m = soma_erro_xy / soma_erro_x_quadratico
  c = media_Y - m*media_X
  reta = m*X+c

  return {
    'media_X': media_X,
    'media_Y': media_Y,
    'erro_x': erro_x,
    'erro_y': erro_y,
    'soma_erro_xy': soma_erro_xy,
    'erro_x_quadratico': erro_x_quadratico,
    'soma_erro_x_quadratico': soma_erro_x_quadratico,
    'm': m,
    'c': c,
    'reta': reta
  }

def plu(A):
  (P, L, U) = la.lu(A)
  return {
    'P': P,
    'L': L,
    'U': U
  }

def autovalores_autovetores(A):
  autovalores, autovetores = np.linalg.eig(A)
  return {
    'autovalores': autovalores, 
    'autovetores': autovetores
  }

def espectral(autovetores, matrizDiagonal):
  return np.matmul(np.matmul(autovetores,matrizDiagonal),np.linalg.inv(autovetores))

def pvd(A):
  (U,s,V) = np.linalg.svd(A)
  return {
    'U': U,
    's': s,
    'V': V
  }

def back_substitution(A, x, n):
  b = np.dot(A, x)
  xcomp = np.zeros(n)

  for i in range(n-1, -1, -1):
      tmp = b[i]
      for j in range(n-1, i, -1):
          tmp -= xcomp[j]*A[i,j]
          
      xcomp[i] = tmp/A[i,i]
  
  return xcomp