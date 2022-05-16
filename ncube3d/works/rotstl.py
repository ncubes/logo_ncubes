'''
read ascii stl file parsing out the coordinates

rotation matrix to line up with 
R(nˆ, θ) =
| cosθ+n1n1(1-cosθ)     n1n2(1-cosθ)-n3sinθ     n1n3(1-cosθ)-n2sinθ|
|n2n1(1-cosθ)+n3sinθ     cosθ+n2n2(1-cosθ)      n2n3(1-cosθ)-n1sinθ|
|n3n1(1-cosθ)-n2sinθ    n3n2(1-cosθ)+n1sinθ      cosθ+n3n3(1-cosθ) |

=? for 4d?
|  cosθ+n1n1(1-cosθ)    n1n2(1-cosθ)-n3n4sinθ   n1n3(1-cosθ)-n2n4sinθ   n1n4(1-cosθ)-n2n3sinθ|
|n2n1(1-cosθ)+n3n4sinθ    cosθ+n2n2(1-cosθ)     n2n3(1-cosθ)-n1n4sinθ   n2n4(1-cosθ)-n1n3sinθ|
|n3n1(1-cosθ)-n2n4sinθ  n3n2(1-cosθ)+n1n4sinθ     cosθ+n3n3(1-cosθ)     n3n4(1-cosθ)+n1n2sinθ|
|n4n1(1-cosθ)-n2n3sinθ  n4n2(1-cosθ)+n1n3sinθ   n4n3(1-cosθ)+n1n2sinθ     cosθ+n4n4(1-cosθ)  |


Use the 3d rotation.
First 0,0,0 is the bottom of the z brick.
so, first scale per the length of the basis vector.
Secondly, rotate based on the angle between the z unit vector and the basis vector in question.
I order to do this, the normal must be computed so that the formula above can be used.
Once the normal is computer, it provides n0, n1, and n2.  Then the angle must be
computed with trigonomentry based on the triange formed by the origin and the end of the basis
vector.  This would be easy to compute, all four quadrants should be considered.
Which way does the normal point?  Some kind of right hand rule is required to get it right.
However, if consistant method is used, does it matter right or left hand rule?

All the angles will be less than or 180 degrees, or it is a bad projection.
can the cross product be used?  Perhaps!

It is after all a subset of the Clifford Algebra that would be apprpriate.

cross prdouct produces vector perpendicular to both vectors a  and b.
a x b = bz-cy,cx-az,ay-bx in cartesian coordinates
||a x b|| = ||a|| ||b|| |sinθ|
So using this we can caclulate the normal vector as well as the sin.
We will always have a to be the vector 0,0,1.
The up vector is 'a'.  Thus, the cross product for it is zero and it will not be used
in the construction. 'b' is the basis vector.


So n and theta will be calculated from the basis vector.
The calculation will be repeated for all the basis vectors.

Alternative:  make logo simply output the normal vecotor and theta!  This will reduce the amount
of data transfered between these modules.


 But no, because the basis vectors must be added to the start point in order to "draw" the figure.
 In fact, the start point must be output as well as the basis vectors.

 Inputs: the basis vectors, the start point, the z stl file, the line list
 for no pen-lift.  Given all that, this module will crank out the model.

'''





stl_file = open ('model.stl','r')
out_file = open ('rotmodel.stl','w')
Lines = stl_file.readlines()
n = 0
z = []
for x in Lines:
    line_str = ''
    y = x.split(" ")
    for p in y:
        if p != '':
            try:
                z.append(float(p))
                n += 1
                if n == 3:
                    n=0
                    line_str += ("{:e}".format(z[0]))+' '+("{:e}".format(z[1]))+' '+("{:e}".format(z[2]))+' '+'\n'
                    z=[]
            except ValueError:
                line_str += p
                if (p == 'facet') or (p=='outer') or (p=='solid') or (p=='endsolid'):
                    line_str += ' '
        else:
             line_str += ' '
    out_file.write(line_str)
out_file.close()
stl_file.close()
