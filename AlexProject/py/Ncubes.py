import math

#configure your design here prior to function definition
PixelsPerInch =350
Width =PixelsPerInch * 35.5 
marginPixels =.25 * PixelsPerInch
n_min= 9
n_max =10
squish= 180
stroke = '90ee90'
stoke_width = 1.5

def genbasis (n, s, theta, odd):
    basis = [[s * math.cos (i * theta), s * math.sin (i * theta)] for i in range(n)]
    if odd == 1:
        basis[-1][0] = 0
        basis[-1][1] = 0
        return basis

def design (n, p, s, odd):
    theta =squish/(n - odd)
    genbasis (n, s, theta, odd)
    CanvasPixels = Width + ( 2 * marginPixels )
    user_center = CanvasPixels  / 2.0
    print ('paper square side size inches including bleed (margin): ',CanvasPixels / PixelsPerInch )
    draw(CanvasPixels, n, basis)

for n in range (n_min, (n_max + 1), 1):
    odd  = n % 2
    s = (Width * math.pi) / (2 * n)
    #s= Width / math.sqrt(n)
    n += odd
    p = n
    #ncube (n)
    design (n,p,s,odd)



'''

to ncube :k
k :k-2             
if :k<0 [stop]             
llist [2 1 -2 -1]   
d 2              
while [ not :k<2] [ d :d+2 k :k-2 cube :llist :d ] 
end

to cube :l :p
l1 :l
llist []
queue "llist :p
while [not :l1=[]] [queue "llist dequeue "l1]
l1 :l
queue "llist :p-1
while [not :l1=[]] [queue "llist dequeue "l1]
l1 :l
queue "llist -:p
while [not :l1=[]] [queue "llist dequeue "l1]
l1 :l
queue "llist 1-:p
queue "llist dequeue "l1
queue "llist :p queue "llist :p-1 queue "llist -:p queue "llist 1-:p
while [ not :l1=[] ] [
 x dequeue "l1 
 if (abs :x) = (abs :p-2)  [                                          
   queue "llist :p queue "llist :p-1 queue "llist -:p queue "llist 1-:p
   queue "llist :x 
   queue "llist :p queue "llist :p-1 queue "llist -:p queue "llist 1-:p]
 if not  (abs :x) = (abs :p-2) [ queue "llist :x]]
end

startup [specify]
'''

