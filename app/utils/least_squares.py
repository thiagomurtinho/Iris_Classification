import numpy as np

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
