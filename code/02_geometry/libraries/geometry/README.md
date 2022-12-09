. . . . . . . . . . . . . . . . . . . . . 
.                                       .
.    <<      ><      ><       >< <<     .
.    < ><   ><<     ><<<    ><    ><<   .
.    << >< > ><    ><  ><     ><        .  
.    <<  ><  ><   ><<<<<><      ><      .
.    <<      >< ><<     ><< ><    ><<   .
.    <<      ><><<       ><<  >< <<     .
.                                       .
.             DFAB 2016/17              .
. . . . . . . . . . . . . . . . . . . . . 


# README #

### Description ###

 
The class "Frame" is initialized with a Rhino plane.
It is a generic class, that allows to derive the euler angles (KUKA), axis angle (UR), or quaternions (ABB) from this plane,
the transformation matrix to and from another plane, and also contains some transformation methods.
If no plane is given as an input, the origin of the plane is in world XY.
If draw_geo is set to true: the axes can be visualized as lines (length = 100)

quaternion definition: [qw, qx, qy, qz]
angle_axis definition: [ax,ay,az] (angle = length of the vector, axis = vector)   