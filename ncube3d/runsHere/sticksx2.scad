/* 
draw continous solid from one wertex to the next by 
extruding a cube of side s oriented towards its target
*/

include <cube.scad>;

$fn =3;s =70;f=s;
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
    if (norm(w[i]-w[i+1]) > 0) 
        translate((w[i]+w[i+1])/2)
            rotate([0,acos(((w[i+1]-w[i])[2])/(norm(w[i]-w[i+1]))),
                      atan2(((w[i+1]-w[i])[1]),((w[i+1]-w[i])[0]))])
                scale(v = [1,1,(norm(w[i]-w[i+1])+f)/s])
                    polyhedron( CubePoints, CubeFaces );
   
    for (i = [0 : 1 : len(w2)-2])
    if (norm(w2[i]-w2[i+1]) > 0) 
        translate((w2[i]+w2[i+1])/2)
            rotate([0,acos(((w2[i+1]-w2[i])[2])/(norm(w2[i]-w2[i+1]))),
                      atan2(((w2[i+1]-w2[i])[1]),((w2[i+1]-w2[i])[0]))])
                scale(v = [1,1,(norm(w2[i]-w2[i+1])+f)/s])
                    polyhedron( CubePoints, CubeFaces );
    
    for (i = [0 : 1 : len(w3)-2])
    if (norm(w3[i]-w3[i+1]) > 0) 
        translate((w3[i]+w3[i+1])/2)
            rotate([0,acos(((w3[i+1]-w3[i])[2])/(norm(w3[i]-w3[i+1]))),
                      atan2(((w3[i+1]-w3[i])[1]),((w3[i+1]-w3[i])[0]))])
                scale(v = [1,1,(norm(w3[i]-w3[i+1])+f)/s])
                    polyhedron( CubePoints, CubeFaces );
 