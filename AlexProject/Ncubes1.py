import math
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
  n_min= 10
  n_max= 10
  squish =180
  stroke= '90ee90'
  stroke_width= 1.5


def design (n, s):
  global theta
  global squish
  global CanvasPixels
  global Width
  global user_center
  global odd
  theta =squish/(n - odd)
  genbasis (n, s)
  CanvasPixels =Width + (2 * marginPixels)
  user_center =CanvasPixels  / 2.0
  print ("paper square side size inches including bleed (margin):", CanvasPixels / PixelsPerInch)
  draw()


def genbasis (n, s):
  global basis
  global theta
  global CanvasPixels
  basis = [[s * math.cos (i * theta), s * math.sin (i * theta)] for i in range(n)]
  if odd == 1:
    basis[-1][0] = 0
    basis[-1][1] = 0



def draw():
  global n
  global CanvasPixels
  global CurrentPosition
  global basis
  global ll
  global llist
  fname= open("Alex3.svg", w)
  fname.write ('<?xml version="1.0" standalone="no"?>')
  fname.write ('<svg width="', CanvasPixels,'" height="', CanvasPixels,'" version="1.1" xmlns="http://www.w3.org/2000/svg">')
  CurrentPosition [0] = 0
  CurrentPosition [1] = 0
  for i in range (n):
    CurrentPosition[0] += basis[i][0]
    CurrentPosition[1] += basis[i][1]
  CurrentPosition[0] /= 2
  CurrentPosition[1] /= 2
  fname.write ('<polyline points="', (user_center + CurrentPosition[0]), (user_center + CurrentPosition[1]))

  ll = llist
  
  while ll:
   dimension dequeue "ll
   direction sign dimension
   dimension abs dimension
   itskip 1
   for [i 1 2 1] [~
    Current item i CurrentPosition
    index (list dimension i)
    delta mditem index basis
    if not equalp delta 0 [itskip 0]
    setitem  i CurrentPosition (Current + (direction * delta)) ]
   if itskip = 0 [~
     (print(user_center + item 1 CurrentPosition)(user_center + item 2 CurrentPosition))]
  ]
  
  print ["]
  type [    stroke="#]
  type stroke 
  type  [" fill="none" stroke-width="]
  type stoke_width
  type ["/>]
  print [</svg>]
  
  setwrite []
  show fname
  show "done
  close fname
 


def ncube (k):
  global llist
  k = k-2             
  llist = [2, 1, -2, -1]   
  d = 2              
  while k >= 2: 
    d = d+2 
    k k-2 
    cube (llist d) 

def cube(l, p):
  global llist
  global ll
  l1 = l
  llist = []
  llist.push(p)
  while ll:
    llist.push(l1.pop(0))
  l1 = l
  llist.push(p-1)
  while ll:
    llist.push(l1.pop(0))
  l1 =l
  llist.push(-p)
  while ll:
    llist.push(l1.pop(0))
  l1 =l
  llist.push(1-p)
  llist.push(l1.pop(0))
  llist.push(p)
  llist.push(p-1)
  llist.push(-p)
  llist.push(1-p)
  while ll:
   x = l1.pop(0) 
   if (abs x) = (abs p-2):                                            
     llist.push(p) 
     llist.push(p-1)
     llist.push(-p)
     llist.push(1-p)
     llist.push(x)
     llist.push(p)
     llist.push(p-1)
     llist.push(-p)
     llist.push(1-p)
   if (abs x) != (abs p-2): 
     llist.push(x)
  

specify()
for n in range (n_min, (n_max + 1), 1): #main loop
    odd  = n % 2
    s = (Width * math.pi) / (2 * n)
    n= n + odd
    p= n
    ncube(n)
    design (n, p, s)
