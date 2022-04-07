import numpy as np
from numpy.polynomial import polynomial as poly
from matplotlib import pyplot as plt

def get_lagrange_poly(point, zeros):
  temppoly = np.polynomial.polynomial.polyfromroots(zeros[:, 0])
  outpoly = temppoly * point[1] / poly.polyval(point[0], temppoly)
  return outpoly


def get_prettified_output(polynomial):
    prettified_output = ""
    for i in range(len(polynomial)):
        prettified_output+= '%s' % float('%.3g' % polynomial[i])+"x^"+str(i)+" + "
    return prettified_output[:-2]

def lagrange(points, x):
  polynomial = poly.polyzero
  polylist = np.zeros([len(points) + 1, len(points)])
  resultlist = np.zeros([len(points) + 1, len(x)])
  for i in range(len(points)):
    temp = get_lagrange_poly(points[i], points[~(np.arange(len(points)) == i)])
    if polynomial.any():
      polynomial += temp    
    else:
      polynomial = temp
    print('Polynomonial ' + str(i + 1) + ': ['+ get_prettified_output(temp) + ']')
    polylist[i] = temp
    resultlist[i] = poly.polyval(x, temp)
    #plt.plot(x, poly.polyval(x, temp), '--')
  polylist[-1] = np.sum(polylist, axis=0)
  resultlist[-1] = poly.polyval(x, polylist[-1])
  print('Final Polynomonial: ['+ get_prettified_output(polylist[-1]) + ']')
  #print(resultlist)
  return resultlist



def main():
  points = [[0, 0],
    [1, 1],
    [2, 2],
    [3,3],
    [4, 4]
    ]
  
  points = []
  '''n = 5
  points = np.zeros([n, 2])
  points[:, 0] = np.linspace(0, 5, num=n)
  points[:, 1] = np.exp(points[:, 0])'''
  

  def onclick(event):
    if event.button == 1:
      #global points
      points.append([event.xdata, event.ydata])
      pointsnew = np.append(points, [[event.xdata, event.ydata]], axis=0)

    pointsnew = np.unique(pointsnew, axis=0)
    
    max_x = max(max(pointsnew[:, 0]), 10)
    min_x = min(min(pointsnew[:, 0]), -10)
    dx = .01
    expand = 0
    if len(pointsnew) > 1:
      x = np.arange(min_x - expand, max_x + dx + expand, dx)
    else:
      x = np.arange(-5, 5, dx)
  
    resultlist = lagrange(pointsnew, x)

    plt.clf()
    for j in range(len(pointsnew)):
      plt.plot(x, resultlist[j], '--')

    plt.plot(x, resultlist[-1], 'k')
    #plt.plot(x, np.exp2(x))
    plt.plot(pointsnew[:, 0], pointsnew[:, 1], 'ko')
    if len(pointsnew) > 0:
      #plt.ylim([min(resultlist[-1]) - expand, max(resultlist[-1]) + expand])
      plt.grid()
      #clear frame
      plt.xlim([-10, 10]) #comment this out if want scaling limits
      plt.ylim([-10, 10])
      plt.draw() #redraw


  
  
  fig,ax=plt.subplots()
  fig.canvas.mpl_connect('button_press_event',onclick)

  '''
  x = np.arange(-10, 10, .01)

  resultlist = lagrange(np.array(points), x)

  plt.clf()
  for j in range(len(points)):
    plt.plot(x, resultlist[j])

  plt.plot(x, resultlist[-1], 'k')
  #plt.plot(x, np.exp2(x))
  plt.plot(np.array(points)[:, 0], np.array(points)[:, 1], 'ko')
  #plt.ylim([min(evaluated), max(evaluated)])
  plt.grid()
  #clear frame '''

  plt.xlim([-10, 10])
  plt.ylim([-10, 10])  
  plt.grid()
  plt.show()

  plt.draw()



main()