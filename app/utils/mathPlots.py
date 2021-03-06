import matplotlib.pyplot as plt

def plot(X, Y, ajust=False, line=None, line_label=None, line_color=None ):
  """
  type= dot/linear
  """

  plt.scatter(X,Y,label='Y(X)')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.legend()

  if ajust:
    plt.plot(X,line,label=line_label,color=line_color)

  plt.show(block=True)

  return