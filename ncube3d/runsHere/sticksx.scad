// will draw continous solid from one vertex to the next
include <cube.scad>;
$fn =3;r =15;
function d(i,t) = v[i]*(t)+v[i+1]*(1-t);
function c(i) = 2+2*norm(v[i]-v[i+1])/r;
for (i = [0 : 1 : len(v)-2])
    for (t = [ 0 : 1/c(i) : 1 ])
        translate(d(i,t)) sphere(r);