'''
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

Created on 15.09.2016

@author: rustr
'''

import math
from libraries.useful import clamp
import Rhino.Geometry as rg

def get_vector_sum(vectors):
    ''' returns the sum up all vectors'''
    return reduce(lambda x, y: x + y, vectors)

def get_vector_sum_Vector3d(vectors):
    ''' returns the sum up all vectors'''
    return rg.Vector3d(reduce(lambda x, y: x + y, vectors))

def angle_between_vectors(v1, v2):
    v1u = rg.Vector3d(v1.X, v1.Y, v1.Z)
    v2u = rg.Vector3d(v2.X, v2.Y, v2.Z)
    v1u.Unitize()
    v2u.Unitize()
    dot = v1u * v2u
    dot = clamp(dot, -1.0, 1.0)
    radians = math.acos(dot)
    return radians
    
def signed_angle_between_vectors(v1, v2, normal=None):
    '''Returns the signed angle between vectors, but only if you give a normal.'''
    v1u = rg.Vector3d(v1.X, v1.Y, v1.Z)
    v2u = rg.Vector3d(v2.X, v2.Y, v2.Z)
    v1u.Unitize()
    v2u.Unitize()
    dot = v1u * v2u
    dot = clamp(dot, -1.0, 1.0)
    radians = math.acos(dot)
    if not normal:
        return radians
    else:
        # check weather positive or negative
        v1u.Rotate(radians, normal) # now v1u must be v2u
        d = (v1u - v2u).Length
        if d < 0.01:
            return radians
        else:
            v1u.Rotate(- 2 *radians, normal)
            return -radians
    
def project_point_onto_line(point, lineA, lineB):
    s = lineA - lineB
    v = point - lineA
    pproj = lineA + s * (v * s)/(s * s) 
    return pproj

def get_fillet_radius_by_distance(start_pt, corner_pt, end_pt, distance):
    ''' Returns the radius for a fillet curve in a corner with distance 
    between corner point and tangent point. '''
    alpha = angle_between_vectors(start_pt - corner_pt, end_pt - corner_pt)
    beta = math.pi/2 - alpha/2
    radius = distance/math.sin(beta) * math.sin(alpha/2)
    return radius


if __name__ == "__main__":
    print "hello"