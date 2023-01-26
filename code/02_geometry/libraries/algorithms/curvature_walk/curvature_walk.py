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

Created on 11.10.2016

@author: rustr
'''

import Rhino.Geometry as rg
import math

def walk_along_curvature(srf, start_pt, step_size, follow, angle = 0.0, sign = +1, max_steps = 100000):
    ''' Start at one point on surface and walk along the curvature direction.
    Parameters: 
    srf:       surface
    start_pt:  point to start from
    step_size: the step towards the next point, depends on size of surface
    follow:    is 0 or 1, means follow minimal or maximal curvature direction. 
    angle:     modify the direction with angle (in radians).
    sign:      left or right in direction
    '''
    
    u_domain = rg.Surface.Domain(srf, 0)
    v_domain = rg.Surface.Domain(srf, 1)
    
    points = []
    points.append(start_pt)
    
    for i in range(max_steps):
        
        pt = points[-1]
        rc, u, v = rg.Surface.ClosestPoint(srf, pt)
        curvature = rg.Surface.CurvatureAt(srf, u, v)
        
        k1 = curvature.Kappa(0)
        k2 = curvature.Kappa(1)
        
        if k1 < k2:
            if follow == 0: # follow_minimum_curvature
                dir = curvature.Direction(0)
            else:
                dir = curvature.Direction(1)
        else: 
            if follow == 0: # follow_minimum_curvature
                dir = curvature.Direction(1)
            else:
                dir = curvature.Direction(0)

        dir *= sign
        dir.Rotate(angle, curvature.Normal)
        
        # Flip the direction 180 degrees if it seems to be going backwards
        if len(points) > 1:
            if dir.IsParallelTo(points[-1] - points[-2], 0.5 * math.pi) < 0:
                dir.Reverse()
                
        next_pt = pt + dir * step_size
    
        # bring back to srf
        rc, u, v = rg.Surface.ClosestPoint(srf, next_pt)
        
        if not rc or not u_domain.IncludesParameter(u, True) or not v_domain.IncludesParameter(v, True):
            break
            
        next_pt = rg.Surface.PointAt(srf, u, v)
    
        points.append(next_pt)
        
    return points

if __name__ == "__main__":
    
    pts1 = walk_along_curvature(S, P, step, follow, angle, sign = +1)
    pts2 = walk_along_curvature(S, P, step, follow, angle, sign = -1)
    
    