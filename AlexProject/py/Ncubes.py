import math
import copy
import collections
def specify():
  global PixelsPerInch
  global Width
  global marginPixels
  global n_min
  global n_max
  global squish
  global stroke
  global stroke_width
  PixelsPerInch =350
  Width= PixelsPerInch * 35.5 
  marginPixels= .25 * PixelsPerInch
  n_min= 2
  n_max= 4
  squish =math.pi
  stroke= '90ee90'
  stroke_width= 100

def design (n, s):
  global CanvasPixels
  global user_center
  global theta
  theta =squish/(n - odd)
  genbasis (n, s)
  CanvasPixels =Width + (2 * marginPixels)
  user_center =CanvasPixels  / 2.0
  draw()
  print (str(n-odd)+"cube paper square side size inches including bleed (margin):", CanvasPixels / PixelsPerInch)
  
def genbasis (n, s):
  global basis
  basis = [[s * math.cos (i * theta), s * math.sin (i * theta)] for i in range(n)]
  if odd == 1:
    basis[-1][0] = 0
    basis[-1][1] = 0

def ncube (k):
  global edge
  k = k-2             
  edge = [2, 1, -2, -1]   
  d = 2              
  while k >= 2: 
    d = d+2 
    k = k-2 
    l_prime=[]
    l_prime =copy.deepcopy (edge)
    edge = []
    edge.append(d)
    while l_prime:
      edge.append(l_prime.pop(0))
    l_prime = copy.deepcopy(edge)
    edge.append(d-1)
    while l_prime:
      edge.append(l_prime.pop(0))
    l_prime = copy.deepcopy(edge)
    edge.append(-d)
    while l_prime:
      edge.append(l_prime.pop(0))
    l_prime = copy.deepcopy(edge)
    edge.append(1-d)
    edge.append(l_prime.pop(0))
    edge.append(d)
    edge.append(d-1)
    edge.append(-d)
    edge.append(1-d)
    while l_prime:
     x = l_prime.pop(0) 
     if abs(x) == abs(d-2):                                            
       edge.append(d) 
       edge.append(d-1)
       edge.append(-d)
       edge.append(1-d)
       edge.append(x)
       edge.append(d)
       edge.append(d-1)
       edge.append(-d)
       edge.append(1-d)
     if abs(x) != abs(d-2): 
       edge.append(x)
  
def draw():
  global edge
  fname= open(str(n-odd)+"cube.svg", 'w')
  fname.write ('<?xml version="1.0" standalone="no"?>\n')
  fname.write ('<svg width="'+ str(CanvasPixels) + '" height="' + str(CanvasPixels) + '" version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
  CurrentPosition = [0,0]
  for i in range (n):
    CurrentPosition[0] += basis[i][0]
    CurrentPosition[1] += basis[i][1]
  CurrentPosition[0] /= -2
  CurrentPosition[1] /= -2
  fname.write ('<polyline points="\n' + str(user_center + CurrentPosition[0]) + ' ' + str(user_center + CurrentPosition[1])+ '\n' )
  l_p = copy.deepcopy(edge)
  while l_p:
   dimension = l_p.pop(0)
   direction = math.copysign(1,dimension)
   dimension = abs(dimension)
   itskip = 1
   for i in range(2):
    Current = CurrentPosition[i]
    delta = basis[dimension-1][i]
    if delta != 0:
     itskip = 0
    CurrentPosition[i]= (Current + (direction * delta)) 
   if itskip == 0:
     fname.write (str(user_center + CurrentPosition[0]) + ' ' + str( user_center + CurrentPosition[1]) + '\n')
  fname.write('"\nstroke="#' + str(stroke) + '" fill="none" stroke-width="' + str(stroke_width) + '"/>\n')
  fname.write ('</svg>\n')
  fname.close()
specify()
for n in range (n_min, (n_max + 1), 1):
    odd  = n % 2
    s = (Width * math.pi) / (2 * n)
    n= n + odd
    p= n
    ncube(n)
    design (n, s)
    
