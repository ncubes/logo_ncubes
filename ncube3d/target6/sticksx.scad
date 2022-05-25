/* 
draw continous solid from one wertex to the next by 
extruding a cube of side s oriented towards its target
*/

include <cube.scad>;

$fn =3;s =100 ;f=s;r=.2;
CubePoints = [
  [  -.5 * s, -.5 * s, -.5 * s ],  //0
  [   .5 * s, -.5 * s, -.5 * s ],  //1
  [   .5 * s,  .5 * s, -.5 * s ],  //2
  [  -.5 * s,  .5 * s, -.5 * s ],  //3
  [  -.5 * s, -.5 * s,  .5 * s ],  //4
  [   .5 * s, -.5 * s,  .5 * s ],  //5
  [   .5 * s,  .5 * s,  .5 * s ],  //6
  [  -.5 * s,  .5 * s,  .5 * s ]]; //7
  
CubeFaces = [
  [0,1,2,3],  // bottom
  [4,5,1,0],  // front
  [7,6,5,4],  // top
  [5,6,2,1],  // right
  [6,7,3,2],  // back
  [7,4,0,3]]; // left

for (i = [0 : 1 : len(w)-2])
    scale(v = [r,r,r])
        if (norm(w[i]-w[i+1]) > 0) 
            translate((w[i]+w[i+1])/2)
                rotate([0,acos(((w[i+1]-w[i])[2])/(norm(w[i]-w[i+1]))),atan2(((w[i+1]-w[i])[1]),((w[i+1]-w[i])[0]))])
                    scale(v = [1,1,(norm(w[i]-w[i+1])+f)/s])
                        polyhedron( CubePoints, CubeFaces );