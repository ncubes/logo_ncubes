/* 
draw continous solid from one vertex to the next by 
extruding a cube of side s oriented towards its target
*/

include <cube.scad>;
$fn =3;s =15;
function d(i,t) = v[i]*(t)+v[i+1]*(1-t);
function c(i) = 1+norm(v[i]-v[i+1])/s;
for (i = [0 : 1 : len(v)-2])
    for (t = [ 0 : 1/c(i) : 1 ])
        translate(d(i,t))
            if (norm(v[i]-v[i+1]) > 0) 
                rotate([0,acos(((v[i+1]-v[i])[2])/(norm(v[i]-v[i+1]))),
                          atan2(((v[i+1]-v[i])[1]),((v[i+1]-v[i])[0]))])
                    cube(s, center=true);