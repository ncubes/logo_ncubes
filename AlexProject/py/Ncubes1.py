import math
import copy
import collections

PixelsPerInch =350
Width= PixelsPerInch * 35.5 
marginPixels= .25 * PixelsPerInch
n_min= 2
n_max= 14
squish =math.pi
stroke= '90ee90'
stroke_width= 100

def design (n, s):
  global theta
  global CanvasPixels
  global user_center
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
  global llist
  k = k-2             
  llist = [2, 1, -2, -1]   
  p = 2              
  while k >= 2: 
    p += 2 
    k -= 2
    l = copy.copy(llist)
    l1=[]
    l1 =copy.copy (l)
    llist = []
    llist.append(p)
    while l1:
      llist.append(l1.pop(0))
    l1 = copy.copy(l)
    llist.append(p-1)
    while l1:
      llist.append(l1.pop(0))
    l1 = copy.copy(l)
    llist.append(-p)
    while l1:
      llist.append(l1.pop(0))
    l1 = copy.copy(l)
    llist.append(1-p)
    llist.append(l1.pop(0))
    llist.append(p)
    llist.append(p-1)
    llist.append(-p)
    llist.append(1-p)
    while l1:
     x = l1.pop(0) 
     if abs(x) == abs(p-2):                                            
       llist.append(p) 
       llist.append(p-1)
       llist.append(-p)
       llist.append(1-p)
       llist.append(x)
       llist.append(p)
       llist.append(p-1)
       llist.append(-p)
       llist.append(1-p)
     if abs(x) != abs(p-2): 
       llist.append(x)
  
def draw():
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
  l1 = copy.copy(llist)
  while l1:
   dimension = l1.pop(0)
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


for n in range (n_min, (n_max + 1), 1):
    odd  = n % 2
    s = (Width * math.pi) / (2 * n)
    n= n + odd
    p= n
    ncube(n)
    design (n, s)
    
