import math
import subprocess
PixelsPerInch =100
Width= PixelsPerInch * 35.5 
marginPixels= .25 * PixelsPerInch
n_min= 4
n_max= 6
squish =math.pi
stroke= '00ff00'
stroke_width= 0
style= 'fill-rule:evenodd;fill:#ff0000;fill-opacity:1'
grow0 = 1
grow1 = 1
def design (n, s):
  global theta
  global CanvasPixels
  global user_center
  theta =squish/(n - odd)
  genbasis (n, s)
  CanvasPixels =Width + (2 * marginPixels)
  user_center =CanvasPixels  / 2.0
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
  llist = [1,2,-1,-2]   
  p = 2                   
  while k >= 2:
    hc = len(llist) 
    p += 2;k -= 2;
    llist.append(p-1)  ;  [llist.append(llist[i]) for i in range (hc)]
    llist.append(p  )  ;  [llist.append(llist[i]) for i in range (hc)]
    llist.append(1-p)  ;                                              
    for l in range (hc-1):                    
      x = (llist[l])                                              
      llist.append(x)
      if (abs(x) == abs(p-2)) or (abs(x) == abs(p-3)) :                                            
        llist.append(-p);llist.append(p-1);llist.append(p);llist.append(1-p)
    llist.append(llist[hc-1])
    llist.append(-p)
    print(llist)
def draw():
  global basis
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
  for k in range (len(llist)):
   basis[0][0] = basis[0][0] * grow0
   basis[0][1] = basis[0][1] * grow1
   dimension = llist[k]
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
  fname.write('"\nstroke="#' + str(stroke) + '" fill="none" stroke-width="' + str(stroke_width) + '" style="' + style+'"/>\n')
  fname.write ('</svg>\n')
  fname.close()
  subprocess.run(r"C:\Program Files\Inkscape\bin\inkscape.exe"+' --export-type="png" ' +str(n-odd)+"cube.svg")
  subprocess.run("mspaint "+str(n-odd)+"cube.png")
for n in range (n_min, (n_max + 1), 1):
    odd  = n % 2
    s = (Width * math.pi) / (2 * n)
    stroke_width = odd
    n= n + odd
    ncube(n)
    design (n, s)
    draw()
    
