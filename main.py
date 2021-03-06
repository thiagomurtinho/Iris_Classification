import os
import numpy as np
import pandas as pd

from consolemenu import Screen

from app.utils.data_imports import *
from app.utils.mathPlots import *
from app.utils.mathLib import *

def action_minimum_squares(X, Y):
    np.set_printoptions(precision=2)
    res = minimum_squares(X, Y)


    print("\n")
    print('Dado, Y= mX + c')
    print('\nY= {:0.2f}X + ({:0.2f}): '.format(res["m"],res["c"]) )
    print('m: {:0.2f} kg'.format(res["m"]))
    print('c: {:0.2f}'.format(res["c"]))
    
    print('\nreta:\n{} '.format(res["reta"].values))

    print('\nmedia_X: \n{}'.format(res["media_X"]))
    print('\nmedia_Y: \n{}'.format(res["media_Y"]))
    print('\nerro_x: \n{}'.format(res["erro_x"].values))
    print('\nerro_y: \n{}'.format(res["erro_y"].values))
    print('\nsoma_erro_xy: \n{}'.format(res["soma_erro_xy"]))
    print('\nerro_x_quadratico: \n{}'.format(res["erro_x_quadratico"].values))
    print('\nsoma_erro_x_quadratico: \n{}'.format(res["soma_erro_x_quadratico"]))
    print("\n")

def action_plu(A):
    res = plu(A)
    print("\nResultado P:")
    print(res["P"])
    print("\nResultado L:")
    print(res["L"])
    print("\nResultado U:")
    print(res["U"])

def action_pvd(A):
    res = pvd(A)
    print("\nResultado U:")
    print(res["U"])
    print("\nResultado s:")
    print(res["s"])
    print("\nResultado V:")
    print(res["V"])
    
def action_plot(X, Y):
    linear_values = minimum_squares(X, Y)
    plot(X, Y, 
    ajust = True, 
    line = linear_values["reta"], 
    line_label='Ajuste linear', 
    line_color='red')

    Screen().input('Press [Enter] to continue')

def app():
  np.set_printoptions(precision=2)


  #get path from SO
  project_path = os.path.dirname(os.path.realpath(__file__))

  # # Import data from pandas
  data = pd.read_csv(project_path+'\\app\\data\\dados_07.csv')

  print("\n\n--------- Algelin II - UFRJ --------- ")
  print("------- Trabalho de analise de Iris -------- ")

  Screen().input('\n\nPress [Enter] to continue')

  print('\nQuestão 01:')
  print('- Método dos mínimos quadrados, Coeficiesntes. 01:')

  print('--- Iris-setosa: ---')
  print('--- Dados de Sepal')
  action_minimum_squares(
    extraction_colunms_value(data, 'Iris-setosa', 'SepalLengthCm'), 
    extraction_colunms_value(data, 'Iris-setosa', 'SepalWidthCm'))

  Screen().input('\n\nPress [Enter] to plot example Sepal')

  action_plot(
    extraction_colunms_value(data, 'Iris-setosa', 'SepalLengthCm'), 
    extraction_colunms_value(data, 'Iris-setosa', 'SepalWidthCm'))

  print('\n--- Dados de Petal')
  action_minimum_squares(
    extraction_colunms_value(data, 'Iris-setosa', 'PetalLengthCm'), 
    extraction_colunms_value(data, 'Iris-setosa', 'PetalWidthCm'))
  print('\n')


  print('--- Iris-versicolor: ---')
  print('--- Dados de Sepal')
  action_minimum_squares(
    extraction_colunms_value(data, 'Iris-versicolor', 'SepalLengthCm'), 
    extraction_colunms_value(data, 'Iris-versicolor', 'SepalWidthCm'))

  Screen().input('\n\nPress [Enter] to plot example Petal')

  action_plot(
    extraction_colunms_value(data, 'Iris-versicolor', 'PetalLengthCm'), 
    extraction_colunms_value(data, 'Iris-versicolor', 'PetalWidthCm'))
  print('\n--- Dados de Petal')
  action_minimum_squares(
    extraction_colunms_value(data, 'Iris-versicolor', 'PetalLengthCm'), 
    extraction_colunms_value(data, 'Iris-versicolor', 'PetalWidthCm'))
  print('\n')


  print('--- Iris-virginica: ---')
  print('--- Dados de Sepal')
  action_minimum_squares(
    extraction_colunms_value(data, 'Iris-virginica', 'SepalLengthCm'), 
    extraction_colunms_value(data, 'Iris-versicolor', 'SepalWidthCm'))
  
  Screen().input('\n\nPress [Enter] to plot example Sepal')

  action_plot(
    extraction_colunms_value(data, 'Iris-virginica', 'SepalLengthCm'), 
    extraction_colunms_value(data, 'Iris-versicolor', 'SepalWidthCm'))
  print('\n--- Dados de Petal')
  action_minimum_squares(
    extraction_colunms_value(data, 'Iris-virginica', 'PetalLengthCm'), 
    extraction_colunms_value(data, 'Iris-versicolor', 'PetalWidthCm'))
  print('\n')

  print('\n--- Implementação de PLU ---')
  print('--- Iris-setosa ---\n')
  action_plu(constructor_matrix([
    extraction_colunms_value(data, 'Iris-setosa', 'SepalLengthCm'),
    extraction_colunms_value(data, 'Iris-setosa', 'SepalWidthCm'),
    extraction_colunms_value(data, 'Iris-setosa', 'PetalLengthCm'),
    extraction_colunms_value(data, 'Iris-setosa', 'PetalWidthCm')
  ]))
  print('\n')
  Screen().input('\n\nPress [Enter] to continue')

  print('--- Iris-versicolor ---\n')
  action_plu(constructor_matrix([
    extraction_colunms_value(data, 'Iris-versicolor', 'SepalLengthCm'),
    extraction_colunms_value(data, 'Iris-versicolor', 'SepalWidthCm'),
    extraction_colunms_value(data, 'Iris-versicolor', 'PetalLengthCm'),
    extraction_colunms_value(data, 'Iris-versicolor', 'PetalWidthCm')
  ]))
  print('\n')
  Screen().input('\n\nPress [Enter] to continue')

  print('--- Iris-virginica ---\n')
  action_plu(constructor_matrix([
    extraction_colunms_value(data, 'Iris-virginica', 'SepalLengthCm'),
    extraction_colunms_value(data, 'Iris-virginica', 'SepalWidthCm'),
    extraction_colunms_value(data, 'Iris-virginica', 'PetalLengthCm'),
    extraction_colunms_value(data, 'Iris-virginica', 'PetalWidthCm')
  ]))
  print('\n')
  Screen().input('\n\nPress [Enter] to continue')

#bksub

#q02 decespec

#q03
  print('\n- Decomposição em valores singulares (SVD) ')
  print('--- Iris-setosa ---\n')
  action_pvd(constructor_matrix([
    extraction_colunms_value(data, 'Iris-setosa', 'SepalLengthCm'),
    extraction_colunms_value(data, 'Iris-setosa', 'SepalWidthCm'),
    extraction_colunms_value(data, 'Iris-setosa', 'PetalLengthCm'),
    extraction_colunms_value(data, 'Iris-setosa', 'PetalWidthCm')
  ]))
  print('\n')
  Screen().input('\n\nPress [Enter] to continue')

  print('--- Iris-versicolor ---\n')
  action_pvd(constructor_matrix([
    extraction_colunms_value(data, 'Iris-versicolor', 'SepalLengthCm'),
    extraction_colunms_value(data, 'Iris-versicolor', 'SepalWidthCm'),
    extraction_colunms_value(data, 'Iris-versicolor', 'PetalLengthCm'),
    extraction_colunms_value(data, 'Iris-versicolor', 'PetalWidthCm')
  ]))
  print('\n')
  Screen().input('\n\nPress [Enter] to continue')

  print('--- Iris-virginica ---\n')
  action_pvd(constructor_matrix([
    extraction_colunms_value(data, 'Iris-virginica', 'SepalLengthCm'),
    extraction_colunms_value(data, 'Iris-virginica', 'SepalWidthCm'),
    extraction_colunms_value(data, 'Iris-virginica', 'PetalLengthCm'),
    extraction_colunms_value(data, 'Iris-virginica', 'PetalWidthCm')
  ]))
  print('\n')
  Screen().input('\n\nPress [Enter] to continue')

  return

if __name__ == '__main__':
  app()